import mysql.connector
from mysql.connector import errorcode
import zmq
import json
from InventarioConnection import Connection
from InventarioDA import InventarioDA

class Inventario:

	def __init__(self):
		super(Inventario, self).__init__()
	
	## Método que recibe un objeto json con el requerimiento
	## {nombre, cantidad}
	## Retorna una lista de diccionarios json
	@staticmethod
	def getSuficiente(reqJson):
		try:
			cnx = Connection.getConnection()
			#lstCom = InventarioDA.getComunicados(cnx, reqJson)
			lstCom = InventarioDA.getMensaje(cnx, reqJson)
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

	## Método que recibe un objeto json con el requerimiento
	## {nombre, cantidad}
	## Retorna una lista de diccionarios json
	@staticmethod
	def getConsulta(reqJson):
		try:
			cnx = Connection.getConnection()
			lstCom = InventarioDA.getMensaje(cnx, reqJson)
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

	## Recibe un json (diccionario)
	## Y decide si se reserva el bloque o no
	@staticmethod
	def getReservar(lstDicc):
		reservar = True
		for dicc in lstDicc:
			reservar = reservar and (dicc["dif"] >= 0)
		print("\n> Se reserva: " + str(reservar) + "\n")
		return reservar
	## Fin de getReservar()

	## Recibe el json (diccionario)
	## Recibe la dirección y puerto "localhost:port"
	## Y envía el json a la dirección
	@staticmethod
	def sendJson(resJson, dirPort):
		print("\n> Enviando a " + resJson["destino"])
		# Convierto el json en cadena
		resp = json.dumps(resJson)
		# Aquí reservo ps, papi
		ctxtRes = zmq.Context()
		scktRes = ctxtRes.socket(zmq.REQ)
		scktRes.connect(dirPort)

		# Se envía a Reserva
		scktRes.send_string(resp)

		# Se recibe el poderoso mensaje
		msj = scktRes.recv()
		print(msj)
		return msj
	## Fin de sendReserva()
## Fin de la clase Inventario
