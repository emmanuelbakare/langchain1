# this code will load a text with TextLoader, Split it into chunks with CharacterTextSplitter and 
# embedd the chunks with embeddings inside a vectore db called chromadb with Chroma.from_documents
# then uses db.similarity_search or  db.similarity_search_with_score to search for a particuar text from the stored data in the chromadb

# the problem with this code is everytime you run this code, it regenerate the embeddings inside same database
# thereby creating dublicate embeddings. 
# There is need to seperat the code that generate the Chroma from the code that does the searching so that the database is generate once and 
# multiple searching can be done on it - this is done in example 10. chromaDbPrompt.py
# this file (chromaDB1.py) is run once to generate the database then we switch to 10. chromaDbPrompt.py to keep running different search on the db generated
from langchain.document_loaders import TextLoader 
from langchain.text_splitter import CharacterTextSplitter 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma 


#create a text splitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size =200,
    chunk_overlap = 0
)

#load the text
loader = TextLoader("facts.txt")

# splite the text in the loader using the textsplitter
docs = loader.load_and_split(
    text_splitter = text_splitter
)

#initiated an Embedding instance
embeddings = OpenAIEmbeddings()

# create a chroma dataase, which embed the splitted text into a database called emb.
db = Chroma.from_documents(
    docs,
    embedding= embeddings,
    persist_directory="emb"
)

#search the vector database using this text to compare the most similar embedding in the chroma database
#this generate 4 result by default if you add the parameter k=n (n is number) it only generate n most similar result 
results = db.similarity_search(
    "What is an interesting fact about the English language",
)

for result in results:
    print(result.page_content)
    print()

# this generate only one result that is the most similar
# results = db.similarity_search(
#     "What is an interesting fact about the English language",
#     k=1
# )


# this generate 4 results and also shows the embedding score for each one
result = db.similarity_search_with_score(
    "What is an interesting fact about the English language",
)

# for result in results:
#     print(result[1]) # displays the embedding score
#     print(result[0].page_content) # display related content

