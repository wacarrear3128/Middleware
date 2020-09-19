import mysql.connector
from mysql.connector import errorcode
from Inventario import Inventario
import zmq
import json

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

def setDestino(jsonDict, destino):
	jsonDict["origen"] = "Inventario"
	jsonDict["destino"] = destino
	return jsonDict

#############################################
##### ----- Esto se va a ejecutar ----- #####
#############################################

#dirReserva = "34.121.240.130:1050"
dirReserva = "tcp://localhost:1052"
dirFacturacion = "tcp://localhost:5555"
dirOrdenes = "tcp://*:9092"

# Crea contexto para el módulo del Procesamiendo de Órdenes
ctxtOrd = zmq.Context()
scktOrd = ctxtOrd.socket(zmq.REP)
scktOrd.bind(dirOrdenes)

print("*** MÓDULO DE INVENTARIO ***")

while True:
	print("Esperando solicitudes...\n")
	# Recibo un flujo de bytes con una lista de jsons
	jsonBts = scktOrd.recv()
	# Convierto el flujo de bytes en el json
	jsonLst = getJsonFromBytes(jsonBts)

	print("> Solicitud Recibida")

	lstResp = Inventario.getSuficiente(jsonLst)
	#reservar = Inventario.getReservar(lstResp)
	reservar = lstResp["reservar"]
	
	# La respuesta al módulo de órdenes será la lista armada
	# en formato de cadena json
	lstResp = setDestino(lstResp, "Ordenes")
	resp = getStringFromJson(lstResp)
	scktOrd.send_string(resp)

	if (reservar):
		lstResp = setDestino(lstResp, "Reserva")
		Inventario.sendJson(lstResp, dirReserva)
		lstResp = setDestino(lstResp, "Facturacion")
		Inventario.sendJson(lstResp, dirFacturacion)
		#Inventario.sendJson(lstResp, dirFacturacion)
