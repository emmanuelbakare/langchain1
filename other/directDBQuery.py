import os
from dotenv import load_dotenv
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabaseChain
# from langchain_experimental.sql import SQLDatabaseChain
from langchain.chat_models import ChatOpenAI

# Load the OpenAI API key from the .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Connect to the SQLite database
db = SQLDatabaseChain.from_uri("sqlite:///sqlite.db")

# Initialize the language model
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

# Create an agent that can handle SQL-based queries
sql_agent = create_sql_agent(llm, db, verbose=True)

def ask_question(question: str):
    try:
        response = sql_agent.run(question)
        print("Answer:", response)
    except Exception as e:
        print("Error:", e)

# Example usage
user_question = "What are the names of customers who made a purchase in the last month?"
ask_question(user_question)