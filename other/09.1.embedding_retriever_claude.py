from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
load_dotenv()

claude_api = os.getenv("CLAUDE_KEY")


embeddings = OpenAIEmbeddings()
db= Chroma(
    persist_directory="emb",
    embedding_function= embeddings
)

#llm
chatmodel = ChatAnthropic(
    anthropic_api_key = claude_api,
    model_name="claude-3-5-sonnet-20240620"
    )
#retriever
retriever = db.as_retriever()

#retriever chain
chain  = RetrievalQA.from_chain_type(
    llm = chatmodel,
    retriever = retriever,
    chain_type = "stuff"
)

result= chain.invoke("What is an interesting fact about English Language")
print(result["result"])
