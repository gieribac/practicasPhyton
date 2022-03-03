def principal():
    try:
        estudiantes=[["Pedro Pérez",1095623458, 4.5],["Carlos García",1098748563,3.3],["Laura Gómez",1095869523,3.5],\
            ["Valentina Díaz",1005478125,4.0],["Arturo Calle",1005632147,4.7],["Lina Bedoya",1095487523,2.5],\
            ["Juan Cacua",1098652485,1.8],["Erika Santana",1065487521,3.9],["Jesús Ríos",1005412589,2.3]]
        resultado=[]
        estudiantes_ordennotas=ordenamiento(estudiantes,2)
        resultado.append(busqueda_lineal(estudiantes_ordennotas,0,"Lina Bedoya"))
        resultado.append(busqueda_binaria(estudiantes_ordennotas,2,3.3))
        print (resultado)
    except:
        print ("error inesperado")

def ordenamiento(unaLista,indice): #Se ordena la lista de forma descendente por indice de sublista (nota)
  intercambios = True
  numPasada = len(unaLista) - 1
  while numPasada > 0 and intercambios:
    intercambios = False
    for i in range(numPasada):
      if unaLista[i][indice] < unaLista[i+1][indice]:
        intercambios = True
        unaLista[i], unaLista[i+1] = unaLista[i+1], unaLista[i]
    numPasada -= 1
  return unaLista

def busqueda_lineal(lista,indice,buscar): #busqueda lineal en la lista con indice de sublista (nombre)
    for i in range(len(lista)):
        if lista[i][indice] == buscar:
            return lista[i]
            break

def busqueda_binaria(unaLista,indice,item): #busqueda binaria descendente con indice de sublista (nota)
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False
    contador = 0
    while primero <= ultimo and not encontrado:
        contador +=1
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio][indice] == item: 
            encontrado = True
            return unaLista[puntoMedio]
        else:
            if item >unaLista[puntoMedio][indice]:
                ultimo = puntoMedio -1
            else:
                primero = puntoMedio + 1

principal()