from langchain.tools import  StructuredTool, Tool
from pydantic.v1 import BaseModel
import os


def write_to_file(generated_code, filename):
    with open(filename, 'w') as file:
        file.write(generated_code)
    print(f"created ")
    
class WriteCodeArgs(BaseModel):
    generated_code:str
    filename: str

code_writer = StructuredTool.from_function(
    name = "code_writer",
    description="write  program to file.",
    func = write_to_file,
    args_schema = WriteCodeArgs
)








# class CreateFolderArgs(BaseModel):
#     folder_path: str

# def create_folder(folder_path: str):
#     os.makedirs(folder_path, exist_ok=True)
#     print("Create path ", folder_path)


# make_folder = Tool.from_function(
#     name="make_folder",
#     description="Check if a folder exists, and if not, create it.",
#     func=create_folder,
#     args_schema=CreateFolderArgs
# )



 