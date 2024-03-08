# embedding is rating a sentence into different feeling or parameters to decide what it means or intends to achieve
# embedding are stored in list of number ranging from 1 to -1 - this are called dimensions.
# openAIEmbedding as 1536 dimensions while SentenceTransformer embedding as about 768 dimension.
# openAEmbedding is more accurate but expensive to generate ($).
# convert "Hello World" to an Embedding code
from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv() 

embedding = OpenAIEmbeddings() #use OpenAI Embedding

emb = embedding.embed_query("Hello World")  #Embed "Hello World" into dimentional data (list of numbers between -1 to 1)

print(emb)