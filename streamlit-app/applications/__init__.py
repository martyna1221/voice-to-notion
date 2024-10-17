from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

ai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
