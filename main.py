from venv import create
from app import create_app
import requests


app = create_app


r = requests.get('https://smn.conagua.gob.mx/webservices/?method=1', verify=False)
print(r.status_code)
print(r.json())