import mysql.connector
from mysql.connector import errorcode
import zmq
import json
from Reserva import Reserva

def getStringFromBytes(jsonBytes):
	print("Getting bytes... Returning string...\n")
	return jsonBytes.decode("utf-8")

def getJsonFromString(jsonString):
	print("Getting string... Returning json (dict)...\n")
	return json.loads(jsonString)

def getStringFromJson(jsonDict):
	print("Getting string... Returning json (dict)...\n")
	return json.dumps(jsonDict)

def getJsonFromBytes(jsonBytes):
	print("Getting bytes... Returning json (dict)...\n")
	jsonDict = json.loads(jsonBytes.decode("utf-8"))
	return jsonDict

#############################################
##### ----- Esto se va a ejecutar ----- #####
#############################################

dirInventario = "tcp://*:5052"

# Creo contexto para la comunicación con Inventario
ctxtInv = zmq.Context()
scktInv = ctxtInv.socket(zmq.REP)
scktInv.bind(dirInventario)

print("*** MÓDULO DE RESERVA ***")

while True:
	print("Esperando solicitudes...\n")
	# Se recibe la lista de jsons, en forma de string
	jsonStr = scktInv.recv_string()
	# Se convierte ese string en una lista de jsons
	jsonLst = getJsonFromString(jsonStr)

	print("> Requerimiento recibido.")

	# Llamo al método reservar y almaceno el resultado en correcto
	correcto = Reserva.reservarPedido(jsonLst)

	# Devuelve un mensaje que depende de correcto
	if (correcto):
		msj = "Solicitud reservada exitosamente."
		print("> Reserva exitosa.")
	else:
		msj = "Error ocurrido al procesar la solicitud. Por favor, intente nuevamente."
		print("> Reserva no procesada.")

	# Envía el mensaje
	scktInv.send_string(msj)
