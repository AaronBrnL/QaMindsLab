name=input("Cual es tu nombre: ")
edad=input("Cual es tu edad: ")
ciudad=input("En que ciudad vives: ")
casado=input("Estas casado: ")
elige_num_1_100=input("Elige un numero entre el 1 y el 100: ")
elige_num_100_200=input("Elige un numero entre el 100 y el 200: ")


elige_num_1_100 = int(elige_num_1_100)
elige_num_100_200 = int(elige_num_100_200)

resul_div= (elige_num_1_100 / elige_num_100_200)


print(f'Mi nombre es: {name} mi edad es {edad} , soy de la ciudad de {ciudad} y mi resultado es de la división entre a y b es {resul_div}')