from app import create_app
import requests
import json
import gzip

app = create_app


response = requests.get('https://smn.conagua.gob.mx/webservices/?method=3', verify=False, timeout=60)
print(response.status_code)
headers_json = dict(response.headers)

for k,v in headers_json.items():
    print(k,': ',v)

if response.content == '':
    print('File Empty')

else:
    gzip_fd = gzip.GzipFile(fileobj=response.content)
    gzip_fd = gzip.decompress(response.content)
    parsed = json.loads(gzip_fd)
    with open('forecast.json', 'w') as file:
        json.dump(parsed,file)
        print('Done')
    
