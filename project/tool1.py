from langchain.tools import Tool, StructuredTool
from pydantic.v1 import BaseModel



def write_to_file(generated_code, filename):
    with open(filename, 'w') as file:
        file.write(generated_code)
    
class WriteCodeArgs(BaseModel):
    generated_code:str
    filename: str

code_writer = StructuredTool.from_function(
    name = "code_writer",
    description="write  program to file.",
    func = write_to_file,
    args_schema = WriteCodeArgs
)