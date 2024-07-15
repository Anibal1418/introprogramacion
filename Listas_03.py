#Leer 10 enteros, almacenarlos en una lista y 
#determinar en qué posición del arreglo está el mayor número primo leído
lista = []
def es_primo(x):
    if(x == 1):
        return False
    elif(x == 2 or x == 3 or x ==5 or x == 7):
        return True
    for i in (2, 3, 5, 7):
        if(x%i == 0):
            return False
    return True
i=0
while(i<10):
    try:
        dato = int(float(input("Entre un numero entero: ")))
        lista.append(dato)
        i+=1
    except:
        print("Los valores deben ser numeros enteros, intente de nuevo.")

mayornumprimo = int
j=0
while(True):
    if(j == 10):
        print("La lista no tiene numeros primos.")
        break
    elif(es_primo(lista[j])):
        mayornumprimo = lista[j]
        break
    j+=1
try:
    for num in lista:
        if(es_primo(num) and num > mayornumprimo):
            mayornumprimo = num
    print(f"La posicion del mayor entero primo de la lista es: {lista.index(mayornumprimo)}")
except:
    print("Sin numeros primos, no hay comparacion.")