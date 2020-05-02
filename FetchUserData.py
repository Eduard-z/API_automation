import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response)  # <Response [200]>

# parse response to json format
json_response = json.loads(response.text)

# fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')  # returns a list
print(pages[0])
