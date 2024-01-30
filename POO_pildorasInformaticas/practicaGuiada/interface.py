from tkinter import *

root=Tk()
root.title('CRUD')
root.config(width=500, height=500)


#Espacio para fila superior-------------------------------

barMenu=Menu()

##Espacio para botón BBDD
def Conect_():
    print('Conectando a la base de datos')
    pass
def Exit_():
    root.destroy()

menuBBDD=Menu(barMenu, tearoff=False)
barMenu.add_cascade(menu=menuBBDD, label='BBDD')

menuBBDD.add_command(
    label='Conect',
    command=Conect_
)
menuBBDD.add_command(
    label='Exit',
    command=Exit_
)

##Espacio para botón Borrar
def Clean_():
    pass

barMenu.add_command(label='Borrar', command=Clean_)

##Espacio para boton CRUD
def Create_():
    pass
def Read_():
    pass
def Update_():
    pass
def Delete_():
    pass


menuCRUD=Menu(barMenu, tearoff=False)
barMenu.add_cascade(menu=menuCRUD, label='CRUD')

menuCRUD.add_command(
    label='Create',
    command=Create_
)
menuCRUD.add_command(
    label='Read',
    command=Read_
)
menuCRUD.add_command(
    label='Update',
    command=Update_
)
menuCRUD.add_command(
    label='Delete',
    command=Delete_
)

##Espacio para botón Ayuda

def Ayuda_():
    pass
barMenu.add_command(label='Ayuda',command=Ayuda_)



root.config(menu=barMenu)
root.mainloop()