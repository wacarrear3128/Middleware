import mysql.connector
from mysql.connector import errorcode
import zmq
from objeto import Requerimiento, Reserva, Comunicado
import json
from InventarioConnection import Connection
from InventarioDA import InventarioDA

## Método que recibe un objeto json con el requerimiento
## {nombre, cantidad}
## Retorna una lista de diccionarios json
def getSuficiente(reqJson):
	try:
		cnx = Connection.getConnection()
		lstCom = InventarioDA.getComunicados(cnx, reqJson)
		return lstCom
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		# Cierra la conexion
		cnx.close()
		print("> Conexión a la bd: cerrada.")
## Fin de getSuficiente()

def getReservar(lstDicc):
	reservar = True
	for dicc in lstDicc:
		reservar = reservar and (dicc["dif"] >= 0)
	print("\n> Se reserva: " + str(reservar) + "\n")
	return reservar


## Envía el json a Reserva
## Recibe el json (diccionario)
## Recibe la dirección y puerto "localhost:port"
def sendJson(resJson, dirPort):
	print("\n> Enviando a Reserva")
	# Convierto el json en cadena
	resp = json.dumps(resJson)
	# Aquí reservo ps, papi
	ctxtRes = zmq.Context()
	scktRes = ctxtRes.socket(zmq.REQ)
	scktRes.connect("tcp://" + dirPort)

	# Se envía a Reserva
	scktRes.send_string(resp)

	# Se recibe el poderoso mensaje
	msj = scktRes.recv()
	print(msj)
	return msj
## Fin de sendReserva()


#############################################
##### ----- Esto se va a ejecutar ----- #####
#############################################

dirReserva = "34.121.240.130:1050"
dirFacturacion = "34.123.189.222:5555"

# Crea contexto para el módulo del Procesamiendo de Órdenes
ctxtOrd = zmq.Context()
scktOrd = ctxtOrd.socket(zmq.REP)
scktOrd.bind("tcp://*:9092")

print("*** MÓDULO DE INVENTARIO ***")

while True:
	print("Esperando solicitudes...\n")
	# Recibo una cadena con una lista de jsons
	jsonStr = scktOrd.recv()
	print(jsonStr)
	print(type(jsonStr))
	jsonStr = jsonStr.decode("utf-8")
	print(jsonStr)
	print(type(jsonStr))
	# Convierto esa cadena en una lista de jsons
	jsonLst = json.loads(jsonStr)
	# Declaro la lista donde almacenaré la data a devolver
	lstResp = []
	# Declaro un booleano para decidir si reservar o no
	reservar = True

	print("> Solicitud Recibida")

	lstResp = getSuficiente(jsonLst)

	reservar = getReservar(lstResp)
	
	# La respuesta al módulo de órdenes será la lista armada
	# en formato de cadena json
	resp = json.dumps(lstResp)
	scktOrd.send_string(resp)

	if (reservar):
		sendJson(lstResp, dirReserva)
		sendJson(lstResp, dirFacturacion)

	#scktOrd.send_string(msj)
	#print(json.dumps(lstResp, indent = 4) + "\n" + str(type(resp)))

