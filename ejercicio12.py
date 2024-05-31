#Leer dos números enteros y 
#si la diferencia entre los dos números es par mostrar en pantalla: 
#la suma de los dígitos de los números, 
#si dicha diferencia es un número primo menor que 10 entonces 
#mostrar en pantalla el producto de los dos números y 
#si la diferencia entre ellos terminar en 4 
#mostrar en pantalla todos los dígitos por separado.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

res = abs(num1 - num2)

sumdig = 0
num1m = num1
num2m = num2
resnum = 1

while (resnum != 0):
  sumdig += (int(num1m % 10) + int(num2m % 10))
  num1m = int(num1m / 10)
  num2m = int(num2m / 10)
  resnum = num1m + num2m
  
if(res % 2 == 0):
  print(f"La suma de los digitos de {num1} y {num2} es: {int(sumdig)}")

if(res<10 and (res == 2 or res == 3 or res == 5 or res == 7)):
  print(f"El producto de {num1} y {num2} es: {int(num1 * num2)}")

resnum2 = 1
num1mm = num1
num2mm = num2

if(res % 10 == 4):
  while (resnum2 != 0):
    print("digitos: ", num1mm%10, " ", num2mm%10)
    num1mm = int(num1mm / 10)
    num2mm = int(num2mm / 10)
    resnum2 = num1mm + num2mm