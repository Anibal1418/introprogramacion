#Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3
print("La suma de los primeros 20 múltiplos de 3 es: ")
sum = 0
for i in range(1, 21):
    sum += 3*i
print(sum)