#================= add the ability to store message im message.json with FileChatMessageHistory
# ========such that when the user exit the program and come back in the chat still remembers the previous conversation
#== The message trail is stored in messages.json  as specified with FileChatMessageHistory("messages.json")
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

memory = ConversationBufferMemory(
    chat_memory= FileChatMessageHistory("messages.json"),
    memory_key="messages", 
    return_messages=True,
    )
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
)

while True:
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])
