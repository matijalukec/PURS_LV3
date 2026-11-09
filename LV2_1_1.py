import requests

response = requests.get("http://127.0.0.1:80/")

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)