import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('span#price')
    elems[0].text.strip()




price = getAmazonPrice('https://www.amazon.com.br/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The price is ' + price)
