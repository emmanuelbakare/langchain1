import os

file = """ 
Writing something to file 
"""

def write_to_file(generated_code, filename):
    os.makedirs("generated", exist_ok=True) # make this directory if it does exist
    root_folder=os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(root_folder,"generated",filename)

    with open(folder_path, 'w') as file:
        file.write(generated_code)

