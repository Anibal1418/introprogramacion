#Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 
#y cada uno de los dígitos.
while(True):
    try:
        h =input("Deme un número entero de tres digitos: ")
        if(len(h) != 3):
            raise Exception("El número debe ser de tres dígitos")
        h = int(float(h))
        PriDig = h%10
        SegDig = int(h/10)%10
        TriDig = int(h/100)%10
        print("Primer Digito")
        if(PriDig == 0):
                print('0')
        for i in range(1, PriDig+1):
            print(i)
        print("Segundo Digito")
        if(SegDig == 0):
                print('0')
        for i in range(1, SegDig+1):
            print(i)
        print("Tercer Digito")
        if(TriDig == 0):
                print('0')
        for i in range(1, TriDig+1):
            print(i)
        break
    except:
        print("Debe ser un número entero y de tres digitos, try again")