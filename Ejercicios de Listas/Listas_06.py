#Leer 10 números enteros, almacenarlos en una lista y 
#determinar en qué posiciones se encuentran los números con más de 3 dígitos
lista = []
posiciones = []
i=0
while(i<10):
    try:
        dato = int(float(input("Entre un numero entero: ")))
        lista.append(dato)
        i+=1
    except:
        print("Los valores deben ser numeros enteros, intente de nuevo.")

for num in lista:
    if(int(num/1000) != 0):
        posiciones.append(lista.index(num))

print(f"Los números con más de tres dígitos se encuentran en las posiciones {posiciones}")