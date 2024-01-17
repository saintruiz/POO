import sqlite3

#Creamos la conexión
con=sqlite3.connect('BBDD1')

#Creamos el cursor
cur=con.cursor()

# cur.execute('CREATE TABLE PRODUCTOS (ARTICLE_NAME VARCHAR(50), PRICE INTEGER, SECTION VARCHAR(20))')


#Cerramos la conexión
con.close()