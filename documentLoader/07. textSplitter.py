# split a text file into chunks using CharacterTextSplitter. ie. load the document and split them to different chunks
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

#get the openai key
from dotenv import load_dotenv
load_dotenv()

#configue the text_splitter
text_splitter = CharacterTextSplitter(
    separator= "\n",
    chunk_size = 200,
    chunk_overlap = 0  # when you increase this variable to say 200 it create different chunks. chuck2 as part of the end of chunk2 (overlapping)
)
#load the document to split
loader = TextLoader("facts.txt")

#split the loaded document using the text_splitter
docs = loader.load_and_split(
    text_splitter = text_splitter
)

#iterate through each splitter text
for doc in docs:
    print(doc)
    print()
