from langchain_chroma.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embeddings= OpenAIEmbeddings()
db = Chroma(
 persist_directory="emb",
 embedding_function=embeddings
)
#calculate embedding for the query
#this line is not needed if you are using db.similary_search alone, 
# because db.similary_search will calculate the query embedding
query="What is an interesting fact about English Language"
embed_query = embeddings.embed_query(query)

#find similary by using the embedding we just created from the query
result = db.similarity_search_by_vector(embed_query)
#use result = db.similarity_search(query) if you are not using embedding the query

print(result) #list of relevant document after search

