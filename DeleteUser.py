import requests

url = "https://reqres.in/api/users/2"
response = requests.delete(url)

# fetch response status code
delete_code = response.status_code  # 204
print(delete_code)
