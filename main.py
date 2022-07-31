from venv import create
from app import create_app
import requests
import json


app = create_app


r = requests.get('https://smn.conagua.gob.mx/webservices/?method=1')
print(r.status_code)
print(r.headers)
# print(r.json())
# with open('new_file.json', 'w') as f:
#     json.dump(r.json(), f, indent=2)