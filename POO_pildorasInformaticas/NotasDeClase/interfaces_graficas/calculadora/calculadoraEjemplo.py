from tkinter import *
from math import sqrt
from funcionesCalculadora import *

#Creación de la ventana
main=Tk()
main.title('CALCULADORA')

#Creación de la pantalla de ingreso

screen=Entry(main, font=('arial',20,'bold'),
             width=18,
             justify='right',
             background='black',
             foreground='white')
screen.pack(padx=10,pady=(10,0), ipady=10, fill=BOTH)
screen.insert(0,'0')
teclado=Frame(main)
teclado.pack(padx=10, pady=10)
#Agregamos los valores de los botones

Botones=[['C', 'x^2', '%', '√'],
         ['7', '8', '9', '/'],
         ['4', '5', '6', 'x'],
         ['1', '2', '3', '-'],
         [',', '0', '=', '+']]

#Función para cada botón
def press_btn(text):
    match text:
        case '=':
            result= eval(screen.get().replace('²', '**2'))
            screen.delete(0, 'end')
            screen.insert(0, result)
        case 'C':
            screen.delete(0, 'end')
        case _:
            if screen.get()=='0':
                screen.delete(0,1)
            screen.insert(END, text.replace('x^2', '²').replace('x','*'))

def funcion_btn(text):
    return lambda:press_btn(text)

for i in range(5):
    for j in range(4):
        Button(teclado,
               width=6,
               height=3,
               background='#33C1FF',
               foreground='black',
               font=('arial', 20, 'bold'),
               text=Botones[i][j],
               command= funcion_btn(Botones[i][j]),
               cursor='hand2').grid(row=i, column=j)

main.mainloop()