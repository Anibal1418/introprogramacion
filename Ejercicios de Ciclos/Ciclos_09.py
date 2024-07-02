#Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205
print("\n todos los números comprendidos entre 25 y 205 que terminan en 6 son: ")
for i in range(25, 206):
  if(i%10 == 6):
    print(i)
