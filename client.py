import requests

url = "http://ableytner.ddns.net:27000/message"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
