#Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.
while(True):
    try:
        f = int(float(input("Dame el valor inicial de otro intervalo: ")))
        g = int(float(input("Dame el valor final del intervalo: ")))
        for i in range(f, g+1):
            if((i%10)==4):
                print(i)
        break
    except:
        print("Debe ser un número entero, try again")