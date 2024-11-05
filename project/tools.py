from langchain.tools import Tool, StructuredTool
from pydantic.v1 import BaseModel
import os


def write_to_file(generated_code, filename):
    with open(filename, 'w') as file:
        file.write(generated_code)
    print(f"{filename} created ")
    
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
#     foldername: str

# def create_folder(foldername:str):
#     os.makedirs(foldername,exist_ok=True)
#     print(f"{foldername} created ")

# make_folder = Tool.from_function(
#     name = "make_folder",
#     description="check if a folder exist and if not create it",
#     func = create_folder,
#     args_schema=CreateFolderArgs
# )