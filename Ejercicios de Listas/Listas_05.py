#Leer 10 números enteros, almacenarlos en una lista y 
#determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares
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
print(lista)

listaprimos = []
conteos = []
j=0
while(j<10):
    if(j == 9 and len(listaprimos)==0):
        print("La lista no tiene numeros primos.")
        break
    elif(es_primo(lista[j])):
        listaprimos.append(lista[j])
    else:
        listaprimos.append(0)
    j+=1

try:
    for num in listaprimos:
        conteo = 0
        for i in str(num):
            if(int(i)%2 == 0 and int(i) != 0):
                conteo+=1
        conteos.append(conteo)
    print(f"El numero primo con mayor cantidad de digitos pares esta en la posicion {conteos.index(max(conteos))} del arreglo.")
except:
    print("Sin numeros primos, no hay comparacion.")