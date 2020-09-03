import mysql.connector
from mysql.connector import errorcode
import zmq
from objeto import Comunicado
import json
from ReservaConnection import Connection
from ReservaDA import ReservaDA

# Metodo que recibe un objeto json con el requerimiento
# nombre y cantidad
def reservarPedido(reqJson):
	try:
		# Conecta con la BD usando la configuración del diccionario config
		cnx = Connection.getConnection()
		ReservaDA.setReserva(cnx, reqJson)

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


#############################################
##### ----- Esto se va a ejecutar ----- #####
#############################################

# Creo contexto para la comunicación con Inventario
ctxtInv = zmq.Context()
scktInv = ctxtInv.socket(zmq.REP)
scktInv.bind("tcp://*:1051")

print("*** MÓDULO DE RESERVA ***")

while True:
	print("Esperando solicitudes...\n")
	# Se recibe la lista de jsons, en forma de string
	jsonStr = scktInv.recv()
	# Se convierte ese string en una lista de jsons
	jsonLst = json.loads(jsonStr)
	print("> Requerimiento recibido.")
	# Llamo al método reservar y almaceno el resultado en correcto
	correcto = reservarPedido(jsonLst)

	# Devuelve un mensaje que depende de correcto
	if (correcto):
		msj = "Solicitud reservada exitosamente."
		print("> Reserva exitosa.")
	else:
		msj = "Error ocurrido al procesar la solicitud. Por favor, intente nuevamente."
		print("> Reserva no procesada.")

	# Envía el mensaje
	scktInv.send_string(msj)
