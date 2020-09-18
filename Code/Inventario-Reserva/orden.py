import zmq
import json
from Inventario.objeto import Requerimiento, Cuentas, Message, Pedido

dirInventario = "tcp://localhost:9092"
ctxtInv = zmq.Context()

dirCuentas = "tcp://localhost:1051"
ctxtCnt = zmq.Context()

# req = []
# req.append(Requerimiento("Prod001", 10, "12345678").__dict__)
# req.append(Requerimiento("Prod002", 11, "12345678").__dict__)
# req.append(Requerimiento("Prod003", 12, "12345678").__dict__)
# req.append(Requerimiento("Prod004", 13, "12345678").__dict__)
# req.append(Requerimiento("Prod005", 14, "12345678").__dict__)
# req.append(Requerimiento("Prod006", 15, "12345678").__dict__)
# req.append(Requerimiento("Prod007", 16, "12345678").__dict__)
# req.append(Requerimiento("Prod008", 17, "12345678").__dict__)
# req.append(Requerimiento("Prod009", 18, "12345678").__dict__)
# req.append(Requerimiento("Prod010", 19, "12345678").__dict__)
# reqStr = json.dumps(req)
# #jsonObj = json.loads(jsonStr)

# cxc = []
# cxc.append(Cuentas("Yordi Caushi Cueva", 19).__dict__)
# cxcStr = json.dumps(cxc)



## Es necesario pasarle una lista de diccionarios al Message
## para que se pueda convertir a json
req = []
req.append(Pedido(-1, "Prod004", 18, 0, 0.0).__dict__)
req.append(Pedido(-1, "Prod005", 18, 0, 0.0).__dict__)
req.append(Pedido(-1, "Prod006", 18, 0, 0.0).__dict__)
req.append(Pedido(-1, "Prod007", 18, 0, 0.0).__dict__)

mss = Message("Prueba", "Inventario", "12345678", req, False)

reqStr = json.dumps(mss.__dict__)



print("*** MÓDULO DE PROCESAMIENTO DE ÓRDENES ***\n")

#  Socket to talk to server
print("Connecting to Inventario server…")
scktInv = ctxtInv.socket(zmq.REQ)
scktInv.connect(dirInventario) # 35.184.155.202 
#scktInv.connect("tcp://34.123.133.9:9092")

#scktInv.send_json(jsonObj)
scktInv.send_string(reqStr)

message = scktInv.recv()
print(message)
print(json.dumps(json.loads(message), indent=4))



# #  Socket to talk to server
# print("Connecting to Cuentas server…")
# scktCnt = ctxtCnt.socket(zmq.REQ)
# scktCnt.connect(dirCuentas) # 35.184.155.202 
# #scktCnt.connect("tcp://34.123.133.9:9092")

# #scktCnt.send_json(jsonObj)
# scktCnt.send_string(cxcStr)

# message = scktCnt.recv_string()
# print(message)
# #print(json.dumps(json.loads(message), indent=4))

