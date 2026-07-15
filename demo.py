import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
model="gpt-4.1-nano",
messages = [
  {
    "role": "system",
    "content": "You are a fed up and sassy assistant who hates answering questions."
  },
  {
    "role": "user",
    "content": "what is the weather like today?"
  }
],
temperature=0.7,
max_tokens=100
)

reply = response.choices[0].message.content
print(reply)