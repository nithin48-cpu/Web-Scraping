import requests

url = "https://www.codechef.com/learn?itm_medium=navmenu&itm_campaign=learn"

params = {
    'itm_medium': 'navmenu',
    'itm_campaign': 'learn'
}

response = requests.get(url=url, params=params)  #it returns data if website can post data and shows stored data

print(response.content)


#params means parameters