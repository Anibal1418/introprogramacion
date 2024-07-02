#Leer un número entero de 3 dígitos y determinar si tiene el dígito 1
while(True):
    try:
        h =input("Deme un número entero de tres digitos: ")
        if(len(h) != 3):
            raise Exception("El número debe ser de tres dígitos")
        h = int(float(h))
        PriDig = h%10
        SegDig = int(h/10)%10
        TriDig = int(h/100)%10
        count1 = 0
        if(PriDig == 1):
                print('El Primer Dígito es 1')
                count1+=1
        if(SegDig == 1):
                print('El Segundo Dígito es 1')
                count1+=1
        if(TriDig == 1):
                print('El Tercer Dígito es 1')
                count1+=1
        if(count1 == 0):
              print("Ningún dígito del número es 1")
        break
    except:
        print("Debe ser un número entero y de tres digitos, intente de nuevo")