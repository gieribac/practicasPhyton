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
            contenido=i+contenido
            lista.append([i,0,contenido])
            if (contenido==objetivo): 
                break
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

def areaT(vertices):
    vecUy=vertices[1][1]-vertices[-1][1]
    vecUx=vertices[1][0]-vertices[-1][0]
    vecVy=vertices[0][1]-vertices[-1][1]
    vecVx=vertices[0][0]-vertices[-1][0]
    detx=vecUx*vecVy
    dety=vecUy*vecVx
    area=0.5*(detx**2+dety**2)**0.5
    return(area)

iteracion = 0
n=2
listpx=[]
listpy=[]
avertices=[]
vertices=[]
area=0
while (True):
    cadena = input()
    if (cadena=="*"):
        break
    px, py = hallarpxpy(int(cadena))
    listpx.append(px)
    listpy.append(py)
    for i in range (px-1):
        px, py = hallarpxpy(py)
        listpx.append(px)
        listpy.append(py)
    for i in range (len(listpx)-2):
        avertices.append(listpx[i+1])
    avertices.append(listpx[-1])
    avertices.append(listpy[-1])
    for i in range (len(avertices)):
        vertices.append(hallarpxpy(avertices[i]))
    area=areaT(vertices)
    print (round(area,1))