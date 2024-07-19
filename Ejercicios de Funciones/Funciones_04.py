#Número Par o Impar

def parity(x):
    if(x%2 == 0):
        print("El numero proveido es par.")
    else:
        print("El numero proveido es impar.")

n = int(float(input("Deme un numero entero: ")))
parity(n)