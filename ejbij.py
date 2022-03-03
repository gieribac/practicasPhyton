import math
def hallarpipj(target):
    i=(-1+math.sqrt(1+8*target))//2
    contents=i*(i+1)//2
    j=int(target-contents)
    i=int(i-j)
    return (i,j)
    
print(hallarpipj(30))


