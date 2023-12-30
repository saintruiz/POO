import tkinter as tk
from tkinter import Label, Entry, StringVar

def submit_form():
    # Función que se ejecutará al hacer clic en el botón "Enviar"
    nombre = nombre_var.get()
    email = email_var.get()
    usuario = usuario_var.get()
    contraseña = contraseña_var.get()

    # Puedes realizar acciones con los datos, como imprimirlos en la consola
    print(f"Nombre: {nombre}\nEmail: {email}\nUsuario: {usuario}\nContraseña: {contraseña}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario")

# Variables para almacenar los datos ingresados
nombre_var = StringVar()
email_var = StringVar()
usuario_var = StringVar()
contraseña_var = StringVar()

# Etiquetas y campos de entrada
Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
Entry(ventana, textvariable=nombre_var).grid(row=0, column=1, padx=10, pady=5)

Label(ventana, text="Email:").grid(row=1, column=0, padx=10, pady=5)
Entry(ventana, textvariable=email_var).grid(row=1, column=1, padx=10, pady=5)

Label(ventana, text="Usuario:").grid(row=2, column=0, padx=10, pady=5)
Entry(ventana, textvariable=usuario_var).grid(row=2, column=1, padx=10, pady=5)

Label(ventana, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5)
Entry(ventana, textvariable=contraseña_var, show="*").grid(row=3, column=1, padx=10, pady=5)

# Botón para enviar el formulario
tk.Button(ventana, text="Enviar", command=submit_form).grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
