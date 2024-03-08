# to run this code and get result you must have first generated an emb database with embedding using the 
from langchain.vectorstores.chroma import Chroma 
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from customRetriever import CustomRetriever

from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()

#get the database what was created when you ran chromaDB1.py once
db = Chroma(
    persist_directory="emb",
    embedding_function= embeddings,
)

# retriever = db.as_retriever()
retriever = CustomRetriever(
    embeddings = embeddings,
    chroma = db
)

#RetrievalQA is a chain that takes in the llm, the database to search
chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever = retriever,
    chain_type = "stuff"
)

while True:
    question = input(">> ")
    result = chain.run(question)
    print("*"*30)
    print(result)
    print("*"*30)