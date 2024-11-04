from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from two_model_generator import generate_model
from three_djangotools import format_response
import os

load_dotenv()

class DjangoGenerator:
    def __init__(self, llm="openai") -> None:
        self.llm = self.get_llm() 
        self.prompt ="" 

    def get_llm(self, llm="claude"):
        #instantiate the LLM
        if llm.lower()=="openai":
            # llm = ChatOpenAI(model="gpt-3.5-turbo")
            llm = ChatOpenAI(model="gpt-4o-mini")
        elif llm.lower()=="claude":
            claude_key= os.getenv("CLAUDE_API_KEY")
            llm = ChatAnthropic(
                api_key=claude_key,
                model_name = "claude-3-5-sonnet-20240620"
            )
        return llm
    
    def schema_generator(self, user_app_prompt ):

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

         


        
        while True:
            # chat_input = input(":: ")

            if user_app_prompt.lower() in ('exit','quit','ok'):
                print("... Existing Schema Generator")
                break

            messages.append(HumanMessage(content=user_app_prompt))
            result = self.llm.invoke(messages)
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