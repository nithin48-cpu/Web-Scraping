import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.amazon.in/s?k=iphone&crid=27X1034WM97OC&sprefix=%2Caps%2C554&ref=nb_sb_ss_recent_1_0_recent")
soup = BeautifulSoup(response.content, 'html.parser')
tag = soup.find('span', {'class': "a-size-medium a-color-base a-text-normal"})
print(soup)
 # here we get error because we cant access amazon because its thinging we are accessing in illegal way
 # another way is to access  is use selenium driver
