#Máximo de Tres Números

def maximo(list):
    return max(list)

listanum = []
i = 0
while (i < 3):
    try:
        x = float(input("De los tres numeros que desee comparar: "))
        i += 1
        listanum.append(x)
    except:
        print("Debe ser un entero, intente de nuevo.")

print(f"El maximo de los numeros proveidos es {maximo(listanum)}.")