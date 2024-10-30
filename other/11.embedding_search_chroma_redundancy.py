from langchain_chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings

#embedding
embeddings = OpenAIEmbeddings()
#chroma
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

query="What is an interesting fact about English Language"
embeded_query = embeddings.embed_query(query)

#search for embedded query and remove redundancy from the returned result 
result = db.max_marginal_relevance_search_by_vector(
    embedding= embeded_query,
    lambda_mult=0.8
)

print(result)

