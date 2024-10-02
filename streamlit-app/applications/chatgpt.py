from applications import ai_client
from pydantic import BaseModel, ValidationError
from typing import List
from datetime import date
import json

# Define your Ticket model using Pydantic
class Ticket(BaseModel):
    # author: str
    project: str
    priority: str
    due_date: date
    description: str

# Define a Tickets model that contains a list of Ticket objects
class Tickets(BaseModel):
    tickets: List[Ticket]

def ask_chatgpt(prompt):
    # Define the function schema using the Tickets class schema
    function_schema = {
        'name': 'createTickets',
        'description': 'Generate tickets based on the provided transcription.', # TODO: include today's date; GPT is stuck in 2023
        'parameters': Tickets.schema()  # Use Tickets schema
    }
    # Call the OpenAI API with the function schema
    completion = ai_client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': prompt}],
        functions=[function_schema],
        temperature=.5
    )
    # Parse the function call response
    response = completion.choices[0].message.function_call.arguments
    # Load the function arguments (the tickets) as JSON
    try:
        tickets = json.loads(response)
        # Validate tickets using the Tickets Pydantic model
        validated_tickets = Tickets(**tickets)
        return validated_tickets.tickets  # Return the list of validated tickets
    except (json.JSONDecodeError, ValidationError) as e:
        print(f'Error: {e}')
        return []
