import os
from langchain.tools import Tool 
import sqlite3
# path = os.path.join(os.getcwd(),    "agentapp","db.sqlite")
path = os.path.join(os.path.dirname(__file__),'db.sqlite')
conn = sqlite3.connect(path)


#------ RUN Quer for Table And Field-----
def get_table_and_fields():
    query =""" 
        SELECT
                m.name || ':' || group_concat(p.name, ', ')
            FROM
                sqlite_master m
                JOIN pragma_table_info(m.name) p
            WHERE
                m.type = 'table'
            GROUP BY
                m.name;
            """
    cursor = conn.cursor()
    cursor.execute(query)
    recordset= cursor.fetchall()
    return "\n".join(table[0] for table in recordset if table[0] is not None)



    
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

run_query_tool = Tool.from_function(
    name="run_sql_query",
    description="Run an SQLite Query",
    func = run_sql_query
)

#---------- TABLE FIELDS DESCRIPTIONS-----------

def describe_tables(table_names):
    cursor= conn.cursor()
    tables = ", ".join("'"+table+"'" for table in table_names)
    # print("---TABLES ARE---: ", tables)
    query = f"SELECT sql from sqlite_master WHERE type='table' AND name IN ({tables});"
    # print("QUERY: ", query)
    # rows =cursor.execute(query)
    # print(rows)
    # return ", ".join( row[0] for row in rows if row[0] is not None)
    return query


describe_table_tool = Tool(
    name="describe_tables",
    description="Given a list of table names, return the List of Table fields",
    func = describe_tables
)


# tList = ", ".join(table[0] for table in list_tables())
# rows = get_table_and_fields()
# print(rows)
 