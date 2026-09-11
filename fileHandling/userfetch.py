# JSON User Data Fetching Python Program
import json
from jsonFiles import *

# invoking json filepath
fpath = "D:\\repos\\PythonProjects\\fileHandling\\jsonFiles\\users.json"

# use json dumps to print json contents
with open(fpath, encoding='UTF-8') as file:
    def fetchUserData():
        data = file.read()
        print(json.dumps(data))

    fetchUserData()

file.close()