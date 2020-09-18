import mysql.connector
from mysql.connector import errorcode

class ReservaDA:

	def __init__(self):
		super(ReservaDA, self).__init__()
	

	@staticmethod
	def setReserva(conn, reqJson):
		# Crea un cursor para actualizar la tabla stock y un string con la consulta a ejecutar
		cursor = conn.cursor()

		for json in reqJson:
			# Armo la consulta
			query = ("UPDATE tb_stock SET stock = stock - %d WHERE FK_id_prd = %d" % (json["cnt"], json["idp"]))
			# Ejecuto la consulta armada
			cursor.execute(query)

		# Para cometer los cambios
		conn.commit()
		# Cierra el cursor
		cursor.close()

	@staticmethod
	def doReserva(conn, reqJson):
		# Crea un cursor para actualizar la tabla stock y un string con la consulta a ejecutar
		cursor = conn.cursor()

		for json in reqJson["pedidos"]:
			# Armo la consulta
			query = ("UPDATE tb_stock SET stock = stock - %d WHERE FK_id_prd = %d" % (json["cantidad"], json["idp"]))
			# Ejecuto la consulta armada
			cursor.execute(query)

		# Para cometer los cambios
		conn.commit()
		# Cierra el cursor
		cursor.close()