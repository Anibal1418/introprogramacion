#Contar Vocales

def vocalcount(word):
    listvocal = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in word:
        if letter.lower() in listvocal:
            count += 1
    return count

palabra = input("Deme una palabra cualquiera: ")
print(f"El numero de vocales en '{palabra}' es {vocalcount(palabra)}.")