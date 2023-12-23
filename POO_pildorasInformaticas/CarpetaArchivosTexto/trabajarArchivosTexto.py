from io import *


archivoTexto=open('archivo.txt', 'r')

lineasTexto=archivoTexto.readlines()

archivoTexto.close()

print(lineasTexto)





