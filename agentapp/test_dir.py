import os
import sqlite3 
path = os.path.join(os.path.dirname(__file__),'db.sqlite')
print(path)

conn = sqlite3.connect(path)

def get_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

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

def describe_tables(table_names):
    cursor= conn.cursor()
    tables = ", ".join(f"'table'" for table in table_names)
    query = f"SELECT sql from sqlite_master WHERE type='table' AND name IN ({tables});"
    rows =cursor.execute(query)
    return ", ".join( row[0] for row in rows if row[0] is not None)

   
# query = "SELECT name || '(' || group_concat(sql, ', ') || ')' AS table_with_fields FROM ( SELECT m.name, "
# query += " p.name || ' ' || p.'type' AS sql FROM sqlite_master m JOIN pragma_table_info(m.name) p WHERE "
# query += " m.type = 'table') GROUP BY name;"






# result = get_query(query)
# result2  = ", ".join(f"{table }: {[row for row in table]}" for table in result)
# print(result)
# result = get_query("SELECT name FROM sqlite_master WHERE type='table';")
# result_descr = ", ".join(table[0] for table in result if table[0] is not None)
# print(result_descr)


recordset = get_query(query)
result ="\n".join(table[0] for table in recordset)
print(result)
# for row in recordset:
#     print(row[0])

