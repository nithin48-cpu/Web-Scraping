import requests
from bs4 import BeautifulSoup


class Tracker:
    def __init__(self, url):
        self.url = url
        self.user_agent = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.response = requests.get(url=self.url, headers=self.user_agent).content
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def name(self):
        tag = self.soup.find('span', {'class': 'B_NuCI'})
        print(tag.text)

    def price(self):
        tag = self.soup.find('div', {'class': '_30jeq3 _16Jk6d'})
        print(tag.text)


device = Tracker(
    "http://dl.flipkart.com/dl/oppo-enco-buds-2-28-hours-battery-life-deep-noise-cancellation-bluetooth-headset/p/itm3344fa26518ed?pid=ACCGH7YZY6AHGCHJ&cmpid=product.share.pp&lid=LSTACCGH7YZY6AHGCHJHLWF41"
)
device.name()
device.price()
