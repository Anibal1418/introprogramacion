#Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay
lista = []
i=0
while(i<10):
    try:
        dato = int(float(input("Entre un numero entero: ")))
        lista.append(dato)
        i+=1
    except:
        print("Los valores deben ser numeros enteros, intente de nuevo.")

count = 0
for num in lista:
    if(num < 0):
        count+=1
print(f"En la lista proveida hay {count} numeros enteros negativos.")