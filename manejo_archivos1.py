#Abreir archico y leerlo
def leer():
    f=open('miprimerarchivo.txt','r')
    messaje=f.read()
    print(messaje)
    f.close()

#abrir archivo y guardar escribir al principio
def escribir_principio():
    f=open('miprimerarchivo.txt','a+')
    f.write('\n'+'Julie')#con el salto de linea lo hace al final
    f.close()

def escribir_final(nombre,edad,tel):
    f=open('miprimerarchivo.txt','a+')
    f.write(f'\n{nombre}\n{edad}\n{tel}') #con el salto de linea lo hace al final
    f.close()

#borra lo contenido en el archivo antes de escribir en él
def borrar():
    f=open('miprimerarchivo.txt','w')
    f.write('')#con el salto de linea lo hace al final
    f.close()

def principal():
    ingresar='y'
    while True:
        if ingresar=='y':
            nombre=input('ingrese nombre: ')
            edad=input('ingrese edad: ')
            tel=input('Ingrese telefono: ')
            escribir_final(nombre,edad,tel)
            g=input('desea ingresar un registro?[Y/N]: ')
            ingresar=g.lower()
        else:
            break
    leer()

principal()



