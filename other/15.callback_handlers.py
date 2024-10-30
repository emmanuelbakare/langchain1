from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tools.sql import get_db_schema, run_query_tool
from tools.report import report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler

from dotenv import load_dotenv
load_dotenv()

llm= ChatOpenAI(
    callbacks=[ChatModelStartHandler()]
)
memory = ConversationBufferMemory(memory_key="mem_history",return_messages=True)
system_prompt = f""" 
You a database administrator with access to an sqlite database.
Do not make assumption on the database schema.
use {str(get_db_schema())} to get the schema structure of the database"
"""
prompts = ChatPromptTemplate(

    messages = [
        SystemMessage(content=system_prompt),
        MessagesPlaceholder(variable_name="mem_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

tools =[run_query_tool, report_tool]

agent = create_openai_functions_agent(
    prompt= prompts,
    llm = llm,
    tools = tools    
)


executor = AgentExecutor(
    agent = agent,
    # verbose =True,
    tools = tools,
    memory = memory
)


print(system_prompt)
# result = executor.invoke({"input":"How many users provided a shipping address?"})

while True:

    input_prompt = input("Ask: ")

    if input_prompt.lower()=="exit" or input_prompt.lower()=="quit":
        break

    result = executor.invoke({"input":input_prompt})
    print("="*50)
    print(result['output'])
    print("="*50)

  