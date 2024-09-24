import os, django
import json
import sys

sys.path.append('../../..')



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'password_vuln.settings')
django.setup()

from vuln.models import *
import json

class TestDB:
    def __init__(self,tablename):
        self.table = tablename

    def insert_test(self,values):
        
        try:
            row_created = self.table.objects.create(
                id = 99999,
                fname = values["fname"],
                lname = values["lname"],
                username = values["username"],
                password = values["password"],
                amount = values["amount"]
            )
            ck = 200
        except Exception as e:
            ck = e
        return ck
    
    def get_test(self,id):
        try:
            obj = self.table.objects.get(id=id)
            ck = 200
        except Exception as e:
            ck = e
        return ck
    def delete_test(self,id):
        try:
            obj = self.table.objects.delete(id=id)
            ck = 200
        except Exception as e:
            ck = e
        return ck


test_db = TestDB(user)
with open("../results.json",'r') as f:
    data = json.load(f)



# insert

ck = test_db.insert_test({"fname":"imad","lname":"xt","username":"hello","password":"hi","amount":9999})

assert ck == 200, f"error inserting in database : {ck}"
# get

ck = test_db.get_test(99999)

assert ck == 200, f"error geting from database : {ck}"

# del 

ck = test_db.delete_test(99999)

assert ck == 200, f"error deleting from database : {ck}"

data["integration tests"]["database test"] = "success"

with open("../results.json",'w')as f:
    json.dump(data,f,indent=1)
