import streamlit as st
from audiorecorder import audiorecorder
import whisper
from applications.chatgpt import ask_chatgpt
from applications.card_styling import card_css
from pydantic import ValidationError
import io

# Load the Whisper model
model = whisper.load_model('base')
st.markdown(card_css, unsafe_allow_html=True)

# TODO: add copy to clipboard button
def display_post(post):
    # Display all fields of the LinkedIn post inside a single "card"
    st.markdown(f'''
        <div class="card">
            <h4>LinkedIn Post</h4>
            <div class="field">
                <span class="field-value">{post.content}</span>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Function to transcribe audio using Whisper
def transcribe_audio_from_audiosegment(audio_segment):
    # Export the audio as raw bytes (WAV format)
    audio_buffer = io.BytesIO()
    audio_segment.export(audio_buffer, format='wav')
    audio_buffer.seek(0) # Reset the buffer to the beginning
    # Save the audio temporarily for Whisper to process
    with open('temp_audio.wav', 'wb') as f:
        f.write(audio_buffer.read())
    # Transcribe the audio with Whisper
    result = model.transcribe('temp_audio.wav')
    # Return the transcribed text
    return result['text']

# Main Streamlit app
def main():
    st.title(':parrot: Voice2LinkedIn')
    # Use the audio recorder component
    audio = audiorecorder('Click to record', 'Click to stop recording')
    if len(audio) > 0:
        st.success('Audio recorded successfully!')
        transcript = transcribe_audio_from_audiosegment(audio) # The returned audio is an AudioSegment object, export it as needed
        st.info(f'Transcript: {transcript}')
        gpt_response = ask_chatgpt(transcript) # Send transcript to ChatGPT for post generation
        # st.write(f'GPT Response: {gpt_response}') # Check the structure of GPT response
        try:
            for post in gpt_response:
                display_post(post)
        except ValidationError as e:
            st.write(f'Post validation error: {e}')

if __name__ == '__main__':
    main()
