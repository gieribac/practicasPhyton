import math
print("CONVERSION DE COORDENADAS EN 2D")
while(True):
    print("Digite [1] si desea convertir coordenadas rectangulares a polares")
    print("Digite [2] si desea convertir coordenadas polares a rectangulares: ")
    opcion=int(input())
    if opcion==1: 
        while(True):
            x=float(input("Ingrese el valor de la abcisa 'x': "))
            y=float(input("Ingrese el valor de la ordenada 'y': "))
            r=math.sqrt(math.pow(x,2)+math.pow(y,2))
            if r==0:
                a=0
            else:
                if y>=0:
                    a=math.acos(x/r)
                else:
                    a=math.acos(x/r)+math.pi
            a=a*180/math.pi
            print("La conversion a coordenadas polares para: ")  
            print(f'x={x}, y={y} es:')
            print(f'radio={r}, angulo={a} gradianes')
            print("Desea seguir convirtiendo a coordenadas polares? y/n: ") 
            o=input()
            if 'y'!=o.lower():
                break
    elif opcion==2:
        while(True):
            a=float(input("Ingrese el valor del angulo en gradianes: "))
            r=abs(float(input("Ingrese el valor del radio: ")))
            a_rad=a*math.pi/180
            x=r*math.cos(a_rad)
            y=r*math.sin(a_rad)
            print("La conversion a coordenadas rectangulares para: ")  
            print(f'radio={r}, angulo={a} gradianes es: ')
            print(f'x={x}, y={y}')
            print("Desea seguior convirtiendo a coordenadas rectangulares? y/n: ")
            o=input()
            if 'y'!=o.lower():
                break
    else:
        print("Opcion invalida")
    print("Especifique si desea seguir(y) o salir(n): ")
    o=input()
    if 'y'!=o.lower():
        break
