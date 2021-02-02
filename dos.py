import requests


for i in range(100):
    response = requests.get('https://c00l.xyz')
    print(response.status_code)
