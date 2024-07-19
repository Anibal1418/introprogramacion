#Números Primos

def es_primo(x):
    if(x == 1):
        return False
    elif(x == 2 or x == 3 or x ==5 or x == 7):
        return True
    for i in (2, 3, 5, 7):
        if(x%i == 0):
            return False
    return True

while(True):
    try:
        num = int(input("Deme un numero entero: "))
        if(es_primo(num)):
            print(f"El numero {num} es primo.")
            break
        else:
            print(f"El numero {num} no es primo.")
            break
    except:
        print("Asegurese que sea un numero y entero.")
