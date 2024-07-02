#Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
while(True):
    try:
        m = int(float(input("Deme un número entero: ")))
        for i in range(1, m+1):
            if((i%5)==0):
                print(i)
        break
    except:
        print("Debe ser un número entero, intente de nuevo")