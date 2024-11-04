from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
import os
import base64
from dotenv import load_dotenv

load_dotenv()

def get_image_string(image_path):
    with open(image_path,'rb') as img_file:
        base64_str = base64.b64encode(img_file.read()).decode("utf-8")
    return base64_str

# prompt = PromptTemplate(
#     input_variables=["image_data"],
#     template = "Describe this image {image_data}"
# )

# llm = ChatOpenAI(model="gpt-4o-mini")
# claude_key = os.getenv("CLAUDE_API_KEY")
# llm = ChatAnthropic(
#     api_key=claude_key,
#     model_name="claude-3-5-sonnet-20240620"
# )
# chat = prompt | llm 

#get the image and covert it base64 string
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir,"images","image01.jpg")
image_data = get_image_string(image_path)

# result = chat.invoke({"image_data":image_data})
# print(result.content)
print(len(image_data))
