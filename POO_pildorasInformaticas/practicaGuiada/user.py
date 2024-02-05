import sqlite3

class user():
    def __init__(self, id:str, name:str, lastName:str, pswd:str, addr:str):
        self.__id=id
        self.__name=name
        self.__lastName=lastName
        self.__pswd=pswd
        self.__addr=addr

    def Create_(self):
        data=[self.__id, self.__name, self.__lastName, self.__pswd, self.__addr]

        try:
            con=sqlite3.connect('main.bd')
            cur=con.cursor()
            cur.execute('INSERT INTO main VALUES(?,?,?,?,?)', data)
            con.commit()
            con.close()
            return 'El usuario ha sido creado en la base de datos'
        
        except sqlite3.Error as e:
            result=(f'Error al crear usuario: {e}')
            return result
        