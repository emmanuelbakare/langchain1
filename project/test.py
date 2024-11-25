from code_generator import chat
input_text = input("Enter the application you want to implement: ")
prompt =f"""
suggest the name of the  application I want to develop from the Statement below

Statement:
{input_text}

- no space in the suggested name. Seperate it with an underscore if more than one word
- if there is know abbreviation for the application- suggest only the abbreviation as the name of the application
- only output the suggested app name. do not add a prefix or suffix description to your response
"""
 
result = chat(text=prompt)

print(result)