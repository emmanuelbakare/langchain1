from langchain_core.messages import SystemMessage
from langchain_core.prompts import (HumanMessagePromptTemplate,
                                    ChatPromptTemplate,
                                    MessagesPlaceholder)
from langchain_anthropic import ChatAnthropic
from langchain.tools import StructuredTool 
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tool1 import code_writer
from dotenv import load_dotenv
import os

load_dotenv()

class APPdbSchemaMaker:
    def __init__(self):
        self.system_prompt = """
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
            
            
        """
        #llm initialization
        self.llm = ChatAnthropic(
            anthropic_api_key = os.getenv("CLAUDE_API_KEY"),
            model_name = "claude-3-5-sonnet-20240620"
        )

        #create Memory
        self.memory = ConversationBufferMemory(
                    memory_key="chat_history", 
                    return_messages=True)

        #prompt template
        self.prompt = ChatPromptTemplate(
            input_variable= ["input"],
            messages=[
              self.system_prompt,
              MessagesPlaceholder(variable_name="chat_history"),
              HumanMessagePromptTemplate.from_template("{input}"),
              MessagesPlaceholder(variable_name="agent_scratchpad")

            ]
        )

        
    # def create_code_writer_tool(self):

    #     def write_code(generated_code, filename="generate_code.py"):
    #         pass

    #     return StructuredTool.from_function(
    #         name="code_writer",


    #     )

    def setup_agent(self):
        tools = [code_writer]

        agent = create_tool_calling_agent(
            prompt= self.prompt,
            llm = self.llm,
            tools = tools
        )

        executor = AgentExecutor(
            agent = agent,
            tools = tools,
            memory = self.memory,
            verbose = True
        )

        return executor

    
    #auto code generator
    def automatic_code_gen(self):
        executor = self.setup_agent()
        print("Which application do you want to Build")

        while True:
            user_input = input(":: ")

            if user_input.lower() in ('exit', 'quit','ok','q'):
                print("...exiting Django Model Generator")
                break

            try:
                result = executor.invoke({"input":user_input})
                print("OUTPUT")
                formatted_output=result['output'][0]['text']
                print(formatted_output)
                
                 
            except Exception as err:
                print(f"An error occurred during code generation {str(err)}")
                return f"Error message: {str(err)}"



def main():
    app = APPdbSchemaMaker()
    app.automatic_code_gen()

if __name__ == "__main__":
    main()    




        