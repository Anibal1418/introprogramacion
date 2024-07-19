#Palíndromo

def palindromo(nombre):
    if(nombre.lower() == nombre[::-1].lower()):
        print(f"La palabra '{nombre}' es un palindromo.")
    else:
        print(f"La palabra '{nombre}' no es un palindromo.")

palabra = input("De una palabra para comprobar:\n")
palindromo(palabra)