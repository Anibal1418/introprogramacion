#Área de un Rectángulo

def Arectangle(b, h):
    return(b*h)

while(True):
    try:
        x = float(input("De la base de un rectangulo en centimetros: "))
        y = float(input("De la altura de un rectangulo en centimetros: "))
        break
    except:
        print("Los valores deben ser numericos. Intente de nuevo.")

print(f"El area del rectangulo proveido es de {Arectangle(x, y)} centimetros.")