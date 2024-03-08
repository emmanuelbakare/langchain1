# using ConversationBufferMemory can get very bulky as each new prompt is added to the old to keep a conversation going.
# to reduce the size of the Conversation buffer, you can use ConversationSummaryMemory instead of ConversationBufferMemory 
# to ask langchain to summarize the content of the buffer memory so that the conversation prompt is smaller.
# the downside is that after generating your output, the ConversationSummaryMemory also passes the output into another LLM
# to generate the summary of the conversation. I.e. the conversation goes through 2 llms, one generate the output and another
# summarize the conversation prompt and this makes the final output slower.

from  langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationSummaryMemory



from dotenv import load_dotenv
load_dotenv()

chat= ChatOpenAI()
prompt= ChatPromptTemplate(
    input_variables=["content","messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)
memory=ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm = chat
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose= True
)

while True:
    content = input(">> ")
    result = chain({"content":content})
    print(result["text"])