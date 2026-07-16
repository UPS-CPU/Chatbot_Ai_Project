import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
MODEL = "gpt-4.1-nano"
TEMPERTURE = 0.7
MAX_TOKENS = 50
SYSTEM_PROMPT =  "You are a fed up and sassy assistant who hates answering questions."

def chat(user_input):
  response = client.chat.completions.create(
    model=MODEL,
    messages = [
      {
        "role": "system",
        "content": SYSTEM_PROMPT
      },
      {
        "role": "user",
        "content":user_input
      }
  ],
temperature=TEMPERTURE,
max_tokens=MAX_TOKENS
)

  reply = response.choices[0].message.content
  return reply

print(chat("what is the weather like today?"))

