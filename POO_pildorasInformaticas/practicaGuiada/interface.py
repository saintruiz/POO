from tkinter import *
from mainFunctions import *

root=Tk()
root.title('CRUD')

#FILA SUPERIOR-------------------------------

barMenu=Menu(background='#FFB81C', fg='black', border=3)

##Espacio para botón BBDD
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
    IDvar.set('')
    nameVar.set('')
    lastNameVar.set('')
    pswdVar.set('')
    addrVar.set('')
    print('Interface has been cleaned')

barMenu.add_command(label='Borrar', command=Clean_)

##Espacio para boton CRUD
def CreateUser():
    CreateInB(IDvar.get(), nameVar.get(), lastNameVar.get(), pswdVar.get(), addrVar.get())
    IDvar.set('')
    nameVar.set('')
    lastNameVar.set('')
    pswdVar.set('')
    addrVar.set('')
    print('User has been created')

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
    command=CreateUser
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
barMenu.add_command(label='Help',command=Ayuda_)


#BLOQUE MEDIO----------------------------------------------

frm=Frame(root, background='#FFB81C').config(width=500, height=500)


IDvar=StringVar()
nameVar=StringVar()
lastNameVar=StringVar()
pswdVar=StringVar()
addrVar=StringVar()



IDlabel=Label(frm, text='ID' ).grid(row=0, column=0)
IDentry=Entry(frm, textvariable=IDvar, width=50).grid(row=0, columnspan=3, column=1, padx=20, pady=20)

nameLabel=Label(frm, text='Name' ).grid(row=1, column=0)
nameEntry=Entry(frm, textvariable=nameVar, width=50).grid(row=1, columnspan=3, column=1, padx=20, pady=20)

lastNameLabel=Label(frm, text='Last Name' ).grid(row=2, column=0)
lastNameEntry=Entry(frm, textvariable=lastNameVar, width=50).grid(row=2, columnspan=3, column=1, padx=20, pady=20)

pswdLabel=Label(frm, text='Password' ).grid(row=3, column=0)
pswdEntry=Entry(frm, textvariable=pswdVar, show='$',width=50).grid(row=3, columnspan=3, column=1, padx=20, pady=20)

addLabel=Label(frm, text='Address' ).grid(row=4, column=0)
addEntry=Entry(frm, textvariable=addrVar, width=50).grid(row=4, columnspan=3, column=1, padx=20, pady=20)

createBT=Button(frm, text='Create', command=CreateUser, background='#FFB81C').grid(row=5, column=0)
readBT=Button(frm, text='Read', command=Read_, background='#FFB81C').grid(row=5, column=1)
updateBT=Button(frm, text='Update', command=Update_, background='#FFB81C').grid(row=5, column=2)
deleteBT=Button(frm, text='Delete', command=Delete_, background='#FFB81C').grid(row=5, column=3)



root.config(menu=barMenu)
root.mainloop()