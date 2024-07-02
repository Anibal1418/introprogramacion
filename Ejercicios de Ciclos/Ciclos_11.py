#Leer un número entero de dos dígitos 
#y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro
while(True):
    try:
        h =input("Deme un número entero de dos digitos: ")
        if(len(h) != 2):
            raise Exception("El número debe ser de dos dígitos")
        h = int(float(h))
        PriDig = h%10
        SegDig = int(h/10)%10
        if (PriDig < SegDig):
            for i in range(PriDig, SegDig+1):
                print(i)
            break
        elif (SegDig < PriDig):
            for i in range(SegDig, PriDig+1):
                print(i)
            break
        else:
            print("Los Números son iguales")
            break
    except:
        print("Debe ser un número entero y de dos digitos, intente de nuevo")