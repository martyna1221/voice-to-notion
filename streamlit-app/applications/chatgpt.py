from applications import ai_client
from pydantic import BaseModel, ValidationError
from typing import List
import json
import os

# Define your LinkedInPost model using Pydantic
class LinkedInPost(BaseModel):
    content: str
    hashtags: List[str]

# Define a LinkedInPosts model that contains a list of LinkedInPost objects
class LinkedInPosts(BaseModel):
    posts: List[LinkedInPost]

def load_corpus():
    # Get the directory of the current file (chatgpt.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up one level to the streamlit-app directory
    streamlit_app_dir = os.path.dirname(current_dir)
    
    # The corpus directory is at the same level as applications
    corpus_dir = os.path.join(streamlit_app_dir, 'corpus')
    
    print(f"Attempting to access corpus directory: {corpus_dir}")
    
    if not os.path.exists(corpus_dir):
        print(f"Error: The corpus directory does not exist at {corpus_dir}")
        return "", ""
    
    guidelines = ""
    samples = ""
    
    try:
        for filename in os.listdir(corpus_dir):
            file_path = os.path.join(corpus_dir, filename)
            print(f"Reading file: {file_path}")
            with open(file_path, 'r') as file:
                content = file.read()
                if 'guidelines' in filename.lower():
                    guidelines += content + "\n\n"
                elif 'sample' in filename.lower():
                    samples += content + "\n\n"
    except Exception as e:
        print(f"Error reading corpus files: {str(e)}")
    
    return guidelines, samples

# TODO: pretty rough; improve prompting for better output
def ask_chatgpt(transcript):
    guidelines, samples = load_corpus()
    
    # Define the function schema using the LinkedInPosts class schema
    function_schema = {
        'name': 'createLinkedInPosts',
        'description': """Generate LinkedIn posts based on the provided transcript. 
        Use the guidelines and samples provided to craft engaging and professional posts.
        Each post should be concise, clear, and follow LinkedIn best practices.""",
        'parameters': LinkedInPosts.schema()
    }
    
    # Construct the prompt
    prompt = f"""
    LinkedIn Post Guidelines:
    {guidelines}

    Sample Posts:
    {samples}

    Transcript:
    {transcript}

    Using the LinkedIn post guidelines and sample posts provided above, create 3 LinkedIn posts based on the transcript. 
    Each post should be engaging, professional, and follow the best practices outlined in the guidelines. 
    Use the sample posts as inspiration for tone and structure, but ensure the content is unique and relevant to the transcript.
    Include relevant hashtags for each post.
    """

    # Call the OpenAI API with the function schema
    completion = ai_client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': prompt}],
        functions=[function_schema],
        function_call={"name": "createLinkedInPosts"},
        temperature=0.7
    )

    # Parse the function call response
    response = completion.choices[0].message.function_call.arguments
  
    # Load the function arguments (the posts) as JSON
    try:
        posts = json.loads(response)
        # Validate posts using the LinkedInPosts Pydantic model
        validated_posts = LinkedInPosts(**posts)
        return validated_posts.posts  # Return the list of validated posts
    except (json.JSONDecodeError, ValidationError) as e:
        print(f'Error: {e}')
        return []
