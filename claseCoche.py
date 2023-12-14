class coche():
    def __init__(self):
        self.__largo_chasis=250
        self.__ancho_chasis=120
        self.__ruedas=4
        self.__en_marcha=False
        self.__estado=None
    #Definimos un constructor que dará el estado inicial de la clase
    def __chequeo_interno(self):
        self.gasolina='Not Okay'
        self.aceite='Ok'
        self.puertas='cerradas'
        if self.gasolina=='Ok' and self.aceite=='Ok' and self.puertas=='cerradas':
            return True
        else:
            return False
        
    def movimiento(self):
        self.__en_marcha=self.__chequeo_interno()
        if self.__en_marcha:
            return "El coche está en movimiento"
        else: 
            return "El coche está en reposo"
        #Definimos un método "movimiento" que recibe como parametro un boolean y define si el coche está en movimiento o en marcha

    def estadoCoche(self):
        self.__estado=self.movimiento()
        #Definimos un método que altere el dato "estado" y le de el valor que retorne el método "movimiento"
        return 'El estado del coche: ' + self.__estado
    
    def retornarCaracteristicas (self):
        return "Las características del coche= " + ' ruedas:' + str(self.__ruedas) + " Largo del chasis: " + str(self.__largo_chasis) + ' Ancho del chasis: ' + str(self.__ancho_chasis)
    
miCoche=coche()
print(miCoche.estadoCoche())
print(miCoche.retornarCaracteristicas())

