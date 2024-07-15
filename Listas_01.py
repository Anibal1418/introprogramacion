#Leer 10 enteros, almacenarlos en una lista y 
#determinar en qué posición del arreglo está el mayor número leído.
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

mayornum = lista[0]
for num in lista:
    if(num > mayornum):
        mayornum = num


print(f"La posicion del mayor entero de la lista es: {lista.index(mayornum)}")
