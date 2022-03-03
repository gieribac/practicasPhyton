"""el usuario va a escoger una las opciones 1. busqueda lineal 2. busqueda binaria 
3 salir; debe ingresar el numero para realizar la respectiva busqueda, salida mensaje con el 
numero de interacciones. 
utilizar:
-bloque de excepciones
-funciones y metodos
-parametros de funciones o metodos"""
lista = [122,56,7,9,0,3,45,6,23,12,68,67,4]

def ordenar_lista(Lista):
    n=len(Lista)-1
    while n>0:
        p=buscar_max(Lista,0,n)
        Lista[p], Lista[n] = Lista[n], Lista[p]
        print('cambios',p,n,Lista)
        n=n-1

def buscar_max(Lista, ini, fin):
    pos_max=ini
    for i in range(ini+1,fin+1):
        if Lista[i]>Lista[pos_max]:
            pos_max=i
    return pos_max

def B_lineal(list_,buscar):
    print (list_)
    for i in range(len(list_)):
        if list_[i] == buscar:
            return (True,i+1)
            break
    return (False, i+1)

def B_binaria(list_,item):
    ordenar_lista(list_)
    primero = 0
    ultimo = len(list_)-1
    encontrado = False
    contador = 0
    while primero <= ultimo and not encontrado:
        contador +=1
        puntoMedio = (primero + ultimo)//2
        if list_[puntoMedio] == item: 
            encontrado = True
        else:
            if item <list_[puntoMedio]:
                ultimo = puntoMedio -1
            else:
                primero = puntoMedio + 1
    return(encontrado, contador)

def Pedir():
    return (int(input("Ingrese elemento a buscar: ")))
    
def Principal():
    while True:
        try:
            print("Ingrese una de las siguientes opciones:")
            print("1. busqueda lineal \n2. busqueda binaria \n3. salir")
            option=int(input("Seleccione: "))
            if option==1:
                encontrado, pos = B_lineal(lista,Pedir())
                print(f'elemento {encontrado} mediante busqueda lineal, interacciones utilizadas: {pos}')
            elif option==2:
                encontrado, pos = B_binaria(lista,Pedir())
                print(f'elemento {encontrado} mediante busqueda binaria, interacciones utilizadas: {pos}')
            elif option==3:
                print("gracias por utilizar mi software")
                break
        except:
            print("Caracter erroneo")
Principal()
