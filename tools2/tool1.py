from langchain.tools import Tool
from pydantic.v1 import BaseModel



def write_to_file(generated_code, filename="generated_code.py"):
    with open(filename, 'w') as file:
        file.write(generated_code)
    
class WriteCodeArgs(BaseModel):
    code:str
    # filename: str

code_writer = Tool.from_function(
    name = "code_writer",
    description="write program code to file. add comments of other instructions in the file",
    func = write_to_file,
    args_schema = WriteCodeArgs
)