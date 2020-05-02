import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# read input json file
open_file = open("CreateUser.json", "r")
read_the_content = open_file.read()
transform_into_json = json.loads(read_the_content)
print(transform_into_json)

# make PUT request with json input body
response = requests.put(url, transform_into_json)
print(response.content)

# fetch response status code
update_code = response.status_code  # 200
print(update_code)

# parse response to json format
json_response = json.loads(response.text)

# fetch value using json path
updated_resource = jsonpath.jsonpath(json_response, 'updatedAt')
print(updated_resource[0])
