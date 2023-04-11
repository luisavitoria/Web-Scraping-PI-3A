import requests
from bs4 import BeautifulSoup
import re
from mysqlcon import insert_magic

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

def getMagics(spell_type, table):
    spells = table.find(id=spell_type)
    magic_tags = spells.select('.item-content div:first-child div:nth-of-type(2) p:nth-of-type(1)')
    magic = [magic.text for magic in magic_tags]
    return magic

def getMagicsValues(spell_type, table):
    spells = table.find(id=spell_type)
    value_tags = spells.select('.item-content div:first-child div:nth-of-type(3) p:nth-of-type(1)')
    value = [int(re.findall("\d+", value.text)[0]) for value in value_tags]
    return value

def getMagicsLevels(spell_type, table):
    spells = table.find(id=spell_type)
    level_tags = spells.select('.item-content div:first-child div:nth-of-type(3) p:nth-of-type(2)')
    level = [int(re.findall("\d+", level.text)[0]) for level in level_tags]
    return level

def insertSupportSpells(magic_name, table):
    spell_type = "support"
    magics = getMagics(spell_type, table)
    values = getMagicsValues(spell_type, table)
    levels = getMagicsLevels(spell_type, table)

    for i in range(len(magics)):
        insert_magic(magic_name, spell_type, magics[i], values[i], levels[i])
        
def insertOffensiveSpells(magic_name, table):
    spell_type = "offensive"
    magics = getMagics(spell_type, table)
    values = getMagicsValues(spell_type, table)
    levels = getMagicsLevels(spell_type, table)

    for i in range(len(magics)):
        insert_magic(magic_name, spell_type, magics[i], values[i], levels[i])
        
def insertMagic(url, magic_name):
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find(class_='tab-content')
    insertSupportSpells(magic_name, table)
    insertOffensiveSpells(magic_name, table)
    
    print("Magias inseridas no BD.")
    
    
#Page: Magias - Pyromance
insertMagic("https://zezeniabrasil.com/magias/?v=mage-pyromance", "mage-pyromance")

#Page: Magias - Shaman
insertMagic("https://zezeniabrasil.com/magias/?v=mage-shaman", "mage-shaman")

#Page: Magias - Warlock
insertMagic("https://zezeniabrasil.com/magias/?v=mage-warlock", "mage-warlock")

#Page: Magias - Maskman
insertMagic("https://zezeniabrasil.com/magias/?v=ranger-maskman", "ranger-maskman")

#Page: Magias - Rogue
insertMagic("https://zezeniabrasil.com/magias/?v=ranger-rogue", "ranger-rogue")

#Page: Magias - warrior-barbarian
insertMagic("https://zezeniabrasil.com/magias/?v=warrior-barbarian", "warrior-barbarian")

#Page: Magias - warrior-Paladin
insertMagic("https://zezeniabrasil.com/magias/?warrior-Paladin", "warrior-Paladin")

