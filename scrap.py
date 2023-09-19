import urllib.request,urllib.parse,urllib.error

url=urllib.request.urlopen("https://www.amazon.in/Apple-iPhone-13-128GB-Pink/dp/B09G9FPGTN?ref_=ast_sto_dp&th=1&psc=1")

for line in url:
    print(line.decode().strip())