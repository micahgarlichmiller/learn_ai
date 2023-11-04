# learn_ai
Learning to use AI with python

Misc Notes:
cd ~/github/learn_ai
source ~/github/my_venv/bin/activate
pip install openai #already done
pip install -U python-dotenv # already done
my OPENAI_API_KEY set in ~/.env

Cmd line example that works when you have OPENAI_API_KEY set in your shell:
openai api chat_completions.create -m gpt-3.5-turbo \
    -g user "Hello world"

GPT 3.5 Turbo is the least expensive and most versatile model. Therefore,
it is also the best choice for most use cases.

ChatCompletion takes An array of message objects representing a conversation.
A message object has two attributes: role (possible values are system, user,
and assistant) and content (a string with the conversation message).  system
is optional, after that you can have multi user/assistant

API reference for ChatCompletion: 
https://platform.openai.com/docs/api-reference/chat/create

How to count tokens with tiktoken:
https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken





