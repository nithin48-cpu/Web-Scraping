import requests

url = "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&w=600"

response = requests.get(url=url)

pic = response.content

f = open("image.png", 'wb')

f.write(pic)
