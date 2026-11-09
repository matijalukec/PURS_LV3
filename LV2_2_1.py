import requests

response = requests.post("http://127.0.0.1:80/login", data={"username": "PURS", "password": "1234"})

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)