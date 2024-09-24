import json
file = open("quality.txt","r")

result_test = file.readlines()

fun = lambda x : x.split(' ')[1]

newresult_test = list(map(fun,result_test))

set_of_results = set(result_test)

errors = {}

for i in set_of_results:
    errors.update({i:result_test.count(i)})

with open("../results.json",'r') as f:
    data = json.load(f)

data["quality test"] = json.dumps(errors)

with open("../results.json",'w')as f:
    json.dump(data,f,indent=1)



print(errors)


doc = "https://flake8.pycqa.org/en/latest/user/error-codes.html"
print(f"check for error codes here : {doc}")