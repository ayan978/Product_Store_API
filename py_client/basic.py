import requests

endpoint = "https://httpbin.org/anything"


#get_response = requests.post(endpoint, json={'title':'MyTitle', 'content':'This is a content', 'price':30.25})
get_response = requests.get(endpoint)
print(get_response.text)
print(get_response.json())
print(get_response.status_code)