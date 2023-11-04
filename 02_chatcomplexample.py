# Name:
# Description:

# dotenv (below) gets env from ~/.env (load b4 import openai)
from dotenv import load_dotenv
load_dotenv()
import os
import openai

#####
# in the below question "What is it?" the model has the context of the 
# preceding roles that were included in the message.  This is to show
# that the api doesnt have context unless you provide it. (at the current time)
response = openai.ChatCompletion.create(
    # For GPT 3.5 Turbo, the model is "gpt-3.5-turbo"
    model="gpt-3.5-turbo",
    # Conversation as a list of messages.
    messages=[
        {"role": "system", "content": "You are a helpful teacher."},
        {
            "role": "user",
            "content": "Are there other measures than time complexity for an \
            algorithm?",
        },
        {
            "role": "assistant",
            "content": "Yes, there are other measures besides time complexity \
            for an algorithm, such as space complexity.",
        },
        {"role": "user", "content": "What is it?"},
    ],
)

# Extract the response
print(response['choices'][0]['message']['content'])
