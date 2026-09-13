# JSON User Data Fetching Python Program
import json
from jsonFiles import *

# invoking json filepath
fpath = "D:\\repos\\PythonProjects\\fileHandling\\jsonFiles\\users.json"

# parse the file once into a dict
with open(fpath, encoding='UTF-8') as file:
    data = json.load(file)

def fetchCityNames():
    # returns all cities
    for user in data["utilizadores"]:
        print(json.dumps(user["cidade"],
                        indent=2, ensure_ascii=False))

fetchCityNames()