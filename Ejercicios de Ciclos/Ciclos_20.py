#Leer un número entero y calcular a cuánto es igual la sumatoria de 
#todas las factoriales de los números comprendidos entre 1 y el número leído
def fact(x):
    if(x == 1 or x == 0):
        return 1
    return x*fact(x-1)

while(True):
    try:
        num = int(input("Déme un número entero: "))
        sum = 0
        for i in range(1, num+1):
            sum += fact(i)
        print(f"La sumatoria de las factoriales entre 1 y {num} es {sum}")
        break
    except:
        print("Asegúrese que el valor dado sea un número entero")