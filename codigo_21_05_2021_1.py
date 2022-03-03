"""Leer numeros y guardar en una lista, el proceso de almacenar decide cuando
 el usuario ingrese un numero negativo, finalizar y mostrar:
  el maximo de los numeros y los números pares"""


numeros=[]
pares=[]
thebigboy=[]
n=1 
"""try: 
  numerosp=int(input("ingrese número: "))
except ValueError as e
  print("entrada invalida")"""
while True :
  try: 
    n=int(input("ingrese número: "))
  except ValueError:
    print("la entrada no es valida")
  elif except Except:
    print("Error inesperado")
  else :
    if n>=0 :    
      numeros.append(n)  
      thebigboy=max(numeros)
      if n % 2 ==0:
        pares.append(n)
    else :
      break
print (numeros)
print(f'el maximo de los numeros es {thebigboy}, \nlos numeros pares son {pares}')
