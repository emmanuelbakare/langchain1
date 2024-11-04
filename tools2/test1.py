from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate, HumanMessagePromptTemplate
from utilities import get_llm
from tool1 import code_writer

prompt_message ="""
You are a database django schema developer. Your goal is to create django models code for these schema info.
1. **Employee**
   - id (AutoField, Primary Key)
   - first_name (CharField, max_length=50)
   - last_name (CharField, max_length=50)
   - email (EmailField, unique=True)
   - phone_number (CharField, max_length=15)
   - hire_date (DateField)
   - position (CharField, max_length=100)
   - department (ForeignKey to Department, on_delete=models.CASCADE)
   - created_at (DateTimeField, auto_now_add=True)
   - updated_at (DateTimeField, auto_now=True)

2. **Department**
   - id (AutoField, Primary Key)
   - name (CharField, max_length=100, unique=True)
   - created_at (DateTimeField, auto_now_add=True)
   - updated_at (DateTimeField, auto_now=True)

3. **Manager**
   - id (AutoField, Primary Key)
   - employee (OneToOneField to Employee, on_delete=models.CASCADE)
   - created_at (DateTimeField, auto_now_add=True)
   - updated_at (DateTimeField, auto_now=True)
 
Generate the django code and store it in a models.py folder using the code_writer function.
"""

# output only the result no prefix or suffix description should be added 
# Generate the django code and store it in a models.py folder using the code_writer function.


llm = get_llm("claude")
prompt = ChatPromptTemplate(
    messages = [
        HumanMessagePromptTemplate.from_template(prompt_message),
        MessagesPlaceholder(variable_name="agent_scratchpad")
        
    ]
)

# chat = prompt | llm 

# result =  chat.invoke(input={})
# code =result.content 

 
tools = [code_writer]

agent = create_tool_calling_agent(
    llm=llm,
    prompt= prompt,
    tools= tools
)

executor = AgentExecutor(
    agent = agent,
    verbose=False,
    tools = tools
)
print("Generating the schema models. Please wait...")
result = executor.invoke(input={})

#openai output
# print(result['output']) 

#claude output
print(result['output'][0]['text'])