from langchain.agents import create_openai_tools_agent, create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from tool1 import code_writer 
from utilities import get_llm

def generate_model(clean_schema):
    print("GENERATE AND CREATE THE MODELS")
    system_prompt = """You a fullstack Django develop and your goal is to develop a robust django application.
    This will include  the Django model, views, template and urls as indicated by prompt.
    use the code_writer function to generate the respective views.py, models.py, urls.py file etcrespectively for each code generated.
    store the generated files under the folder name generated in the root folder"""
    

    

    memory= ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    user_prompt = ChatPromptTemplate(
        input_variables = ["prompt_message","chat_history"],
        messages= [
            SystemMessagePromptTemplate.from_template(system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{prompt_message}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ]

    )
    
    llm_type= "openai"
    llm = get_llm(llm_type) 
    # return clean_schema
    tools=[code_writer]

    # agent = create_openai_tools_agent(  # sutable for open ao
    agent = create_tool_calling_agent(
        prompt = user_prompt,
        llm = llm,
        tools = tools
    )

    executor = AgentExecutor(
        agent = agent,
        tools= tools,
        memory= memory,
        verbose = False,
        
    )
    print("Generating the schema models. Please wait...")
    result = executor.invoke({"prompt_message":f"generate the model based on the schema below\n {clean_schema} \n write the code to models.py file"})

    # return prompt_message
    outputs =[]
    outputs.append(return_output(result,llm_type))

    print("Generating the views. Please wait...")
    result = executor.invoke({"prompt_message":"based on the model generated create the view for each model and writ the ouptut in a views.py file"})
    outputs.append(return_output(result,llm_type))


    print("Generating the urls. Please wait...")
    result = executor.invoke({"prompt_message":"generate the urls files and store it in urls.py"})
    outputs.append(return_output(result,llm_type))

    print("Generating the forms. Please wait...")
    result = executor.invoke({"prompt_message":"generate the forms for this application and store it in forms.py"})
    outputs.append(return_output(result,llm_type))

 


    return outputs

    



def return_output(result, llm_type):
    if llm_type.lower()=="claude":
        return result['output'][0]['text']
    else:
        return result['output']




