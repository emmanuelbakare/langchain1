from langchain.agents import create_openai_tools_agent, create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from tools import code_writer 
from utilities import get_llm

def generate_model(clean_schema):
    print("GENERATE AND CREATE THE MODELS")
    system_prompt = """You a fullstack Django develop and your goal is to develop a robust django application.
    This will include  the Django model, views, template and urls as indicated by prompt.
    use the code_writer function to generate the respective views.py, models.py, urls.py file etc respectively for each code generated.
    store the generated files under the folder name generated in the root folder.
    - While generating the codes ensure that you put in mind the relationship between the models, forms views and templates.
    - Put in mind that we will be generating function views.
    - I am using Bootstrap for the template files
    - add internal documentation to the code so that it can be easily understood
    
    """
    # - where ever there is need to create a folder you cannot find use the create_folder function to create the folder

    

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
    tools=[code_writer ]

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
    print("Generating the schema models. Please wait..."  )
    #MODEL
    result = executor.invoke({"prompt_message":f"generate the model based on the schema below\n {clean_schema} \n write the code to models.py file"})

    # return prompt_message
    outputs =[]
    outputs.append(return_output(result,llm_type))

    #FORM
    print("Generating the forms. Please wait..." )
    result = executor.invoke({"prompt_message":"""generate the forms for this application and store it in forms.py. 
                              - ensure the fields in the models are captured in the form except the id"""})
    outputs.append(return_output(result,llm_type))



    #VIEWS
    print("Generating the views. Please wait..." )
    result = executor.invoke({"prompt_message":"""based on the model generated, create CRUD  views for each model and write the ouptut in a views.py file. 
                              - Ensure your views reflects the urls as generated in urls.py appropriately. 
                              - Generate functions based views
                              - when specifying template path in render method DO NOT add the folder path name, only add the file name e.g. DO NOT write render(request,'<foldername>/<filename.html>', {})  "<foldername>/" should be EXCLUDED in the render parameter"""})
    outputs.append(return_output(result,llm_type))

    #URLS
    print("Generating the urls. Please wait...", end=" ")
    result = executor.invoke({"prompt_message":"""Generate the urls files based on the views generate  and store it in urls.py. add an app_name in urls. 
                              - Ensure the URL captures all the views function. Generate a function based urls
                              """})
    outputs.append(return_output(result,llm_type))

    #TEMPLATES
    print("Generating the templates. Please wait...", end=" " )

    file_path=""
    try:
        result = executor.invoke({"prompt_message":"""Based on the views generated, generate the templates for each views where necessary in a .html files. 
                                - Generate a base.html file from which the other templates files will extend from. add bootstrap cdn to the base.html file
                                - Create a well styles bootstrap layouts for each template file
                                -Store the .html files in subfolder templates which is under the templates folder.
                                - Ensure the name of the object called inside any template file is same with the object passed to render context in views.py 
                                - if you encounter a FileNotFoundError then store the file path in  variable called file_path
                                """})
    except FileNotFoundError:
        print('FILE OR DIRECTROY NOT FOUND')
        print("PATH: ", file_path)

                            #   - if you encounter a FileNotFoundError then run the create_folder function to create the directory that is missing
    outputs.append("generated all the templates needed for the application")

    #ADMIN
    print("Generating the admin. Please wait..." )
    result = executor.invoke({"prompt_message":"generate the admin configuration file for access to the backend"})
    outputs.append(return_output(result,llm_type))
    outputs.append("="*50)


     #Testing
    print("Carring out Test. Please wait..." )
    result = executor.invoke({"prompt_message":"Carry out test on all the files generated (models.py, urls.py, forms.py, views.py and all the template files). ensure that namings, functions and variables are consistent with each other. rewrite the codes that is not correct and overwrite the wrong one with the code_writer function"})
    outputs.append(return_output(result,llm_type))

    return outputs

    


#code for outputting result in openai or claude are different. this function helps to format the output similarly.
def return_output(result, llm_type):
    if llm_type.lower()=="claude":
        return result['output'][0]['text']
    else:
        return result['output']




