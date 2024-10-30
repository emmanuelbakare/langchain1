from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage,HumanMessage


load_dotenv()
messages= [
    SystemMessage(content="output only the response. do not add a prefix or suffix description")
]

chat = ChatOpenAI(model="gpt-4o-mini")
result = ""
while True:
    #1. check if the final word in an output is a particle word or patthern
    #2. if it not e.g. </html> then let chat_input='continue' else allow entering a quesition
    
    chat_input=input("Question: ")

    if chat_input.lower()=="exit":
        break
    humanchat = HumanMessage(content=chat_input)
    messages.append(humanchat)
    result = chat.invoke(messages)
    output =result.content
    print("Answer: ",output)
    messages.append(AIMessage(content=output))

    

print(messages)