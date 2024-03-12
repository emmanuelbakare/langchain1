from langchain_community.chat_models import ChatOpenAI 
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder 
)
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent 
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferMemory

from tool2 import run_query_tool,   get_table_and_fields
from htmlGenerator import write_report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler
from dotenv import load_dotenv 


load_dotenv()
# tables = ", ".join(table[0] for table in list_tables() if table[0] is not None)

ai_msg =f"""
You are an AI that has access to a database with these tables \n
The database has tables  and fields using this format
Format:
<table>:field1,field2,... \n
{get_table_and_fields()} \n
Do not make any assumption of what database exist or what
column exist. Use the provided table and fields. 
"""
handler = ChatModelStartHandler()
llm = ChatOpenAI(
    callbacks = [handler]
)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
prompt = ChatPromptTemplate(
    messages= [
        SystemMessage(content=ai_msg),
        MessagesPlaceholder(variable_name = "chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name = "agent_scratchpad")
    ]
)



# tools = [run_query_tool, describe_table_tool, write_report_tool]
tools = [run_query_tool, write_report_tool]

agent = OpenAIFunctionsAgent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

agent_executor = AgentExecutor(
    agent = agent,
    tools = tools,
    verbose= True,
    memory= memory
)
while True:
    prompt_request = input(">> ")
    agent_executor(prompt_request)