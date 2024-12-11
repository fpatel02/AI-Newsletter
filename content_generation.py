# AI Content generation

import os
from dotenv import load_dotenv, dotenv_values
import openai

load_dotenv

def generate_newsletter_content():
    openai.api_key = os.getenv("API_KEY")

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "Create a weekly newsletter about the latest tech news.",
        max_tokens = 500
    )   
    
    return response.choices[0].text.strip()