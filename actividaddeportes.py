#Realizar un programa que capture los resultados por equipo del deporte de su preferencia
# y al final los imprima en pantalla.

equipos = []
resultados = []

n = input("Número de equipos de fútbol por analizar: ")

for i in range(int(n)):
  equipos.append(input("Nombre del equipo de fútbol: "))
  resultados.append((int(input("Número de victorias del equipo en cuestión: "))))

for i in range(len(equipos)):
  print(f"\nEl equipo del {equipos[i]} ha logrado conseguir {resultados[i]} victorias.")