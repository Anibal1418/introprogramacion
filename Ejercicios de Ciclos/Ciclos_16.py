#Promediar los x primeros múltiplos de 2 
#y determinar si ese promedio es mayor que los y primeros múltiplos de 5 
#para valores de x y y leídos
while(True):
    try:
        x = int(input("Determine cuántos múltiplos de 2 se usarán para comparar: "))
        y = int(input("Determine cuántos múltiplos de 5 se usarán para comparar: "))
        avgx=0
        avgy=0
        for i in range(1,x+1):
            avgx += 2*i
        for j in range(1, y+1):
            avgy += 5*j
        avgx =(avgx/x)
        avgy = (avgy/y)
        if (avgx > avgy):
            print(f"El promedio de los {x} primeros múltiplos de 2 es mayor que el promedio de los {y} primeros múltiplos de 5.")
            print(f"{avgx} > {avgy}")
        elif (avgy > avgx):
            print(f"El promedio de los {x} primeros múltiplos de 2 es menor que el promedio de los {y} primeros múltiplos de 5.")
            print(f"{avgx} < {avgy}")
        else:
            print(f"El promedio de los {x} primeros múltiplos de 2 es igual que el promedio de los {y} primeros múltiplos de 5.")
            print(f"{avgx} = {avgy}")
        break
    except:
        print("Se pide un número entero, intente de nuevo")
