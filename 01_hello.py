# Name: hello.py
# Description: hello world using openai

# dotenv (below) gets env from ~/.env (load b4 import openai)
from dotenv import load_dotenv
load_dotenv()
import openai

#####
# Call the openai ChatCompletion endpoint, with th ChatGPT model
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

# Extract the response
print(response['choices'][0]['message']['content'])
