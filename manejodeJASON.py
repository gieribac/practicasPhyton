"""leer de json a Json: convertir(parsear) un archivo Json en un diccionario de python import json"""
# jsonData='{"name":"Frank","age":39}'
# leerJson=json.loads(jsonData)
# print(leerJson)

"""construir archivo de Json con python: convertir(codificar) un diccionario de python en un archivo Json"""
# import json
# pyDictionary={"name":"Gio","age":33,"isMarryed":False}
# writeJson=json.dumps(pyDictionary)
# print(writeJson)

"""construir fichero Json"""
import json
datos={}
datos['clientes']=[]
datos['clientes'].append({"name":"Gio","age":33})
datos['clientes'].append({"name":"Julie","age":24})
with open('data.json','w') as file:
    json.dump(datos,file,indent=4)

"""api con json"""
#https://youtu.be/lLsYjzpSDyA
