from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_openai_tools_agent, AgentExecutor
from code_generator import generate_model
from utilities import get_llm, format_response


#generate The Schema
def schema_generator(user_app_prompt ):

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
    llm = get_llm("openai")


    
    while True:
        # chat_input = input(":: ")

        if user_app_prompt.lower() in ('exit','quit','ok', 'q','x'):
            print("... Existing Django Application Generator")
            break

        messages.append(HumanMessage(content=user_app_prompt))
        result = llm.invoke(messages)
        output= result.content
        print("OUTPUT\n", output)

        messages.append(AIMessage(content=output))
        user_app_prompt = input(":: ")

    # return the last outputted result but only the schema part
    print("return final SCHEMA RESULT")
    if user_app_prompt.lower()=="ok":
        return messages
    else:
        return None
        


def main():
    # print("Enter the Application You want to develop")
    user_app_prompt = input("Enter the Application You want to develop-\n:: ")
    schema_response = schema_generator(user_app_prompt)
    #if a schema is generated
    if schema_response is not None:
        clean_schema = format_response(schema_response[-1],"schema") #get the schema alone from the response
        print(clean_schema)
        model_results = generate_model(clean_schema) #
        print("=====CODE generated=====")
        for result in model_results:
            print(result)
            print()
    else:
        print("- Exiting -")

if __name__=="__main__":
    main()