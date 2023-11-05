# Name:
# Description:

# dotenv (below) gets env from ~/.env (load b4 import openai)
from dotenv import load_dotenv
load_dotenv()
import os
import openai

#####
response = openai.ChatCompletion.create(
    # For GPT 3.5 Turbo, the model is "gpt-3.5-turbo"
    model="gpt-3.5-turbo",
    # Conversation as a list of messages.
    messages=[
        {"role": "system", "content": "You are a wize pirate."},
        {
            "role": "user",
            "content": "What is the best way to stop mutiny aboard \
            your ship?",
        },
    ],
)

# Extract the response
print(response['choices'][0]['message']['content'])
