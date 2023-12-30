from tkinter import *

root=Tk()
#Creaciónn de la raíz
root.title('Ventada de pruebas')
root.config(bg='LightYellow')


#Creación de frame

miFrame=Frame(root, width=1000, height=1000)
miFrame.pack(fill='both', expand='True')
miFrame.config(bg='PaleGreen4')

#Creación de Label

Label(miFrame, text='Hello, World', font=('Comic Sans MS', 18), bd=0, bg='PaleGreen4').place(x=0, y=0)

miImagen=PhotoImage(file='Isotipo.png')

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()
