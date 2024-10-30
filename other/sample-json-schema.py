message = [
    {
        "role":"user",
        "content":"How many orders are there?"
    }
]

functions = [
    {
        "name":"sql_query",
        "description": "Run an sql query. Return the result",
        "parameters":{
            "type": "object",
            "properties":{
                "query":{
                    "type":"string",
                    "description":"the sql query to execute"
                }
            }
        }
    }
]