from dotenv import load_dotenv
import os
from openai import OpenAI
from notion_client import Client

load_dotenv()

ai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# notion = Client(auth=os.getenv('NOTION_API_KEY')) # Uncomment this line if you want to use Notion
