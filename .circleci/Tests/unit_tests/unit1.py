from vuln.models import *
import json



all_users = user.objects,all()

predifined_amount = 2000

circuled_amount = 0

for i in all_users:
    circuled_amount += i.amount

with open("../results.json","r") as f:
    data = json.load(f)



assert predifined_amount == circuled_amount, f"failed amount test predifined = {predifined_amount} circuled = {circuled_amount}"

data["unit tests"] = "success"

with open("../results.json","w") as f:
    json.dump(data,f,indent=1)

print("amount test passed sucessfully")