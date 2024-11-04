import re

def format_response(message, tag):
    match = re.search(rf'\[{tag}\](.*?)\[/{tag}\]', message.content, re.DOTALL)

    if match:
        return  match.group(1).strip()  # Get the text and remove any leading/trailing whitespace


    else:
        return "No schema found"
