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
    vertices=[]
    px, py = hallarpipj(int(cadena))
    tam=px
    listpy.append(py)
    px, py = hallarpipj(py)
    listpx.append(px)
    for i in range (1,tam-2):
        if listpy[-1]!=0 and listpy[-1]!=1:
            if (py!=listpy[-1]):
                px, py = hallarpipj(py)
                listpx.append(px)
                listpy.append(py)
            else:
                listpx.append(py)
    px, py = hallarpipj(py)
    listpx.append(px)
    listpx.append(py)
    for i in range(len(listpx)):
        b=listpx.index(listpx[i])
        if listpx[i] in listpx and b!=i:
            vertices.append(vertices[b])
        else:
            vertices.append(hallarpipj(listpx[i]))
    print (listpx)
    print(f'vertices{vertices}')
    #print (round(areaPoligono(vertices),1))
    # print(f'listpx{listpx}')
    # print(f'listpy{listpy}')
    # print(f'vertices{vertices}')
    area=areaPoligono(vertices)

    #print (avertices)
    #print (vertices)
    print (round(area,1))