import requests
from bs4 import BeautifulSoup
import re
from mysqlcon import insert_magic, insert_items
import string

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

def getNames(table):
    names_tags = table.select('.name')
    names = [name.text for name in names_tags]
    return names

def getArmAtaque(table):
    arms_tags = table.select('tr td:nth-of-type(3) span:nth-of-type(1) ')
    arms = [arm.text for arm in arms_tags]
    return arms

def getArmDefesa(table):
    arms_tags = table.select('tr td:nth-of-type(3) span:nth-of-type(2) ')
    arms = [arm.text for arm in arms_tags]
    return arms

def getVocacao(table):
    vocacao_tags = table.select('tr td:nth-of-type(4) p')
    vocacao_list = [vocacao.get_text(strip=True, separator='\n').splitlines() for vocacao in vocacao_tags]
    vocacao = []
    for item in vocacao_list:
        vocacao.append(", ".join(item))
    return vocacao


def insertItem(url, item_name):
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find(id='myTable')
    names = getNames(table)
    ataques = getArmAtaque(table)
    defesas = getArmDefesa(table)
    vocacoes = getVocacao(table)
    
    if(len(ataques) == 0):
        ataques = [None] * len(names)
    
    if(len(defesas) == 0):
        defesas = [None] * len(names)
        
    if(len(vocacoes) == 0):
        vocacoes = [None] * len(names)
    
    for i in range(len(names)):
        insert_items(item_name, names[i], ataques[i], defesas[i], vocacoes[i])
    
    print("Itens inseridos no BD.")
        
    
insertItem("https://zezeniabrasil.com/itens/amuletos/", 'amuleto')
insertItem("https://zezeniabrasil.com/itens/aneis/", "aneis")
insertItem("https://zezeniabrasil.com/itens/armors/", "armaduras")
insertItem("https://zezeniabrasil.com/itens/armas-corpo-a-corpo/", "armas corpo a corpo")
insertItem("https://zezeniabrasil.com/itens/armas-de-longo-alcance/", "armas de longo alcance")
insertItem("https://zezeniabrasil.com/itens/botas/", "botas")
insertItem("https://zezeniabrasil.com/itens/braceletes/", "braceletes")
insertItem("https://zezeniabrasil.com/itens/calcas/", "calcas")
insertItem("https://zezeniabrasil.com/itens/comidas/", "comidas")
insertItem("https://zezeniabrasil.com/itens/helmets/", "elmos")
insertItem("https://zezeniabrasil.com/itens/equipamentos-de-pesca/", "equipamentos de pesca")
insertItem("https://zezeniabrasil.com/itens/escudos/", "escudos")
insertItem("https://zezeniabrasil.com/itens/gathering/", 'gathering')
insertItem("https://zezeniabrasil.com/itens/itens-de-creaturas/", "itens de criaturas")
insertItem("https://zezeniabrasil.com/itens/luvas/", "luvas")
insertItem("https://zezeniabrasil.com/itens/municoes/", "munições")
insertItem("https://zezeniabrasil.com/itens/pocoes-magicas/", "poções mágicas")
insertItem("https://zezeniabrasil.com/itens/quivers/", "quivers")
insertItem("https://zezeniabrasil.com/itens/receitas/", "receitas")
insertItem("https://zezeniabrasil.com/itens/spellbooks/", "spellbooks")
insertItem("https://zezeniabrasil.com/itens/wands/", "wands")


