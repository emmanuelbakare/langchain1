from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from dotenv import load_dotenv


load_dotenv()
# Get the task and the Language
task = input("Enter the Programming Task: ")
language= input("Which Language do you want it: ")

llm = OpenAI()

template = PromptTemplate(
    template = "Write a short {language} function that will {task}",
    input_variables=["language", "task"]
)


chain = LLMChain(
    llm=llm,
    prompt=template
)


result = chain({
    "language": language,
    "task": task
})
print(result["text"])