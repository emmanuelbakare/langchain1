from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

messages = [
    SystemMessage(content="create your output in json format"),
    HumanMessage(content="group the book of psalms into 10 categories")
]

model = ChatOpenAI(model="gpt-4o-mini")
result = model.invoke(messages)

print(result)
print("REUSLT TYPE", type(result))

