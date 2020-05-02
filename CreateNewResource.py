import requests
import json

url = "https://reqres.in/api/users"

# read input json file
open_file = open("CreateUser.json", "r")
read_the_content = open_file.read()
transform_into_json = json.loads(read_the_content)
print(transform_into_json)

# make POST request with json input body
response = requests.post(url, transform_into_json)
print(response.content)

# parse response to json format
json_response = json.loads(response.text)

# fetch response status code
create_code = response.status_code  # 201
print(create_code)

# fetch header from response
response_header = response.headers
print(response_header.get('Content-Length'))
