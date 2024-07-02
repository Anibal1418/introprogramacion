#Leer un número entero y mostrar en pantalla su tabla de multiplicar
while(True):
    x = int(float(input("Deme un número entero: ")))
    print(f"La tabla de multiplicación de {x} es: ")
    for i in range(1,13):
        print(x*i)
    break