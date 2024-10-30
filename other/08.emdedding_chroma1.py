from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size = 200,
    chunk_overlap = 0
)

loader = TextLoader("facts.txt")

docs = loader.load_and_split(
    text_splitter=splitter
)

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(
    docs,
    embedding = embeddings,
    persist_directory ="emb"
)

results = db.similarity_search(
    "what is an interesting fact about the English language",
    k=1
    )

for result in results:
    print(result.page_content)
    print('*'*70)

