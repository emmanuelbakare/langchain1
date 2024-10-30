from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tools.sql import get_db_schema, run_query_tool
from tools.report import report_tool

from dotenv import load_dotenv
load_dotenv()

llm= ChatOpenAI()
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
    verbose =True,
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

 

 ######TEST Questions - USING ONLY SYSTEM PROMPT
#  list the top 10 product ordered
# list the top 10 customer and how much they spent
# list all products, how many times it was ordered and total amount sold. generate an html report 
     # errro in question 3
    #total context - 16,385
    #total used context- 19,363
    #messages in functions  -72


##################################################################
"""Here are the top 10 products ordered:

1. Unbranded Pizza - 10 orders
2. Refined Chips - 9 orders
3. Generic Ball - 8 orders
4. Fresh Bike - 8 orders
5. Sleek Pizza - 8 orders
6. Rubber Mouse - 8 orders
7. Steel Table - 8 orders
8. Gorgeous Fish - 8 orders
9. Steel Bike - 8 orders
10. Plastic Salad - 7 orders
"""


##################################################################
"""
Here are the top 10 customers and how much they spent:

1. Justin Mccall - $174
2. Jonathan Cannon - $172
3. Miss Karen Knight - $168
4. Kyle Reynolds - $167
5. Michael Gray - $166
6. Robert Rivas - $160
7. Ronald Johnson - $152
8. Nicole Mora - $149
9. Robin Boyd - $144
10. Stephanie Simmons - $139
"""

# Conclusion - Using sytem prompt will generate less token