from langchain_openai import ChatOpenAI
from langchain_core.prompts import (ChatPromptTemplate,
                                    MessagesPlaceholder,
                                    HumanMessagePromptTemplate)
from langchain_core.messages import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from tools.sql import run_query_tool, get_db_schema 

from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI()
system_prompt = f"""
    You are an AI assistance with access to an sqlite database.
    use the database schema below to generate the query
    { str(get_db_schema())} 
    this schema contains a key value pair of table name and corresponding fields in this format
    <table_name>:<fields1, field2,...>
    use only these tables to generate the queries and make no assumptions
"""

prompt = ChatPromptTemplate(
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

tools = [run_query_tool]
agent = create_openai_functions_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)
 
agent_executor = AgentExecutor(
    agent= agent,
    tools = tools,
    verbose = True
)
print("*"*80)
print(system_prompt)
print("*"*80)
# result = agent_executor.invoke({"input":"How many users are in the database?"})
result = agent_executor.invoke({"input":"How many users provided a shipping address?"})
print(result['output'])