from langchain_openai import ChatOpenAI
from langchain_core.prompts import (ChatPromptTemplate,
                                    MessagesPlaceholder,
                                    HumanMessagePromptTemplate)
from langchain.agents import create_openai_functions_agent, AgentExecutor
from tools.sql import run_query_tool

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate(
    messages = [
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

# result = agent_executor.invoke({"input":"How many users are in the database?"})
result = agent_executor.invoke({"input":"How many users provided a shipping address?"})
print(result['output'])