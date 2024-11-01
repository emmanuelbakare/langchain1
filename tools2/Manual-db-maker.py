from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from manual_make_model import generate_model


load_dotenv()


system_prompt = """ 
You are an expert Django database schema designer. 
            Create a database schema for the application name entered by user and modify as 
            specified by the user.
            Guidelines:
            1. Include all necessary tables but dont include tables that are not specific to this application
            2. Define appropriate fields for each table
            3. Consider relationships between tables
            4. Follow Django model best practices
            5. Your output response should be a list of the schema (tables and fields). 
            6. Your prefix description before the result output should be "SCHEMA SUGGESTION FOR <APPLICATION NAME>" 
                     under the description should be a double underline as a separator
            6. For suffix discription write "Type 'OK' if you are satisfied with this schema or 
                    further more instruction to modify (Add, update, Delete) any item in the schema"
            7. After user input is "OK"  then convert the last schema into a django model file, 
               then generate a file python with the write_code function 
               and name the file models.py
           8. format the output as shown below

Format:
<prefix description>
[schema]
   <list of tables and there structures>
[/schema]
<suffix description>

"""
 
messages= [system_prompt] 

#instantiate the LLM
llm = ChatOpenAI(model="gpt-4o-mini")


print("Enter the Application You want to develop")
while True:
    chat_input = input(":: ")

    if chat_input.lower() in ('exit','quit','ok'):
        print("... Existing Database Generator")
        break

    messages.append(HumanMessage(content=chat_input))
    result = llm.invoke(messages)
    output= result.content
    print("OUTPUT\n", output)

    messages.append(AIMessage(content=output))

if chat_input.lower()=="ok":
    generate_model(messages[-1])