#Leer 10 números enteros, almacenarlos en una lista y 
#calcular la factorial a cada uno de los números leídos almacenándolos en otra lista
lista = []
factoriales = []

def fact(x):
    if(x == 1 or x == 0):
        return 1
    return x*fact(x-1)

i=0
while(i<10):
    try:
        dato = int(float(input("Entre un numero entero: ")))
        lista.append(dato)
        i+=1
    except:
        print("Los valores deben ser numeros enteros, intente de nuevo.")
print(lista)

for num in lista:
    factoriales.append(fact(num))

print(f"Las factoriales de todos los numeros proveidos, en orden, son: {factoriales}.")