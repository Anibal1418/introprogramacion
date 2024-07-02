#Leer un número entero y mostrar todos los divisores 
#exactos del número comprendidos entre 1 y el número leído
while(True):
    try:
        c = int(float(input("Dame un número entero: ")))
        for i in range(1,c+1):
            if c%i == 0:
                print(i)
        break
    except:
        print("No es un número entero, try again")