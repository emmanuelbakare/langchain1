import os
from langchain.tools import Tool 
import sqlite3
# path = os.path.join(os.getcwd(),    "agentapp","db.sqlite")
path = os.path.join(os.path.dirname(__file__),'db.sqlite')
conn = sqlite3.connect(path)

def run_sql_query(query):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()

run_query_tool = Tool.from_function(
    name="run_sql_query",
    description="Run an SQLite Query",
    func = run_sql_query
)

 
 