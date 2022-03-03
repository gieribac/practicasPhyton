#dado numero encriptado, hallar vertices
def hallarpxpy(objetivo):
    contenido = 0
    rango = 0
    i=-1
    j=0
    lista = []
    if (objetivo == 0):
        i=0
        j=0
    elif (objetivo == 1):
        i=1
        j=0
    else:
        while (contenido < objetivo):
                i = i + 1
                contenido=i+contenido
                lista.append([i,0,contenido])
        rango = 2*i
        for i in range (objetivo+1,rango):
            if (contenido==objetivo): 
                break
            contenido=i+contenido
            lista.append([i,0,contenido])
        if (contenido!=objetivo):
            for j in range (1,rango):
                for i in range (rango-2-j):
                    contenido=lista[i+j][2]+j
                    lista.append([i,j,contenido])
                    if (contenido==objetivo): 
                        break
                if (contenido==objetivo): 
                    break
    return (i,j)


a,b=hallarpxpy(61)
print(f'{a}\n{b}')
