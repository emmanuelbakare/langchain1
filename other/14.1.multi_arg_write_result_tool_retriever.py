from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts  import ( MessagesPlaceholder,
                                     ChatPromptTemplate,
                                     HumanMessagePromptTemplate)
from langchain_core.messages import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor 
from tools.sql import get_db_schema, run_query_tool
from tools.report import report_tool
load_dotenv()

llm = ChatOpenAI()

system_prompt = f"""
You a database administrator with access to an sqlite database.
Do not make assumption on the database schema.
use {str(get_db_schema())} to get the schema structure of the database"
"""
prompts = ChatPromptTemplate(
    messages=[
        SystemMessage(content= system_prompt),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

tools = [run_query_tool,report_tool]
agent = create_openai_functions_agent(
    prompt= prompts,
    llm = llm,
    tools = tools
)

executor = AgentExecutor(
    agent= agent,
    verbose=True,
    tools = tools
)

print(system_prompt)
# result = executor.invoke({"input":"How many users provided a shipping address?"})
result = executor.invoke({"input":"summarize the top 10 most popular product and write the result to a report file"})
print(result['output'])