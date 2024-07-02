#Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído
while(True):
    try:
        b = int(float(input("Dame un número entero: ")))
        for i in range(1,b+1):
            if i%2 == 0:
                print(i)
        break
    except:
        print("No es un número entero, try again")