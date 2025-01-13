# This file will serve a wrapper for the GPT-2 model. It will be used to generate text based on the input prompt.
from openai import OpenAI
import streamlit as st

api_key = st.secrets["api_key"]

# Create a client
client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-4o", messages=[{"role": "user", "content": "write a haiku about ai"}]
)
print(response.choices[0].message.content)
