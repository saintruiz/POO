import tkinter as tk

ventana = tk.Tk()
ventana.title("Barra de menús en Tk")
ventana.config(width=400, height=300)
# Crear una barra de menús.
barra_menus = tk.Menu()
# Insertarla en la ventana principal.
ventana.config(menu=barra_menus)
ventana.mainloop()
