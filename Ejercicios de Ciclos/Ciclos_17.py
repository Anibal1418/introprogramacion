#Leer números hasta que digiten 0 y determinar a cuánto es 
# igual el promedio de los números terminados en 5.
lista = []
x = 1
avg = 0
count = 0
while(True):
    try:
        while(x != 0):
            x = int(float(input("Digite un número, digite 0 en caso de no querer dar más números: ")))
            lista.append(x)
        for num in lista:
            if(num%10 == 5):
                avg += num
                count += 1
        agv = (avg/count)
        print(f"El promedio de los números dados terminados en 5 es: {avg}")
        break
    except:
        print("Asegúrese que los valores digitados sean números.")
