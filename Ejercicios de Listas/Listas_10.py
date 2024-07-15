# Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y 
# determinar cuántos divisores exactos tiene este último número 
# entre los valores almacenados en la lista
lista = []
i=0
while(i<10):
    try:
        dato = int(float(input("Entre un numero entero: ")))
        lista.append(dato)
        i+=1
    except:
        print("Los valores deben ser numeros enteros, intente de nuevo.")

while(True):
    try:
        dividendo = int(float(input("Deme un número entero que actúe como dividendo: ")))
        break
    except:
        print("Debe ser un entero, intente de nuevo.")
count = 0
for num in lista:
    if(dividendo%num == 0):
        count+=1

print(f"El entero proveído tiene {count} divisores exactos en la lista inicial.")