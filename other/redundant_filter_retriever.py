
from langchain.schema import BaseRetriever
from langchain.embeddings.base import Embeddings
from langchain_chroma import Chroma 

# this class is loaded inside 12.cusotm_retriever.py as the redundant remove

class RedundantFilterRetriever(BaseRetriever):
    embeddings: Embeddings
    chroma: Chroma 


    def get_relevant_documents(self, query):
        #embed the query
        embeded_query= self.embeddings.embed_query(query)

        #generate non redundant chain from chroma using max_marginal_revelance_search_by_vector
        result = self.chroma.max_marginal_relevance_search_by_vector(
            embedding = embeded_query,
            lambda_mult= 0.8
            )

        return result
    
    async def aget_relevant_documents(self):

        return []
    



    
