from math import *
import re

def main(string:str):
    if 'x' in string:
        lista=string.split('x')
        return (int(lista[0])*int(lista[1]))
    
    elif '/' in string:
        lista=string.split('/')
        try:
            return float(int(lista[0])/int(lista[1]))
        except ZeroDivisionError:
            return "No se puede dividir por 0"
        
    elif '+' in string:
        lista=string.split('+')
        return (int(lista[0])+int(lista[1]))
    
    elif '-' in string:
        lista=string.split('-')
        return (int(lista[0])-int(lista[1]))


# def principal (cadena:str):
#     mainLista=re.findall(r'[0-9]+|[+\-*/X]', cadena)
    
