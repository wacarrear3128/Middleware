import zmq
import json
from Inventario.objeto import Objeto, Requerimiento, Cuentas


context = zmq.Context()

req = []
req.append(Requerimiento("Prod001", 10, "12345678").__dict__)
req.append(Requerimiento("Prod002", 11, "12345678").__dict__)
req.append(Requerimiento("Prod003", 12, "12345678").__dict__)
req.append(Requerimiento("Prod004", 13, "12345678").__dict__)
req.append(Requerimiento("Prod005", 14, "12345678").__dict__)
req.append(Requerimiento("Prod006", 15, "12345678").__dict__)
req.append(Requerimiento("Prod007", 16, "12345678").__dict__)
req.append(Requerimiento("Prod008", 17, "12345678").__dict__)
req.append(Requerimiento("Prod009", 18, "12345678").__dict__)
req.append(Requerimiento("Prod010", 19, "12345678").__dict__)

reqStr = json.dumps(req)
#jsonObj = json.loads(jsonStr)

print("*** MÓDULO DE PROCESAMIENTO DE ÓRDENES ***\n")

# #  Socket to talk to server
# print("Connecting to Inventario server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:9092") # 35.184.155.202 
# #socket.connect("tcp://34.123.133.9:9092")

# #socket.send_json(jsonObj)
# socket.send_string(reqStr)

# message = socket.recv()
# print(message)
# print(json.dumps(json.loads(message), indent=4))



cxc = []
cxc.append(Cuentas("Yordi Caushi Cueva", 19).__dict__)

cxcStr = json.dumps(cxc)
#  Socket to talk to server
print("Connecting to Cuentas server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1050") # 35.184.155.202 
#socket.connect("tcp://34.123.133.9:9092")

#socket.send_json(jsonObj)
socket.send_string(cxcStr)

message = socket.recv()
print(message)
#print(json.dumps(json.loads(message), indent=4))

