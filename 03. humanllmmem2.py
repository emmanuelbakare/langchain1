# =========== Add the ability to remember message using the  ConversationBufferMemory 
# ============that stores all messages in a buffer named 'messages' in this example
#====== Only downside is that when user exit the program and comes back in previous message history will be lost
# humanllmmem3.py address the issue
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory 

from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI()

#create the memory to store the conversation
memory = ConversationBufferMemory(
    memory_key="messages", 
    return_messages=True,
    )

#create the prompt
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

#generate the chain
chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
)

while True:
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])
