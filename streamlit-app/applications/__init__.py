from dotenv import load_dotenv
from google.cloud import firestore
import os
from openai import OpenAI

load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './key.json'

db = firestore.Client()
# ai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
