from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from redundant_filter_retriever import RedundantFilterRetriever
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv() 

embeddings = OpenAIEmbeddings() 
llm = ChatOpenAI(model="gpt-4-turbo")

db = Chroma(
    persist_directory="emb",
    embedding_function= embeddings
)

retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db)

chain = RetrievalQA.from_chain_type(
    llm = llm,
    retriever = retriever,
    chain_type = "stuff"
)

result = chain.invoke("What is an Interesting fact about English Language")

print(result)

