import re
def generate_model(code):
    pass
    


def format_output(code):
    match = re.search(r'\[schema\](.*?)\[/schema\]', code.content, re.DOTALL)

    if match:
        schema_text = match.group(1).strip()  # Get the text and remove any leading/trailing whitespace
        # print("Extracted Schema:\n", schema_text)

    else:
        print("No schema found.")
        print(code.content) 
