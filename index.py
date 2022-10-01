even = 0
odd = 0

num = int(input("Ingrese un numero entero positivo: "))

while num != 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = int(input("Ingrese un numero entero positivo: "))
    
print("Números pares:", even)
print("Números impares:", odd)

