valores = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,29]
def busqueda_binaria(unaLista,item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False
    contador = 0
    while primero <= ultimo and not encontrado:
        contador +=1
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio] == item: 
            encontrado = True
        else:
            if item <unaLista[puntoMedio]:
                ultimo = puntoMedio -1
            else:
                primero = puntoMedio + 1
    return(encontrado, contador)
numero = int(input('Ingresa el numero a buscar: '))
busqueda, iteraciones = busqueda_binaria(valores, numero)
print(f'el valor encontrado fue {busqueda}​​ y las iteraciones fueron {iteraciones}​​')

def busqueda_lineal(buscar):
    for i in range(len(valores)):
        if valores[i] == buscar:
            return (True,i+1)
            break
            return (False, i+1)
            
buscar = int(input('indica un numero a buscar: '))
conseguido, iteraciones = busqueda_lineal(buscar)
if conseguido:
    print(f'el numero fue encontrado en {iteraciones} iteraciones')
else:
    print(f'el numero no fue encontrado, se realizo {iteraciones} iteraciones')
