import json
import zmq
from Inventario.objeto import Message, Pedido

## PRUEBA DEL NUEVO JSON

## Es necesario pasarle una lista de diccionarios al Message
## para que se pueda convertir a json
req = []
req.append(Pedido(-1, "Prod004", 18, 0, 0.0).__dict__)
req.append(Pedido(-1, "Prod005", 18, 0, 0.0).__dict__)
req.append(Pedido(-1, "Prod006", 18, 0, 0.0).__dict__)
req.append(Pedido(-1, "Prod007", 18, 0, 0.0).__dict__)

mss = Message("Prueba", "Inventario", "12345678", req, False)

print("Objeto: ")
print(mss)

print("Req: ")
print(req)
print(type(req))

print("json: ")
jsonStr = json.dumps(mss.__dict__)
print(jsonStr)
print(type(jsonStr))

print("\nAHORA AL REVES\n")

jsonDict = json.loads(jsonStr)
print("jsonDict: ")
print(jsonDict)
print(type(jsonDict))
campo = jsonDict["pedidos"]
print(campo)
print(type(campo))
subCampo = campo[3]["nombre"]
print(subCampo)
print(type(subCampo))


dirPrueba = "tcp://localhost:9092"
ctxtPrueba = zmq.Context()

#  Socket to talk to server
print("Connecting to Inventario server…")
scktPrueba = ctxtPrueba.socket(zmq.REQ)
scktPrueba.connect(dirPrueba) # 35.184.155.202 
#scktInv.connect("tcp://34.123.133.9:9092")

#scktInv.send_json(jsonObj)
scktPrueba.send_string(jsonStr)

message = scktPrueba.recv()
print(message)
#print(json.dumps(json.loads(message), indent=4))

