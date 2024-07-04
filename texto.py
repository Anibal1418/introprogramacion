#Leer un texto y realizar las siguientes operaciones:
#1) Retornar todo el texto en mayúsculas
#2) Retornar todo el texto en minúsculas
#3) Retornar los dos primeros caracteres del texto
#4) Retornar los dos últimos caracteres del texto
#5) Retornar la cantidad de veces que se repite el último caracter
#6) Retornar el texto invertido

text = input("Deme un texto cualquiera: ")
#1
mayus = text.upper()
print("En mayúsculas:", mayus)
#2
minus = text.lower()
print("En Minúsculas:", minus)
#3
doschar = text[:2]
print("Primeros dos caracteres:", doschar)
#4
dosultchar = text[-2:]
print("Últimos dos caracteres:", dosultchar)
#5
lastcha = text[-1:].lower()
count = 0
for cha in text:
    if(cha.lower() == lastcha):
        count += 1
print(f"El último caracter se repite {count} veces.")
#6
inv = text[::-1]
print("La palabra invertida es:", inv)
