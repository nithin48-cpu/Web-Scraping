import requests

url="https://www.w3schools.com/tags/tag_img.asp"

response=requests.get(url="https://www.w3schools.com/tags/tag_img.asp")

print(response.headers)
print(response.status_code)
print(response.content)