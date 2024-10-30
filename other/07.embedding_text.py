from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings()

emb=  embedding.embed_query("Hi there")

print(emb)