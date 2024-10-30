from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder,SystemMessagePromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()
#memory initialization
memory = ConversationBufferMemory(memory_key="history", return_messages=True)
openai = ChatOpenAI(model="gpt-4-turbo")

prompt = ChatPromptTemplate(
    input_variables = ["input", "history"],
    messages = [
        SystemMessagePromptTemplate.from_template("Output only the result. Do not add a prefix or suffix explanation"),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)

chain = LLMChain(
    llm = openai,
    prompt = prompt,
    memory= memory
)

while True:
    my_chat = input("Question: ")
    if my_chat.lower()=="exit":
        break

    if len(my_chat) > 0 :
        result = chain.invoke({
            "input":my_chat
        })
        print(result)

