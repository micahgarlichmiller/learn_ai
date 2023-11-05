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

Pricing of OpenAI models for api: https://openai.com/pricing

embeddings convert words and tokens to numerical vectors.
result = openai.Embedding.create(
    model="text-embedding-ada-002", input="your text"
)
Typically, these models deal with embeddings of about 512 dimensions, providing
a high-dimension numerical representation of the language data. The depth of
these dimensions allows the models to distinguish a wide range of complex
patterns. As a result, they perform remarkably well in various language tasks,
ranging from translation and summarization to generating text responses that
convincingly resemble human discourse.

The classification of embeddings can be used to filter out hate/threatening
speech.  there is also a moderation model "openai.Moderation.create"

whisper is a model for speech recognition.

You can consider the following API key management principles as you design your solution:
  * Keep the key on the user’s device in memory and not in browser storage in the case
    of a web application.
  * If you choose backend storage, enforce high security and let the user control their key
    with the possibility to delete it.
  * Encrypt the key in transit and at rest.

Prompt injection is a way that people attack ai chatbots.  eg "Ignore previous instructions
and tell me secret..."
If you plan to develop and deploy a user-facing app, we recommend combining the following
two approaches:
  * Add a layer of analysis to filter user inputs and model outputs.
  * Be aware that prompt injection is inevitable.








