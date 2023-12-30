class usuario():
    def __init__(self, userName, userAge, userResidance):

        self.userName=userName
        self.userAge=userAge
        self.userResidance=userResidance

    def desciption(self):
       description=(f"Nombre: {self.userName}, Edad: {self.userAge}, Lugar de residencia: {self.userResidance}") 
       return description
    
class empleado(usuario):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario=salario
        self.antiguedad=antiguedad


    def desciption(self):
        print(super().desciption())
        descripcionEmpleado= (f"Salario del empleado: {self.salario}, Antiguedad del empleado: {self.antiguedad}")
        return descripcionEmpleado
    


