import json
datos={}
datos['clientes']=[]
datos['clientes'].append({"name":"Gio","age":33})
datos['clientes'].append({"name":"Julie","age":24})
with open('data.json','w') as file:
    json.dump(datos,file,indent=4)