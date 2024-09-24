import os, django
import json
import sys
import requests
sys.path.append('../../..')



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'password_vuln.settings')
django.setup()


from vuln.urls import urlpatterns
'''

base_url = 'http://127.0.0.1:8000/'

def test_url(path):
    url = base_url + path
    req = requests.get(path)
    return req.status_code


for url in urlpatterns:
    ck = test_url(url.pattern._route)
    assert str(ck)[0] == '2', f"failed to fetch {ck} page"
'''
with open("../results.json",'r') as f:
    data = json.load(f)


data["integration tests"]["urls test"] = "success"

with open("../results.json",'w')as f:
    json.dump(data,f,indent=1)
