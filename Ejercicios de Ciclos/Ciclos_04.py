#Leer dos números y mostrar todos los enteros comprendidos entre ellos.
while(True):
    try:
        d = int(float(input("Dame el valor inicial de un intervalo: ")))
        e = int(float(input("Dame el valor final del intervalo: ")))
        for i in range(d, e+1):
             print(i)
        break
    except:
        print("Debe ser un número entero, try again")