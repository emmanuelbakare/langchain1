import os
from langchain.tools import Tool 
from pydantic.v1 import BaseModel
from typing import List

import sqlite3
# path = os.path.join(os.getcwd(),    "agentapp","db.sqlite")
path = os.path.join(os.path.dirname(__file__),'db.sqlite')
conn = sqlite3.connect(path)




    
# ------ list of tables --------
def list_tables():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = cursor.fetchall()
    return result

#------ Run Table Query------------



def run_sql_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following Error Occurred. {str(err)}"

class RunQueryArgsSchema(BaseModel):
    query:str

run_query_tool = Tool.from_function(
    name="run_sql_query",
    description="Run an SQLite Query",
    func = run_sql_query,
    args_schema=RunQueryArgsSchema
)

#---------- TABLE DESCRIPTIONS-----------

def describe_tables(table_names):
    cursor= conn.cursor()
    tables = ", ".join(f"'table'" for table in table_names)
    query = f"SELECT sql from sqlite_master WHERE type='table' AND name IN ({tables});"
    rows =cursor.execute(query)
    return ", ".join( row[0] for row in rows if row[0] is not None)
    # return query

class DescribTableArgsSchema(BaseModel):
    table_names:List[str]

describe_table_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, return the schema of those tables",
    func = describe_tables
)


tList = ", ".join(table[0] for table in list_tables())
rows = describe_tables(tList)
# print(tList)
# print("---Rows---\n",rows)
print(rows)
 