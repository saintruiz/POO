from io import *


archivoTexto=open('archivo.txt', 'r+')

archivoTexto.write('\nSiempre es una buena ocasión para estudiar programacion')
texto=archivoTexto.read()

archivoTexto.close()

print(texto)



