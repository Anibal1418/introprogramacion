#Leer 10 números enteros, almacenarlos en una lista 
#y determinar a cuánto es igual el promedio entero de los datos de la lista
lista = []
i=0
while(i<10):
    try:
        dato = int(float(input("Entre un numero entero: ")))
        lista.append(dato)
        i+=1
    except:
        print("Los valores deben ser numeros enteros, intente de nuevo.")
print(lista)

print(f"El promedio entero de los valores de la lista es {int(sum(lista)/len(lista))}.")