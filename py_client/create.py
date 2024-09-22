import requests

endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.post(endpoint, json={'title':'Generic Title', 'content':'Generic Content', 'price':'92.22'})
print(get_response.json())