"""recibir una cadena de caracteres, dónde por medio de una funcion creo una lista
que contiene los caracteres(tener la posibilidad de manipular su construcción), ordenar esa lista de caracteres
-implementar 2 metodos de ordenamiento"""

def burbuja_eficiente(unaLista):
  intercambios = True
  numPasada = len(unaLista) - 1
  while numPasada > 0 and intercambios:
    intercambios = False
    for i in range(numPasada):
      if unaLista[i] > unaLista[i+1]:
        intercambios = True
        unaLista[i], unaLista[i+1] = unaLista[i+1], unaLista[i]
    numPasada -= 1

def ord_seccion(lista):
    n=len(lista)-1
    while n>0:
        p=buscar_max(lista,0,n)
        lista[p],lista[n]=lista[n],lista[p]
        n=n-1

def buscar_max(lista,ini,fin):
    pos_max=ini
    for i in range (ini+1, fin+1):
        if lista[i]>lista[pos_max]:
            pos_max=i
    return pos_max

string_=input('Ingrese una cadena de caracteres: ')
validation=input('Desea especificar un separador?[y/n]: ')
validation.lower()
list_=list(string_) if validation=="n" else string_.split(input('Ingrese separador de la cadena: '))
print(list_)
ordenar=input('Especifique si desea ordenar la lista por primer metodo[1], o por burbuja eficiente[2]: ')
burbuja_eficiente(list_) if ordenar=="2" else ord_seccion(list_)
print(list_)

