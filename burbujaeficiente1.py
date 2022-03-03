def ordenamiento_eficiente(unaLista,ind):
  intercambios = True
  numPasada = len(unaLista) - 1
  while numPasada > 0 and intercambios:
    intercambios = False
    for i in range(numPasada):
      if unaLista[i][ind] > unaLista[i+1][ind]:
        intercambios = True
        unaLista[i], unaLista[i+1] = unaLista[i+1], unaLista[i]
    numPasada -= 1
  return unaLista




unaLista = [['a', 'c'], ['b', 'd','c', 'a'], ['c', 'a']]
numbersList = [[7,1,8,2,9,0,3],[5,12],[6,1]]
l=ordenamiento_eficiente(numbersList,0)

print(l)


