#Filtrar elementos: filtrar una lista de números para obtener solo los números pares.

listanum = []
n = int(input("Número de elementos de la lista a filtrar: "))

for i in range(n):
  num = int(input(f"Ingrese un número hasta llenar la lista con {n} espacios: "))
  listanum.append(num)

print("\nAhora se filtrará la lista de manera que solo queden números pares\n")

for numb in listanum:
  if (numb % 2 != 0):
    listanum.remove(numb)
    
print(f"La lista filtrada queda como: {listanum}\n")


#Operaciones matemáticas: calcular la media de una lista de números.

listamath = []
m = int(input("Número de elementos de la lista para calcular su promedio: "))

for i in range(m):
  num = int(input(f"\nIngrese un número hasta llenar la lista con {m} espacios: "))
  listamath.append(num)

suma = 0

for j in range(len(listamath)):
  suma += listamath[j]

print(f"\nEl promedio de los números insertados en la lista {listamath} es {suma/len(listamath)}\n")

#Acceder y modificar elementos: utilizar índices (o llaves, en este caso) para acceder a elementos en un diccionario y modificarlos.

schooldict = {'Escuelas':1, 'Estudiantes':30, 'Profesores':6, 'Materias':12}

while(True):
  modif = input(f"\nAhora, ingrese la llave que quiere modificar, o añadir, en el diccionario del sistema escolar {schooldict}:\n")
  if (modif in schooldict):
    try:
      schooldict[modif] = int(input("Ingrese el nuevo valor de la información (entero): "))
    except:
      print("Valor no válido")
  else:
    print("Llave no válida")

  conf = input("\nDesea cambiar otro valor? Y/N: ")
  if (conf == 'N'):
    break

print("\nEl diccionario escolar ahora se ve así: ", schooldict)