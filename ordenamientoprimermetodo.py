"""solicitar al usuario los limitesde la lista y asignarle numeros aleatorios en el rango con libreria ramdom 
y ordenarla con este metodo"""
"""solicitar al usuario el tamaño de la lista y asignarle numeros aleatorios con libreria ramdom 
y ordenarla con este metodo"""
def principal():
    while True:
        try:
            Lista=[]
            option=input("Digite 1 si desea especificar un rango \nDigite 2 si desea especificar un tamaño de lista\n Digite 3 para salir\nSeleccione: ")
            if option=='1':
                rango_min,rango_max = pedir_limites_rango()
                for k in range (abs(rango_max-rango_min)): Lista.append(random.randint(rango_min,rango_max))
                ordenar_lista(Lista)
                print('LISTA ORDENADA')
                print(Lista)
            elif option=='2':
                tam=pedir_tam_rango()
                for k in range (tam): Lista.append(random.randrange(tam))
                ordenar_lista(Lista)
                print('LISTA ORDENADA')
                print(Lista)
            elif option=='3':
                break
        except:
            print("Ingreso  de datos incorrecto")



import random
def pedir_limites_rango():
    rango_min=int(input('ingrese numero menor del rango a generar para la lista: '))
    rango_max=int(input('ingrese numero mayor del rango a generar para la lista: '))
    return(rango_min,rango_max)

def pedir_tam_rango():
    return(int(input('ingrese el tamaño de la lista deseado: ')))

def ordenar_lista(Lista):
    n=len(Lista)-1
    while n>0:
        p=buscar_max(Lista,0,n)
        Lista[p], Lista[n] = Lista[n], Lista[p]
        n=n-1

def buscar_max(Lista, ini, fin):
    pos_max=ini
    for i in range(ini+1,fin+1):
        if Lista[i]>Lista[pos_max]:
            pos_max=i
    return pos_max

principal()

