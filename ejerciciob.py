import math
def hallarpipj(target):
    i=(-1+math.sqrt(1+8*target))//2
    contents=i*(i+1)//2
    j=int(target-contents)
    i=int(i-j)
    return (i,j)
def areaPoligono(vertices):
    area=0
    for i in range (1,len(vertices)-1):
        vecUy=vertices[i][1]-vertices[0][1]
        vecUx=vertices[i][0]-vertices[0][0]
        vecVy=vertices[i+1][1]-vertices[0][1]
        vecVx=vertices[i+1][0]-vertices[0][0]
        area=area+0.5*math.sqrt((math.pow((vecUx*vecVy-vecUy*vecVx),2)))
    return(area)

while (True):
    cadena = input()
    if (cadena=="*"):
        break
    listpx=[]
    listpy=[]
    avertices=[]
    vertices=[]
    px, py = hallarpipj(int(cadena))
    tam=px-1
    listpx.append(px)
    listpy.append(py)
    for i in range (tam):
        px, py = hallarpipj(py)
        listpx.append(px)
        listpy.append(py)
    for i in range (tam-1):
        avertices.append(listpx[i+1])
        print (avertices)
    avertices.append(listpx[-1])
    print (avertices)
    avertices.append(listpy[-1])
    for i in range (tam+1):
        vertices.append(hallarpipj(avertices[i]))
    area=areaPoligono(vertices)
    print (listpx)
    print (listpy)
    print (avertices)
    print (vertices)
    print (round(area,1))