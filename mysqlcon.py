import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sqlpassword',
    database='pi_3a',
)

def create_table():
    connection
    mycursor = connection.cursor()

    mycursor.execute("CREATE TABLE monsters (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), image_link VARCHAR(400), life VARCHAR(50), experience VARCHAR(50), UNIQUE (id))")
    mycursor.execute("CREATE TABLE magic (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), spell_type VARCHAR(50), spell_name VARCHAR(50), value INT, level INT, UNIQUE (name))")
    mycursor.execute("CREATE TABLE items (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(50), name VARCHAR(50), ataque VARCHAR(50), defesa VARCHAR(50), vocacao VARCHAR(200), UNIQUE (id))")

def insert_monster(name, image_link, life, experience):
    connection
    mycursor = connection.cursor()
    
    sql = "INSERT INTO monsters (name, image_link, life, experience) VALUES (%s, %s, %s, %s)"
    val = (name, image_link, life, experience )
    mycursor.execute(sql, val)

    connection.commit()

    
def insert_magic(name, spell_type, spell_name, value, level):
    connection
    mycursor = connection.cursor()
    
    sql = "INSERT INTO magic (name, spell_type, spell_name, value, level) VALUES (%s, %s, %s, %s, %s)"
    val = (name, spell_type, spell_name, value, level)
    mycursor.execute(sql, val)

    connection.commit()

    
def insert_items(item, name, ataque, defesa, vocacao):
    connection
    mycursor = connection.cursor()
    
    sql = "INSERT INTO items (item, name, ataque, defesa, vocacao) VALUES (%s, %s, %s, %s, %s)"
    val = (item, name, ataque, defesa, vocacao)
    mycursor.execute(sql, val)

    connection.commit()

create_table()