def fecha():
     try:
          day=int(input("Ingrese día: "))
          month=int(input("Ingrese mes: "))
          year=int(input("Ingrese año: "))
          
          if month<1 or month>12:
               print("Fecha inválida: Mes inválido")
          elif day<1 or day>31:
               print("Fecha inválida: Día inválido")
          elif day==31:
               month31=(1, 3, 5, 7, 8, 10, 12)
               if month not in month31:
                    print("Fecha inválida: El mes no tiene 31 días")
          elif day>29 and month==2:
               print(f'Fecha inválida: El mes no puede tener {day} días')
          elif day==29 and month==2 and year%4!=0:
               print("Fecha inválida: El dia y mes no corresponden porque el año no es bisiesto")
          else:
               print("Fecha válida")
     except ValueError:
          error()
                         
def primo():
     try:
          num=int(input("Ingrese un número: "))
          if num<0:
               print(f'El número {num} no es número primo')
          else:
               acumulador=0
               for k in range(2,num):
                    acumulador+=num%k==0
               validar="es" if acumulador==0 else "no es"
               print(f'El número {num} {validar} número primo')
     except ValueError:
          error()

def cifras():
     try:
          num=int(input("Ingrese un número: "))
          validar=num
          acumular=0
          while validar>0:
               acumular+=1
               validar=num-10**acumular
          print (f'El número {num} tiene {acumular} cifras')
     except ValueError:
          error()

def error():
	print("Oops, entrada invalida, sólo se permiten números enteros positivos. Intente de nuevo")

while True:
     print("Seleccione una Opción")
     try:
          option=int(input(" 1: Ingresar fecha en formato numerico para corroborar su existencia. \
               \n 2: Ingrese un número para saber si es primo o nó. \n 3: Ingrese un número y sepa cuántas cifras tiene. \
               \n 4: Finalice el programa. \n Opción: "))

          if option==4:
               print("Gracias por utilizar este programa")
               break
          else:
               switch_option={1:fecha, 2:primo, 3:cifras}
               switch_option.get(option, error)()
     except ValueError:
          print("Oops, entrada invalida, sólo se permiten números enteros. Intente de nuevo")
     