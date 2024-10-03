import streamlit as st
from audiorecorder import audiorecorder
import whisper
from applications.chatgpt import ask_chatgpt
from applications.card_styling import card_css
from pydantic import ValidationError
# from applications import notion # Uncomment this line if you want to use Notion
import os
import io

# Load the Whisper model
model = whisper.load_model('base')
st.markdown(card_css, unsafe_allow_html=True)

# Function to display each ticket with all fields inside a single card
def display_ticket(ticket):
    # Display all fields of the ticket inside a single "card"
    st.markdown(f'''
        <div class="card">
            <h4>{ticket.project}</h4>
            <div class="field">
                <span class="field-label">Priority: </span>
                <span class="field-value">{ticket.priority.value}</span>
            </div>
            <div class="field">
                <span class="field-label">Due Date: </span>
                <span class="field-value">{ticket.due_date}</span>
            </div>
            <div class="field">
                <span class="field-label">Description: </span>
                <span class="field-value">{ticket.description}</span>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Function to send a ticket to Notion (specific to the table schema)
# TODO: customize this function based on your Notion schema
def send_ticket_to_notion(ticket, database_id):
    due_date_str = ticket.due_date.isoformat() 
    new_page = {
        'parent': {'database_id': database_id},
        'properties': {
            'Description': {
                'title': [  # 'Description' is now the title field as per your schema
                    {
                        'text': {
                            'content': ticket.description  # Use 'description' as the title
                        }
                    }
                ]
            },
            'Project': {
                'select': {  # 'Project' is now a select field
                    'name': ticket.project
                }
            },
            'Priority Level': {
                'select': {  # 'Priority' remains a select field
                    'name': ticket.priority
                }
            },
            'Due Date': {
                'date': {  # 'Due Date' remains a date field
                    'start': due_date_str  # Use string date in 'YYYY-MM-DD' format
                }
            }
        }
    }
    # Create the page in Notion (add entry to the table)
    notion.pages.create(**new_page)

# Function to transcribe audio using Whisper
def transcribe_audio_from_audiosegment(audio_segment):
    # Export the audio as raw bytes (WAV format)
    audio_buffer = io.BytesIO()
    audio_segment.export(audio_buffer, format='wav')
    audio_buffer.seek(0)  # Reset the buffer to the beginning
    # Save the audio temporarily for Whisper to process
    with open('temp_audio.wav', 'wb') as f:
        f.write(audio_buffer.read())
    # Transcribe the audio with Whisper
    result = model.transcribe('temp_audio.wav')
    # Return the transcribed text
    return result['text']

# Main Streamlit app
def main():
    st.title(':parrot: Voice-to-Ticket Creator')
    # Use the audio recorder component
    audio = audiorecorder('Click to record', 'Click to stop recording')
    if len(audio) > 0:
        st.success('Audio recorded successfully!')
        transcript = transcribe_audio_from_audiosegment(audio) # The returned audio is an AudioSegment object, export it as needed
        st.info(f'Transcript: {transcript}')
        gpt_response = ask_chatgpt(transcript) # Send transcript to ChatGPT for ticket generation
        # st.write(f'GPT Response: {gpt_response}') # Check the structure of GPT response
        # Process the returned tickets (now a list of validated tickets)
        try:
            for ticket in gpt_response:  # gpt_response is already a list of validated Ticket objects
                display_ticket(ticket)
                # Send the ticket to Notion
                # send_ticket_to_notion(ticket, os.getenv('NOTION_DB_ID')) # Uncomment this line to send to Notion
        except ValidationError as e:
            st.write(f'Ticket validation error: {e}')
        st.success('Ticket(s) successfully sent to Notion!')

if __name__ == '__main__':
    main()
