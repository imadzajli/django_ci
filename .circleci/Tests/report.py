import json


f = open("../results.json",'r')

report = json.load(f)

print(f"results of tests : {report}")