from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
import re

load_dotenv()

def get_llm(llm="claude"):
        #instantiate the LLM
        if llm.lower()=="openai":
            # llm = ChatOpenAI(model="gpt-3.5-turbo")
            llm = ChatOpenAI(model="gpt-4o-mini")
        elif llm.lower()=="claude":
            claude_key= os.getenv("CLAUDE_API_KEY")
            llm = ChatAnthropic(
                api_key=claude_key,
                model_name = "claude-3-5-sonnet-20240620"
            )
        return llm

 

def format_response(message, tag):
    match = re.search(rf'\[{tag}\](.*?)\[/{tag}\]', message.content, re.DOTALL)

    if match:
        return  match.group(1).strip()  # Get the text and remove any leading/trailing whitespace


    else:
        return "No schema found"