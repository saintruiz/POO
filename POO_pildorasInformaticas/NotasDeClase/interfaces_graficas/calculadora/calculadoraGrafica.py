#Debemos construir una calculadora gráfica
from tkinter import *
from funcionesCalculadora import *


root=Tk()
root.title('Calculadora')

mainFrame=Frame(root)
mainFrame.pack()


#----------------------ESPACIO PARA FUNCIONES----------------------

mainString=StringVar()


def pulsarBoton(n:str):
    if n=='0' and mainString.get()=='':
        #codicional para evaluar si el número que se va a ingresar al principio es cero y se ignore
        pass
    else:
        mainString.set(mainString.get() + n)

def clearText():
    mainString.set('')

#FILA DE LA PANTALLA
pantalla=Entry(mainFrame, bg='Black', fg='#03f943', justify='right', width=75, textvariable=mainString).grid(row=0, columnspan=4, padx=10, pady=10)

#Se crea la pantalla en la cual la variable de texto será la mainString (Vamos a manipular la mainString en todo el programa)



#---------------------PRIMERA FILA DE BOTONES------------------------
#Se crea cada botón declarando sus configuraciones principales, y también una función lambda que va a manipular la mainString, trayendo lo que había y sumándole el texto del número
boton7=Button(mainFrame, text="7", width=15, height=3, bd=3, command=lambda:pulsarBoton('7')).grid(row=1, column=0)

boton8=Button(mainFrame, text='8', width=15, height=3, bd=3, command=lambda:pulsarBoton('8')).grid(row=1, column=1)

boton9=Button(mainFrame, text='9', width=15, height=3, bd=3, command=lambda:pulsarBoton('9')).grid(row=1, column=2)

botonDivision=Button(mainFrame, text='÷', width=15, height=3, bd=3, command=lambda:pulsarBoton('÷')).grid(row=1, column=3)


#------------------------SEGUNDA FILA DE BOTONES---------------------------------


boton4=Button(mainFrame, text='4', width=15, height=3, bd=3, command=lambda:pulsarBoton('4')).grid(row=2, column=0)

boton5=Button(mainFrame, text='5', width=15, height=3, bd=3, command=lambda:pulsarBoton('5')).grid(row=2, column=1)

boton6=Button(mainFrame, text='6', width=15, height=3, bd=3, command=lambda:pulsarBoton('6')).grid(row=2, column=2)

botonMultiplicacion=Button(mainFrame, text='x', width=15, height=3, bd=3, command=lambda:pulsarBoton('x')).grid(row=2, column=3)


#-------------------------TERCERA FILA DE BOTONES------------------


boton1=Button(mainFrame, text='1', width=15, height=3, bd=3, command=lambda:pulsarBoton('1')).grid(row=3, column=0)

boton2=Button(mainFrame, text='2', width=15, height=3, bd=3, command=lambda:pulsarBoton('2')).grid(row=3, column=1)

boton3=Button(mainFrame, text='3', width=15, height=3, bd=3, command=lambda:pulsarBoton('3')).grid(row=3, column=2)

botonResta=Button(mainFrame, text='-', width=15, height=3, bd=3, command=lambda:pulsarBoton('-')).grid(row=3, column=3)


#------------------------CUARTA FILA DE BOTONES---------------------


botonDecimal=Button(mainFrame, text=',', width=15, height=3, bd=3, command=lambda:pulsarBoton(',')).grid(row=4, column=0)

boton0=Button(mainFrame, text='0', width=15, height=3, bd=3, command=lambda:pulsarBoton('0')).grid(row=4, column=1)

botonIgual=Button(mainFrame, text='=', width=15, height=3, bd=3, command=lambda:mainString.set(main(mainString.get()))).grid(row=4, column=2)

botonResta=Button(mainFrame, text='+', width=15, height=3, bd=3, command=lambda:pulsarBoton('+')).grid(row=4, column=3)

#-------------------------Fila para limpiar----------------
botonLimpiar=Button(mainFrame, text='Limpiar', height=3, bd=3, command=lambda:mainString.set('')).grid(row=5, columnspan=4)

root.mainloop()