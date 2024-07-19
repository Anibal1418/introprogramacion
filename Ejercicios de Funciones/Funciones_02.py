#Función de Suma

def sumatoria(list):
    return sum(list)

listanum = []
while (True):
    try:
        x = float(input("Deme los numeros que desee sumar, escriba cero para parar: "))
        if(x == 0):
            break
        else:
            listanum.append(x)
    except:
        print("Debe ser un entero, intente de nuevo.")

print(f"La sumatoria de los numeros proveidos es {sumatoria(listanum)}.")