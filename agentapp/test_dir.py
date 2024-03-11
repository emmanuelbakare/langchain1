import os
import sqlite3 
path = os.path.join(os.path.dirname(__file__),'db.sqlite')
print(path)

conn = sqlite3.connect(path)

def get_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


query = "SELECT name || '(' || group_concat(sql, ', ') || ')' AS table_with_fields FROM ( SELECT m.name, "
query += " p.name || ' ' || p.'type' AS sql FROM sqlite_master m JOIN pragma_table_info(m.name) p WHERE "
query += " m.type = 'table') GROUP BY name;"

result = get_query(query)
print(result)

