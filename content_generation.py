# AI Content generation

import openai

def generate_newsletter_content():
    openai.api_key = '[api key]'

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "Create a weekly newsletter about the latest tech news.",
        max_tokens = 500
    )   
    
    return response.choices[0].text.strip()