import requests
from bs4 import BeautifulSoup


def extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    # tag=soup.div      ## here it return all the div in web
    tag = soup.find('div', {'id': 'mp-right'})    # here it will filter dive according to parameters
    h=tag.find_all("h2")    # again finding the p in tag
    print([span.text for span in h])


extract("https://en.wikipedia.org/wiki/Main_Page")







