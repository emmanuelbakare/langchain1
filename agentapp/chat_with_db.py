from langchain_community.chat_models import ChatOpenAI 
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder 
)
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent 
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferMemory
from tool import run_query_tool, list_tables, describe_table_tool
from htmlGenerator import write_report_tool
from dotenv import load_dotenv 

load_dotenv()
tables = ", ".join(table[0] for table in list_tables() if table[0] is not None)

ai_msg =f"""
You are an AI that has access to a database with these tables \n
The database has tables of {tables} \n
Do not make any assumption of what database exist or what
column exist. Instead, use the 'describe_tables' function
"""
print(ai_msg)
llm = ChatOpenAI()
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

tools = [
        run_query_tool, 
        describe_table_tool,
        write_report_tool]

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

# agent_executor("how many users have provided a shipping address")