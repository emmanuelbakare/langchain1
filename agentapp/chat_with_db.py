from langchain_community.chat_models import ChatOpenAI 
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder 
)
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent 
from tool import run_query_tool
from dotenv import load_dotenv 

load_dotenv()

llm = ChatOpenAI()
prompt = ChatPromptTemplate(
    messages= [
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name = "agent_scratchpad")
    ]
)

agent = OpenAIFunctionsAgent(
    llm = llm,
    prompt = prompt,
    tools = [run_query_tool]
)

agent_executor = AgentExecutor(
    agent = agent,
    tools = [run_query_tool],
    verbose= True
)

while True:
    prompt_request = input(">> ")
    agent_executor(prompt_request)