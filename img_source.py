import requests

user=input("Enter the image name : ")

url=f"https://www.bing.com/images/search?q={user}&form=HDRSC3&first=1"

user_agent={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
}

response=requests.get(url=url,headers=user_agent).text
print(response)
