import sqlite3

conn = sqlite3.connect("db.sqlite")

def sql_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return  f"The following Error Occurred {str(err)}" 


def describe_table():
    cursor = conn.cursor()
    cursor.execute("SELECT name from sqlite_master WHERE type='table'")
    return ", ".join(name[0] for name in cursor.fetchall())


result = describe_table()
print(result)


# result= sql_query("Select count(*) from USERS")
# result= sql_query("SELECT name FROM sqlite_master WHERE type = 'table'")
# print(", ".join(name[0] for name in result ))

 
