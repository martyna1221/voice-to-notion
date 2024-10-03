from applications import ai_client
from pydantic import BaseModel, ValidationError
from typing import List
from enum import Enum
from datetime import date
import json

# Define the Priority Enum based on the options in your screenshot
class Priority(str, Enum):
    critical = 'Critical'
    urgent = 'Urgent'
    normal = 'Normal'
    low_priority = 'Low Priority'
    icing = 'Icing'

# Define your Ticket model using Pydantic
class Ticket(BaseModel):
    # author: str
    project: str
    priority: Priority
    due_date: date
    description: str

# Define a Tickets model that contains a list of Ticket objects
class Tickets(BaseModel):
    tickets: List[Ticket]

def ask_chatgpt(prompt):
    # Define the function schema using the Tickets class schema
    function_schema = {
        'name': 'createTickets',
        'description': f"""Generate tickets based on the provided transcription. The field Priority can only take on a couple of options: 
        {', '.join([priority.value for priority in Priority])}.
        Today's date is {date.today().isoformat()}.
        The descriptions should be consice and clear but descriptive. I want good grammar as well.""",
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
