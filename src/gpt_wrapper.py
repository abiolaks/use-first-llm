# This file will serve a wrapper for the GPT-2 model. It will be used to generate text based on the input prompt.
from openai import OpenAI

api_key = "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"

# Create a client
client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-4o", messages=[{"role": "user", "content": "write a haiku about ai"}]
)
print(response.choices[0].message.content)
