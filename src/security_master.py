import json
import pandas as pd

with open('/Users/talhajamal/Desktop/Code/Daily Market Update /data/yhallsym.txt', 'r') as file:
    json_data = file.read()

json_string = json_data.replace("'", '"')

json_dict = json.loads(json_string)

print(json_dict)