from  langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename, html):
    with open(filename, 'w') as file:
        file.write(html)

class ReportBaseArgs(BaseModel):
    filename:str 
    html:str 

report_tool = StructuredTool.from_function(
    name = "write_report",
    description="Write an HTML file to disk. Use this tool whenever there is a request for a report",
    func= write_report,
    args_schema= ReportBaseArgs
)