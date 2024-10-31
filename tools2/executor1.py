import os
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_openai  import ChatOpenAI
from langchain.tools import Tool
from tool1 import code_writer
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI API Key

system_message=SystemMessage(content="""
        Generate a python code and store the code in a python file using the function call.
         
""")
# Define your prompt template
prompt_template = ChatPromptTemplate(
    input_variables=["code_request"],
    messages= [
        system_message,
        HumanMessagePromptTemplate.from_template("{code_request}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

# Create an OpenAI language model instance
llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = [code_writer]
# Create an agent with the prompt
agent = create_openai_tools_agent(
    llm=llm, 
    prompt=prompt_template,
    tools=tools
)
# Create an AgentExecutor
executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# Define the code generation request

code_request = input("Enter the code request: ") 

# # Run the executor to get the generated code
result = executor.invoke({"code_request":code_request})
print("FINAL RESULT\n",result['output'])


print(f"Code generated and written to file:")
 
