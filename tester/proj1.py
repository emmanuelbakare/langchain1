from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_core.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate)
from dotenv import load_dotenv 

load_dotenv()


system_message= SystemMessage(content="""
    You are an System design expert. You are to develop breakdown application to be developed into modules
    you have 3 options to chose from if client/user as you to develop an application
    1. It the user input is a know application and the application as other standalone sub modules, then list the standalonesub modules in this format
       [Submodules]
        <list of application submodules>: <description>
       [/submodules]
    2. It the user input is a know application and the application is a standalone modules without sub modules then list the tables the application will require in this format
        [tables]
        <tabe name>:[<table fields>]
        [/tables]
    3. If the application name is not familiar the output
         [app-unknown]
            <description illustrating the the name is not a know application and suggesting user to provide more information>
        [/app-unknown]     
                              
                              
    
""")
chat = ChatOpenAI(model="gpt-4o-mini")

ask_app = input("What Application do you want to develop: ")


messages= [system_message]

messages.append(HumanMessage(content=ask_app))

result = chat.invoke(messages)

print(result.content)
