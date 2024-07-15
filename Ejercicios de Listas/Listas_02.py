#Leer 10 enteros, almacenarlos en una lista y 
#determinar en qué posición de del arreglo está el mayor número par leído.
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

mayornumpar = int
j=0
while(True):
    if(j == 10):
        print("La lista no tiene numeros pares.")
        break
    elif(lista[j]%2==0):
        mayornumpar = lista[j]
        break
    j+=1
try:
    for num in lista:
        if(num%2==0 and num > mayornumpar):
            mayornumpar = num
    print(f"La posicion del mayor entero par de la lista es: {lista.index(mayornumpar)}")
except:
    print("Sin numero pares, no hay comparacion.")


