#Conversión de Grados Celsius a Fahrenheit

def CaF(x):
    return '%.2f'%(32 + (9/5)*x)
try:
    n = float(input("Deme la temperatura en Celsius: "))
    print(f"La temperatura en Fahrenheit es de {CaF(n)} grados.")
except:
    print("Debe ser un numero. Intente de nuevo.")