n=int(input('Enter a integer number: '))
cube=0
while cube**3 < abs(n):
    cube+=1
if cube**3 != abs(n):
    print(n,' is not a perfect cube')
else: 
    if n<0:
        cube=-cube
        print('cube root ', n, 'is',cube)