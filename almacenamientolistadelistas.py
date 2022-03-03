"""algoritmo para almacenar una lista de listas 
y ordenarla segun determinado indice de sublista"""
def burbuja(unaLista,p):
    for i in range(len(unaLista)):
        for j in range(len(unaLista)):
            if unaLista[i][p]<unaLista[j][p]:
                unaLista[i], unaLista[j]=unaLista[j], unaLista[i]
no_students=int(input('Ingresar la cantidad de  estudiantes: '))
t_students=[]
unalista=0
for k in range(1,no_students+1):
    student=[]
    print(f'Estudiantes {k}: ')
    name=input(f'Ingrese el nombre del estudianttocue {k}: ')
    age=int(input(f'Ingresar la edad del  estudiante {k}: '))
    student.append(name)
    student.append(age)
    t_students.append(student)
print(t_students)
burbuja(t_students,1)
print(t_students)
