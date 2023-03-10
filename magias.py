import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# Page: Magias
page = requests.get("https://zezeniabrasil.com/magias/?v=mage-pyromance", headers = headers)
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find(class_='tab-content')

support_spells = table.find(id='support')


magic_support_tags = support_spells.select('.item-content div:first-child div:nth-of-type(2) p:nth-of-type(1)')
magic_support = [magic.text for magic in magic_support_tags]
print(magic_support)


value_magic_support_tags = support_spells.select('.item-content div:first-child div:nth-of-type(3) p:nth-of-type(1)')
value_magic_support = [value.text for value in value_magic_support_tags]
print(value_magic_support)