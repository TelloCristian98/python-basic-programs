def palindromo(palabra):
    palabra = palabra.replace(' ','') #Elimina los espacios vacíos#
    palabra = palabra.lower() #convierte a minúsculas todas las letras#
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print ("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == '__main__':
    run()