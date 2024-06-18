#Sistema que capture 4 notas de un alumno y luego muestre el promedio de las mismas.

def promedio(estudiante):
  sumatoria = 0
  promedio = 0
  for i in range(4):
    try:
      nota = int(input(f"Ingrese la nota {i+1} de {estudiante}: "))
    except:
      print("Las notas deben ser números enteros")
      exit()
    if (nota >= 0):
      sumatoria += nota
      promedio = sumatoria/4
    else:
      print("Las notas negativas no son válidas")
      exit()
  return promedio

dict = {}
while (True):
  student = input("Ingrese el nombre y matrícula del estudiante: ")
  dict.update({student:promedio(student)})
  print(f"El promedio de notas del estudiante {student} es {dict[student]}.")
  print("----------------------------------------\n")
  salida = input("Desea evaluar otro estudiante? Y/N: ")
  if (salida == "N"):
    for key, value in dict.items():
      print(f"Estudiante {key} tiene un promedio de {value}")
    break
