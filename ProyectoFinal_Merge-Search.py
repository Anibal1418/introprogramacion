#Definir una función que tome un arreglo, el índice de su primer elemento, el del medio, y
#el último, para así partirlo a la mitad una y otra vez y organizar los elementos en esos
#subarreglos con una operación de comparación simple.

def Merger(array, p, m, u):
#Crear arreglos temporales para almacenar los datos en cada lado del arreglo (izquierda y derecha)
    iz = []
    der = []
    
    l = (m-p+1)
    r = (u-m)

    for i in range(0, l):
        iz.append(array[p+i])
    for j in range(0, r):
        der.append(array[m+j+1])
    
    a = 0 #índice del arreglo izquierdo
    b = 0 #índice del arreglo derecho
    k = p #índice del arreglo sorteado (empezando desde el indice del arreglo dado)

#Comparación simple, si un elemento es menor que el otro, remplazar del arreglo temporal al real.
    while (a < l and b < r):
        if(iz[a] <= der[b]):
            array[k] = iz[a]
            a += 1
        else:
            array[k] = der[b]
            b += 1
        k += 1

#Evita repeticiones en los arreglos de ambos lados, y agrega elementos faltantes.
    while(a<l):
        array[k] = iz[a]
        a += 1
        k += 1

    while(b<r):
        array[k] = der[b]
        b += 1
        k += 1

#Define una función recursiva que toma un arreglo, el índice de su primer elemento,
#y el índice de su último elemento, partiendo el arreglo en dos creando un índice que indica
#la mitad del arreglo, y llamando la función recursivamente para un arreglo del inicio a la mitad, y
#otro de la mitad al último elemento.

def MergeSort(array, pri, ult):
    if (pri < ult):
#Operación matemática que evita overflow
        mitad = (pri+ult-1)//2
#Recursión
        MergeSort(array, pri, mitad)
        MergeSort(array, mitad+1, ult)
#Llamar la otra función dentro de esta función con los valores actualizados de cada recursión.
        Merger(array, pri, mitad, ult)

#Binary Search, siguiendo la temática de Divide and Conquer, coge un número entero dado y lo busca
#en un arreglo ya sorteado, en este caso, por Merge Sort, partiendo el arreglo en izquierda o
#derecha usando comparaciones de mayor o menor

def BinarySearch(array, iz, der, obj):

    if(iz<=der):

        mit = (iz+der)//2

        if(array[mit] == obj):
            return mit
        #Si el medio es menor que el objetivo, esta a la derecha
        elif(array[mit] < obj):
            return BinarySearch(array, mit + 1, der, obj)
        #Si el medio es mayor que el objetivo, esta a la izquierda
        elif(array[mit] > obj):
            return BinarySearch(array, iz, mit - 1, obj)
        
    else:
        print("El elemento no esta presente en el arreglo.")
        return 'null'

#Crear un arreglo de números cualesquiera de tamaño indefinido como entradas del usuario.
arreglo = []
while(True):
    try:
        dato = input("Deme una cantidad de numeros enteros, ponga N para acabar: ")
        if(dato.lower() == 'n'):
            break
        dato = int(float(dato))
        arreglo.append(dato)
    except:
        print("Asegúrese que los números sean enteros.")

print("El arreglo antes de la organización: ", arreglo)
MergeSort(arreglo, 0, len(arreglo)-1)
print("El arreglo después de la organización: ", arreglo)

while(True):
    try:
        bus = input("Entre un número para buscarlo en el arreglo construido, ponga N para parar de buscar: ")
        if(bus.lower() == 'n'):
            print("Gracias por utilizar este programa.")
            break
        busca = int(float(bus))
        ind = (BinarySearch(arreglo, 0, len(arreglo)-1, busca))
        if(ind != 'null'):
            print(f"El número {busca} está en el índice {str(ind)}")
    except:
        print("Asegúrese que el número a buscar sea entero como el arreglo.")