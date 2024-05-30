#Determina si un nombre tiene 3 vocales o más, si es asi, imprime el nombre


vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

i = 0

word = input("Deme un nombre: ")

for letter in word:
  if letter in vocales:
    i+=1

if i >= 3:
  print(word)
else:
  print("Su nombre no tiene 3 vocales")
