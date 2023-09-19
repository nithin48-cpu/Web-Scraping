import requests
from bs4 import BeautifulSoup


class PriceTracker():
    def __init__(self, url):
        self.tag2 = None
        self.tag = None
        self.url = url
        self.user_agent = {
            'User_Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        self.response = requests.get(url=self.url, headers=self.user_agent).content
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def name(self):
        self.tag = self.soup.find('span', {'class':"a-size-large product-title-word-break"})
        print(self.tag.text.strip())

    def price(self):
        self.tag2 = self.soup.find('span', {'class': 'a-price-whole'})
        print(self.tag2.text.strip())


device = PriceTracker('https://www.amazon.in/Apple-iPhone-13-128GB-Pink/dp/B09G9FPGTN?ref_=ast_sto_dp&th=1&psc=1')
device.name()
device.price()
