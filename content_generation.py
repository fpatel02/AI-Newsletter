# AI Content generation

import os
from dotenv import load_dotenv, dotenv_values
import openai

load_dotenv("C:/Users/Owner/OneDrive/Desktop/Classes/Fall 2024/DS 3850/FinalProject/AINewsletter/AI-Newsletter/.env")

def generate_newsletter_content():
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    if openai.api_key is None:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Create a weekly newsletter about the latest tech news and summarize it into a clearly formatted list."}
        ],
        max_tokens = 500
    )   
    
    return response.choices[0].text.strip()