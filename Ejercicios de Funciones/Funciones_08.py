#Factorial
def fact(x):
    if(x == 1 or x == 0):
        return 1
    return x*fact(x-1)

while(True):
    try:
        num = int(input("Déme un número entero: "))
        print(f"El factorial de {num} es {fact(num)}")
        break
    except:
        print("Asegúrese que el valor dado sea un número entero")