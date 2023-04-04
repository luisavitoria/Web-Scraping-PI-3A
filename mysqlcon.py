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

    mycursor.execute("CREATE TABLE monsters (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), image_link VARCHAR(400), life VARCHAR(50), experience VARCHAR(50))")

def insert_monster(name, image_link, life, experience):
    connection
    mycursor = connection.cursor()
    
    sql = "INSERT INTO monsters (name, image_link, life, experience) VALUES (%s, %s, %s, %s)"
    val = (name, image_link, life, experience )
    mycursor.execute(sql, val)

    connection.commit()

    print(mycursor.rowcount, "monster inserted.")


#create_table()