#Leer un número entero, mostrar todos los enteros comprendidos entre 1 y el número leído
while(True):
    try:
        a = int(float(input("Dame un número entero: ")))
        for i in range(1,a+1): #Incluyendo 1 y el número leído
            print(i)
        break
    except:
        print("No es un número entero, try again")