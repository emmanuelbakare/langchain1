from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ( HumanMessagePromptTemplate, 
                                    MessagesPlaceholder, 
                                    ChatMessagePromptTemplate)
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="")