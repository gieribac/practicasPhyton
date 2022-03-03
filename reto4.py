
def buscar_max(Lista, index_):
    pos_max=0
    max_=0
    for i in range(0,len(Lista)-1):
        if Lista[i][index_]>=Lista[pos_max][index_]:
            pos_max=i
            max_=Lista[i][index_] 
        product=Lista[pos_max][0]
    return  product, max_
    
def buscar_min(Lista, index_):
    pos_min=len(Lista)-1
    min_=0
    for i in range(len(Lista)-1,0,-1):
        if Lista[i][index_]<=Lista[pos_min][index_]:
            pos_min=i
            min_=Lista[i][index_] 
        product=Lista[pos_min][0]
    return product, min_

def filtro_so(lista,so):
    list_f=[]
    for i in range(0,len(lista)):
        if lista[i][2]==so:
            list_f.append(lista[i])
    return list_f

def filtro_product(lista,product):
    list_f=[]
    for i in range(0,len(lista)):
        if lista[i][0]==product:
            list_f.append(lista[i])
    return list_f

productos = [["Acrobat",256000,"Windows"],["Xampp",125000,"Windows"],["Xcode",235800,"Mac"],["Fedora",468000,"Linux"],["Zafari",0,"Mac"],["Ubuntu",287000,"Linux"]]
win_products=filtro_so(productos,"Windows")
linux_products=filtro_so(productos,"Linux")
mac_products=filtro_so(productos,"Mac")
producto_xcode=filtro_product(mac_products,"Xcode")
mac_producto=producto_xcode[0][0]
mac_valor=producto_xcode[0][1]
product_p_max_win, p_maximo_win=buscar_max(win_products,1)
product_p_min_linux, p_min_linux=buscar_min(linux_products,1)
print(win_products)
print(linux_products)
print(f'windows, precio máximo: {product_p_max_win, p_maximo_win}')
print(f'linux, precio minimo: {product_p_min_linux, p_min_linux}')
print(f'mac, producto Xcode: {mac_producto, mac_valor}')
lista_final=[[product_p_max_win, p_maximo_win],[product_p_min_linux, p_min_linux],[mac_producto, mac_valor]]
print(f'lista final: {lista_final}')
