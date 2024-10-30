import sqlite3
from langchain.tools import Tool
from pydantic.v1 import BaseModel

conn = sqlite3.connect("db.sqlite")

def sql_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return  f"The following Error Occurred {str(err)}" 

class RunQueryArgsSchema(BaseModel):
    query: str

run_query_tool = Tool.from_function(
    name= "run_sql_query",
    description = "Run sql query and return result",
    func = sql_query,
    args_schema= RunQueryArgsSchema
)

#==============================================================
#==============================================================

def list_tables():
    c = conn.cursor()
    c.execute("SELECT name from sqlite_master WHERE type='table'")
    results= c.fetchall()
    return ", ".join(name[0] for name in results)

#=============================================================
#=============================================================
 
def get_describe_table(*args, **kwargs):
    cursor = conn.cursor()
    cursor.execute("SELECT name from sqlite_master WHERE type='table'")
    return ", ".join(name[0] for name in cursor.fetchall())

describe_table  = Tool.from_function(
    name = "describe_table",
    description="Describe the table schema",
    func= get_describe_table
)
#=============================================================
#=============================================================

def get_db_schema(*args, **kwargs):
    # Connect to the SQLite database
    cursor = conn.cursor()
    
    # Get the list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Dictionary to hold schema information
    schema = {}

    # Loop through all the tables and get their column information
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        # Extract the column names
        column_names = tuple(column[1] for column in columns)
        
        # Add the table and its columns to the schema dictionary
        schema[table_name] = column_names

    # Close the connection
    # conn.close()

    return schema

full_db_schema = Tool.from_function(
    name= "full_db_schema",
    description="get full database Schema",
    func=get_db_schema
)
