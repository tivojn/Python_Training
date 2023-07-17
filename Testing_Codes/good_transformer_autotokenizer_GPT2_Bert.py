from transformers import AutoTokenizer
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
text_input = input('Please input your prompt: ')
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with statements, and your task is to convert them to standard English."
    },
    {
      "role": "user",
      "content": text_input
    }
  ],
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print (response)
# Load the tokenizer
#tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# The text to count tokens for
text_response = response.choices[0].message["content"]

# Encode the text to count tokens
encoded_response = tokenizer.encode(text_response)
encoded_input = tokenizer.encode(text_input)

# Count the number of tokens
num_tokens_input = len(encoded_input)
num_tokens_response = len(encoded_response)

print(f"Input is '{text_input}'' and it used: {num_tokens_input} tokens")
print(f"Response is : '{text_response}' and it used: {num_tokens_response} tokens calculated via {tokenizer}")
print (f'The response used {response.usage["completion_tokens"]} tokens calculated via response.usage.')
