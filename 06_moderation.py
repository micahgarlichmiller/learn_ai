
# Name:
# Description:

# dotenv (below) gets env from ~/.env (load b4 import openai)
from dotenv import load_dotenv
load_dotenv()
import os
import openai

#####
# Call the openai Moderation endpoint, with the text-moderation-latest model
response = openai.Moderation.create(
    model="text-moderation-latest",
    input="This is a safe example, you could put something nasty here and compare output.",
)

# Extract the response
print(response)
