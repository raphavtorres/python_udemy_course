JSON is a Data Structure
JavaScript Object Notation

"file_name.json"

data types: true; 123.12; null; "string", [array], {object --> something with more than a value}


# Example with python
import json
import os

# create complete file path name
BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'file-python.json')  # --> path + file name

with open(SAVE_TO, 'w') as file:
    json.dump()  # (dump to a file)
    # json.dumps (dump in string)
