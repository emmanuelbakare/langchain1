def get_db_schema(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
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
    conn.close()

    return schema