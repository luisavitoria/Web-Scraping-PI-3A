import requests
from bs4 import BeautifulSoup
from mysqlcon import insert_monster

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# Page: Monsters
page = requests.get("https://zezeniabrasil.com/monsters/", headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find(id="myTable")

#imagens
images_tags = table.find_all('img') 
images = []
for img in images_tags:
    images.append(img["src"])

#nomes
names_tags = table.find_all(class_="name")
names = [name.text for name in names_tags]

#dados de vida
lifes_tags = table.select('.text-life:first-child')
lifes = [life.text for life in lifes_tags]

#dados de experiencia
experience_tags = table.select('.text-life:last-child')
experience = [experience.text for experience in experience_tags]

for i in range(len(names)):
    insert_monster(names[i], images[i], lifes[i], experience[i])
    
print("Monstros inseridos no BD.")



