from tkinter import *

root=Tk()
root.title('Formulario')

name_var=StringVar()
email_var=StringVar()
pswd_var=StringVar()
# comment_var=StringVar()

def obtener_texto():
    #Función que se ejecuta al oprimir el botón "Enviar"
    name=name_var.get()
    email=email_var.get()
    password=pswd_var.get()
    print(f"Nombre: {name}\nEmail: {email}\nContraseña: {password}")

    root.destroy()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack(fill='both', expand='True')

#Etiqueta y campo de nombre
nameLabel=Label(miFrame, text='Nombre: ').grid(row=0, column=0, sticky='e')
nameBox=Entry(miFrame, width=50, textvariable=name_var).grid(row=0, column=1, pady=5)
#Etiqueta y campo de email
emailLabel=Label(miFrame, text='Email: ').grid(row=1,column=0, sticky='e')
emailBox=Entry(miFrame, width=50, textvariable=email_var).grid(row=1, column=1, pady=5)
#Etiqueta y campo de contraseña
pswdLabel=Label(miFrame, text='Password: ').grid(row=2, column=0, sticky='e')
pswdBox=Entry(miFrame, width=50, textvariable=pswd_var, show='$').grid(row=2, column=1, pady=5)

#Etiqueta y campo de comentario (con scroll-bar)

commentLabel=Label(miFrame, text='Comentario').grid(row=3, column=0, sticky='e')
commentBox=Text(miFrame, width=50, height=15).grid(row=3, column=1, pady=5)

scrollBar=Scrollbar(miFrame, command=commentBox).grid(row=3, column=2, sticky='nsew')

Button(miFrame, text='Enviar', command=obtener_texto,).grid(row=4, column=0, pady=10, columnspan=2)

root.mainloop()


