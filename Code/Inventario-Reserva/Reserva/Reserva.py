import mysql.connector
from mysql.connector import errorcode
import zmq
import json
from ReservaConnection import Connection
from ReservaDA import ReservaDA

class Reserva:

	def __init__(self):
		super(Reserva, self).__init__()
		
	# Metodo que recibe un objeto json con el requerimiento
	# nombre y cantidad
	def reservarPedido(reqJson):
		try:
			# Conecta con la BD usando la configuración del diccionario config
			cnx = Connection.getConnection()
			#ReservaDA.setReserva(cnx, reqJson)
			ReservaDA.doReserva(cnx, reqJson)
			# Devuelve True si todo sale bien
			return True
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)

			# Devuelve False si hay error
			return False
		else:
			# Cierra la conexion
			cnx.close()
			print("... Conexión cerrada.")
