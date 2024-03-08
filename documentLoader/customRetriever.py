from langchain.embeddings.base import Embeddings
from langchain.vectorstores.chroma import Chroma
from langchain.schema import BaseRetriever

class CustomRetriever(BaseRetriever):
    embeddings: Embeddings
    chroma: Chroma 

    def get_relevant_documents(self, query):
        #calculate the embedding for the DB
        emb= self.embeddings.embed_query(query)
        
        # take the embedding and feed it into  max_marginal_relevance_search_by_vector to remove duplicate
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8
        )
    
    async def aget_relevant_documents(self):
        return []