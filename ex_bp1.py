#hallar numero encriptado
i_row = 3
j_row = 61
objetivo = j_row + i_row
contenido = 0
rango = 0

#lista=[[1,2,3],[4,5,6],[7,8,9]]
i=-1
lista = []
#for i in range (rango+1):
while (i < objetivo):
        i = i + 1
        contenido=i+contenido
        lista.append([i,0,contenido])

rango = objetivo+1

for j in range (1,rango):
    for i in range (rango-j):
        contenido=lista[i+j][2]+j
        lista.append([i,j,contenido])
        if (i==i_row and j==j_row): 
            break
    if (i==i_row and j==j_row): 
            break

print (f'fila: {i}\ncolumna: {j}\ncontenido: {contenido}')


