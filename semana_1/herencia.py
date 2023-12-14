class vehiculos():
    def __init__(self, tipo, marca, modelo):
        self.tipo=tipo
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
        self.estado=None

    def arrancar (self):
        self.enMarcha=True
    
    def acelerar (self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estadoObjeto (self):
        if self.enMarcha and self.acelera and not self.frena:
            return 'El vehiculo está en marcha y acelerando'
        elif self.enMarcha and self.frena and not self.acelera:
            return 'El vehiculo está en marcha y frenando'
        elif self.enMarcha:
            return 'El vehiculo está en marcha pero no está acelerando ni frenando'
        else:
            return 'El vehiculo está en reposo'
        
    def retornarCaracteristicas(self):
        return 'Tipo de vehículo: ' + self.tipo + 'Marca del vehículo: ' + self.marca + 'Modelo del vehículo: ' + self.modelo
    
class furgoneta(vehiculos):
    __estadoDeCarga=False
    def carga (self):
        self.__estadoDeCarga=True
    
    def estadoObjeto (self):
        if self.enMarcha and self.acelera and self.__estadoDeCarga and not self.frena:
            return 'El vehiculo está en marcha, acelerando y va cargado'
        elif self.enMarcha and self.frena and self.__estadoDeCarga and not self.acelera:
            return 'El vehiculo está en marcha, frenando y va cargado'
        elif self.enMarcha:
            return 'El vehiculo está en marcha pero no está acelerando ni frenando'
        else:
            return 'El vehiculo está en reposo'

class motocicleta(vehiculos):
    __estadoCaballito=False

    def caballito(self):
        self.__estadoCaballito=True
    
    def estadoObjeto (self):
        if self.enMarcha and self.acelera and self.__estadoCaballito and not self.frena:
            return 'El vehiculo está en marcha, acelerando y haciendo el caballito'
        elif self.enMarcha and self.frena and not self.acelera:
            return 'El vehiculo está en marcha y frenando'
        elif self.enMarcha:
            return 'El vehiculo está en marcha pero no está acelerando ni frenando'
        else:
            return 'El vehiculo está en reposo'


miMoto=motocicleta ('Moto', 'Kawasaki', 'Ninja H2R')
miMoto.arrancar()
miMoto.acelerar()
miMoto.caballito()
print(miMoto.estadoObjeto())

miFurgoneta=furgoneta('Camion', 'Renault', 'Kangoo' )
miFurgoneta.arrancar()
miFurgoneta.acelerar()
miFurgoneta.carga()
print(miFurgoneta.estadoObjeto())