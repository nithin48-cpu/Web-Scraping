import csv

import requests
from bs4 import BeautifulSoup


def extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    # tag=soup.div      ## here it return all the div in web
    tag = soup.find('div', {'id': 'mp-right'})  # here it will filter dive according to parameters
    h = tag.find_all("h2")  # again finding the p in tag
    content = [span.text for span in h]

    with open('wiki.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(content)


extract("https://en.wikipedia.org/wiki/Main_Page")
