class coche():
    def desplazamiento(self):
        return 'Me desplazo utilizando 4 ruedas'
    
class moto():
    def desplazamiento(self):
        return 'Me desplazo en dos ruedas'
    
class camion():
    def desplazamiento(self):
        return 'Me desplazo utilizando seis ruedas'
    
def desplazamientoVehiculo(vehiculo):
    return vehiculo.desplazamiento()

miVehiculo=camion()

print(desplazamientoVehiculo(miVehiculo))



