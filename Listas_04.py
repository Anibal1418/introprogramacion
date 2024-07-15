# Leer 10 números enteros, almacenarlos en una lista y determinar 
# cuántos números de los almacenados en dicho arreglo comienzan en dígito primo

digprimos = [2, 3, 5, 7]
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
    for dig in digprimos:
        if(num%10 == dig):
            count+=1
print(f"{count} números de la lista comienzan en dígitos primos.")