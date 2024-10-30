from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tools.sql import get_db_schema, run_query_tool
from tools.report import report_tool

from dotenv import load_dotenv
load_dotenv()

# Initialize LLM
llm = ChatOpenAI()


# Updated system prompt
system_prompt = f"""
You are a database administrator with access to an SQLite database.
Refer to the following schema structure: {str(get_db_schema())}
"""

# Set up memory with a token limit to avoid overflow
memory = ConversationBufferMemory(
    memory_key="mem_history", 
    return_messages=True, 
    )

# Define the prompt
prompts = ChatPromptTemplate(
    messages=[
        SystemMessage(content=system_prompt),
        MessagesPlaceholder(variable_name="mem_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

# Define tools
tools = [run_query_tool, report_tool]

# Create agent
agent = create_openai_functions_agent(
    prompt=prompts,
    llm=llm,
    tools=tools
)

# Executor
executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
    memory=memory
)

# Main loop
while True:
    input_prompt = input("Ask: ")

    if input_prompt.lower() in ["exit", "quit"]:
        break

    try:
        result = executor.invoke({"input":input_prompt})
        print("=" * 50)
        print(result['output'])
        print("=" * 50)
    except Exception as e:
        print(f"Error: {e}")
