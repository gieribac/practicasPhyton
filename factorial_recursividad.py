number=int(input('Ingrese un número natural para calcular su factorial: '))
fact=1
def factorial (num):
    fact=1 if num==1 else num*factorial(num-1)
    return fact
print(f'el factorial del número {number} es {factorial(number)}')