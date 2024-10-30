from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tools.sql import get_db_schema, run_query_tool, full_db_schema
from tools.report import report_tool

from dotenv import load_dotenv
load_dotenv()


llm= ChatOpenAI(model="gpt-4-turbo")
memory = ConversationBufferMemory(memory_key="mem_history",return_messages=True)
system_prompt = f""" 
You a database administrator with access to an sqlite database.
Do not make assumption on the database schema.
use  full_db_schema function tool to get the schema structure of the database"
"""
prompts = ChatPromptTemplate(

    messages = [
        SystemMessage(content=system_prompt),
        MessagesPlaceholder(variable_name="mem_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

tools =[run_query_tool, report_tool, full_db_schema]

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


 ######TEST Questions - USING FUNCTION TOOLS
#  list the top 10 product ordered
# list the top 10 customer and how much they spent
# list all products, how many times it was ordered and total amount sold. generate an html report 
     # errro in question 3
    #total context - 16,385
    #total used context- 58,625
    #messages in functions  -103

 ##################################################################
"""
 Here are the top 10 products ordered along with the number of times they have been ordered:

1. Product ID: 3929, Total Ordered: 10
2. Product ID: 1437, Total Ordered: 9
3. Product ID: 3192, Total Ordered: 8
4. Product ID: 3115, Total Ordered: 8
5. Product ID: 2091, Total Ordered: 8
6. Product ID: 1657, Total Ordered: 8
7. Product ID: 1576, Total Ordered: 8
8. Product ID: 1392, Total Ordered: 8
9. Product ID: 248, Total Ordered: 8
10. Product ID: 3694, Total Ordered: 7
 """

 ##################################################################
""" 
Here are the top 10 customers based on how much they have spent:

1. Customer: Justin Mccall, Total Spent: $174      
2. Customer: Jonathan Cannon, Total Spent: $172    
3. Customer: Miss Karen Knight, Total Spent: $168  
4. Customer: Kyle Reynolds, Total Spent: $167      
5. Customer: Robert Rivas, Total Spent: $160       
6. Customer: Ronald Johnson, Total Spent: $152     
7. Customer: Nicole Mora, Total Spent: $149        
8. Customer: Robin Boyd, Total Spent: $144
9. Customer: Stephanie Simmons, Total Spent: $139  
10. Customer: Laura Carpenter, Total Spent: $134
 """