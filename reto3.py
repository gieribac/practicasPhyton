"""Se necesita un programa que les permita ingresar los datos de los vendedores que tienen, el total de
 sus ventas anuales y el valor de la comisión ganada por las ventas (la comisión es de 10% para ventas 
 mayor al millon de pesos, de 20% para ventas mayores a los 3 millones y del 25% para ventas mayores 
 a los 5 millones de pesos), cada dato en una lista independiente respectivamente.

Despues de ingresar todos los datos y tener las listas llenas, el usuario del sistema debe poder realizar
 las siguientes acciones a través de un menú que el programa le va a mostrar:

1.	Saber cual es el vendedor con el mayor total de ventas, se debe mostrar cuanto monto vendio
    y el nombre del vendedor, así como el valor ganado por comisión.
2.	Saber cual fue el total de ventas de toda la empresa y el total pagado en comisiones.
3.	Saber cual es el vendedor con el menor total de ventas, se debe mostrar cuanto monto vendio
    y el nombre del vendedor, así como el valor ganado por comisión. """

cant_sellers=int(input('Ingresar la cantidad de  vendedores: '))
sellers_name=[]
annual_sales=[]
sales_commission=[]
for k in range(1,cant_sellers+1):
    print(f'Vendedor {k}: ')
    name_seller=input(f'Ingrese el nombre del vendedor {k}: ')
    sellers_name.append(name_seller)
    annual_sale_seller=float(input(f'Ingrese la cantidad la suma de las ventas anuales de {name_seller}: '))
    annual_sales.append(annual_sale_seller)
    if 3e+6>annual_sale_seller>=1e+6:
        sales_commission.append(annual_sale_seller*0.1)
    elif 5e+6>annual_sale_seller>=3e+6:
        sales_commission.append(annual_sale_seller*0.2)    
    elif annual_sale_seller>=5e+6:
        sales_commission.append(annual_sale_seller*0.25)
    else:
        sales_commission.append(0)  

print(sellers_name,annual_sales,sales_commission) 
the_best_sales=max(annual_sales)
index_best=annual_sales.index(the_best_sales)
the_worst_sales=min(annual_sales)
index_worst=annual_sales.index(the_worst_sales)
total_sales=sum(annual_sales)
total_commissions=sum(sales_commission)
print(f'\nSeller with the highest total sales: {sellers_name[index_best]}')
print(f'Annual sales: {the_best_sales}')
print(f'Commission earned: {sales_commission[index_best]} \n')
print(f'Saller with the lowest total sales: {sellers_name[index_worst]}')
print(f'Annual sales: {the_worst_sales}')
print(f'Commission earned: {sales_commission[index_worst]} \n')
print(f'Total company sales: {total_sales}')
print(f'Total commissions paid: {total_commissions}')

