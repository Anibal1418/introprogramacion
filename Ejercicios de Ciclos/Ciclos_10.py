#Leer un número entero y determinar a 
#cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.
while(True):
    try:
        j = int(float(input("Deme un número entero para determinar la sumatoria: ")))
        sum = 0
        for i in range(1, j+1):
            sum += i
        print(f"La sumatoria de los enteros comprendidos entre 1 y {j} es {sum}.")
        break
    except:
        print("Debe ser un número entero, try again")