import pickle
from paquetesCoche.claseCoche import *
import time

fichero=open('losCoches', 'rb')

data=pickle.load(fichero)

fichero.close()

del(fichero)

for coche in data:
    print(coche.movimiento())
    print(coche.estadoCoche())
    print(coche.retornarCaracteristicas())
    time.sleep(2)