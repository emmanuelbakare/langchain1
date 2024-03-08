from langchain.llms import OpenAI 
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

#input values
task = input("Proramming Task: ")
language = input("Programming Language: ")

#create LLM
llm = OpenAI() 
#============================= PROMPT TEMPLATE========================
code_prompt = PromptTemplate(
    template="write a program in {language} for {task}",
    input_variables=["language", "task"]
)

test_prompt = PromptTemplate(
    template="write a test for {code}",
    input_variables=["code"],
    

)
#===========================LLM CHAIN ===========================
code_chain= LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
    
)

test_chain = LLMChain(
    llm = llm,
    prompt=test_prompt,
    output_key="test"

)

#================= SEQUENCE CHAIN==================

chain_sequence = SequentialChain(
    chains = [code_chain, test_chain],
    input_variables=["task","language"],
    output_variables=["code", "test"]
)
result = chain_sequence({
    "language":language,
    "task":task
})

print("==========CODE================")
print(result["code"])
print()

print("==========TEST================")
print(result["test"])




