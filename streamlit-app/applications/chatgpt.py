from applications import ai_client

def ask_chatgpt(prompt):
    completion = ai_client.chat.completions.create(model='gpt-4o',messages=[{'role': 'user', 'content': f'{prompt}'}])
    text_response = completion.choices[0].message.content
    return text_response
