#Dado el texto:

dato="oso,perro,10,5 son animales"

#Imprimir los siguientes valores:
# oso es un palindromo
# perro no es un palindromo
# tenemos 5 oso
# tenemos 10 perro
# oso y perro son animales

animals = []
animals.append(dato.split(",")[0])
animals.append(dato.split(",")[1])
for animal in animals:
    if(animal==animal[::-1]):
        print(f"{animal} es un palindromo")
    else:
        print(f"{animal} no es un palindromo")
numoso = dato.split(",")[3][:1]
print(f"tenemos {numoso} {animals[0]}")
numperro = dato.split(",")[2]
print(f"tenemos {numperro} {animals[1]}")
frase = dato.split(",")[3][2:]
print(f"{animals[0]} y {animals[1]} {frase} ")