from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()
# openai_key = os.getenv("OPENAI_KEY_TWO")

# chat= ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)
chat= ChatOpenAI(model="gpt-4o-mini")


result = chat.invoke("Write a very short poem")

print(result.content)
