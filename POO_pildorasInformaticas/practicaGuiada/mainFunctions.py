import sqlite3
from user import *
def Conect_():
    try:
        con=sqlite3.connect("main.bd")
        cur=con.cursor()
        cur.execute("""CREATE TABLE main(
                    ID VARCHAR(5) PRIMARY KEY,
                    name VARCHAR(50),
                    lastName VARCHAR(50),
                    pswd VARCHAR(50),
                    addr VARCHAR(100)
                     )""")
        con.commit()
        con.close()

        return 'La base de datos ha sido creada'

    except sqlite3.Error as e:

        result=(f"Error al conectar la base de datos: {e}")

        return result
    
    
    
def CreateInB(Id:str, name:str, lastName:str, pswd:str, addr:str):
    User_=user(Id, name, lastName, pswd, addr)
    return User_.Create_()

def Read_(id:str) -> list:
    query=(f"SELECT * FROM main WHERE ID={id}")
    con=sqlite3.connect('main.bd')
    cur=con.cursor()
    data=cur.execute(query)
    con.commit()
    con.close()

    return data