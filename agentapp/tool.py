from langchain.tools import Tool 
import sqlite3

conn = sqlite3.connect("db.sqlite")

def run_sql_query(query):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()

run_query_tool = Tool.from_function(
    name="run_sql_query",
    description="Run an SQLite Query",
    func = run_sql_query
)