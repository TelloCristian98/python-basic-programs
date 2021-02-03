import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + numeros + simbolos

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)    
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena)
    return contrasena


def run():
    password = generar_contrasena()
    print('Tu nueva contraseña es: ' + password)



if __name__ == '__main__':
    run()