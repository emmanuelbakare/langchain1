from langchain.document_loaders import TextLoader 

from dotenv import load_dotenv
load_dotenv("../.env")

#load the document using TextLoader and send the output to txt
loader = TextLoader("facts.txt")
txt=loader.load()

print(txt)