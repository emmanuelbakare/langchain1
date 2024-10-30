from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


embeddings = OpenAIEmbeddings()
db= Chroma(
    persist_directory="emb",
    embedding_function= embeddings
)

chatmodel = ChatOpenAI(model="gpt-4-turbo")
retriever = db.as_retriever()

chain  = RetrievalQA.from_chain_type(
    llm = chatmodel,
    retriever = retriever,
    chain_type = "stuff"
)

result= chain.invoke("What is an interesting fact about English Language")
print(result)
