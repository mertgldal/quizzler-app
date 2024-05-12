import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Open trivia 'API_URL'
response = requests.get(os.getenv('API_URL'))
data = response.json()

question_data = data['results']