#halla el area de un poligono irregular o irregular a partir de sus vertices
def areaPoligono(vertices):
    area=0
    for i in range (1,len(vertices)-1):
        vecUy=vertices[i][1]-vertices[0][1]
        vecUx=vertices[i][0]-vertices[0][0]
        vecVy=vertices[i+1][1]-vertices[0][1]
        vecVx=vertices[i+1][0]-vertices[0][0]
        areat=0.5*((vecUx*vecVy-vecUy*vecVx)**2)**0.5
        area=area+areat
    return(area)

#print(areaPoligono([(1, 1), (2, 0), (0, 0)]))



vertices=[(1, 1), (2, 0), (0, 0)]
print(areaPoligono(vertices))

