#Hacer una aplicación que reciba el nombre de los estudiantes y las notas
#y al final imprima la nota promedio de cada uno

estudiantes = []
promedios = []

n = input("Número de estudiantes en la clase: ")
m = input("Número de materias por clase: ")

for i in range(int(n)):
  notas = 0
  estudiantes.append(input("Nombre del estudiante: "))
  for j in range(int(m)):
    nota = (float(input("Nota del estudiante: ")))
    notas += nota
  promedio = notas / int(m)
  promedios.append(promedio)

for i in range(len(estudiantes)):
  print(f"El promedio de {estudiantes[i]} es: {promedios[i]}")