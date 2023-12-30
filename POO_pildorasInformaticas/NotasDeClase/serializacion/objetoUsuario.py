from paquetesUsuario.claseUsuario import *
import pickle

userAlexis=empleado(1500, 5, 'Alexis Duque', 42, 'Santiado de Chile')


userData={
    'Nombre':userAlexis.userName,
    'Edad':userAlexis.userAge,
    'Residencia':userAlexis.userResidance,
    'Salario':userAlexis.salario,
    'Antiguedad':userAlexis.antiguedad
}


ficheroBinario=open('AlexisDuque', 'wb')

pickle.dump(userData, ficheroBinario)

ficheroBinario.close()
