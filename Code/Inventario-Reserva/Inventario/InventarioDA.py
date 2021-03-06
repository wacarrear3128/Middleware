import mysql.connector
from mysql.connector import errorcode
from objeto import Mensaje, Message, Pedido

class InventarioDA:

	def __init__(self):
		super(InventarioDA, self).__init__()

	## Para devolver la lista de objetos Comunicado correspondientes de una
	## conn (conexión a base de datos) y un
	## reqJson (lista de jsons)
	@staticmethod
	def getComunicados(conn, reqJson):
		cursor = conn.cursor()
		# Declaro la lista donde guardaré los objetos Suficiente
		lstCom = []

		for json in reqJson:
			# Armo la consulta a ejecutar
			query = ("SELECT FK_id_prd, stock, p.prc_prd FROM tb_stock AS s JOIN tb_productos AS p ON p.id_prd = s.FK_id_prd WHERE p.nom_prd = '%s'" % json["nombre"])
			# Ejecuto la consulta
			cursor.execute(query)

			# Recorro la consulta para recuperar los valores devueltos
			for x in cursor.fetchall():
				id_prd = x[0]
				stock = x[1]
				prc_prd = x[2]

			# Armo el objeto Suficiente con los datos devueltos pos la consulta
			objCom = Mensaje(id_prd, json["nombre"], json["cantidad"], (stock - json["cantidad"]), (prc_prd * json["cantidad"]), json["dni"])
			print("Stock: " + str(stock)+ " --> Cantidad: " + str(json["cantidad"]) + " --> DNI: " + str(json["dni"]))

			# Esto imprime si el stock alcanza para satisfacer el pedido
			if(objCom.dif < 0):
				print("Suficiente: no")
			else:
				print("Suficiente: sí")

			# Agrego el objeto Suficiente a la lista que devolveré al final
			lstCom.append(objCom.__dict__)

		# Cierra el cursor
		cursor.close()
		# Devuelve la lista de Comunicados
		return lstCom
	## Fin getComunicados()

	@staticmethod
	def getMensaje(conn, reqJson):
		cursor = conn.cursor()
		# Declaro la lista donde guardaré los objetos Suficiente
		lstPed = []
		reservar = True

		for json in reqJson["pedidos"]:
			query = ("SELECT FK_id_prd, stock, p.prc_prd FROM tb_stock AS s JOIN tb_productos AS p ON p.id_prd = s.FK_id_prd WHERE p.nom_prd = '%s'" % json["nombre"])

			cursor.execute(query)

			for x in cursor.fetchall():
				id_prd = x[0]
				stock = x[1]
				prc_prd = x[2]

			objPed = Pedido(id_prd, json["nombre"], json["cantidad"], (stock - json["cantidad"]), (prc_prd * json["cantidad"]))
			print("Stock: " + str(stock)+ " --> Cantidad: " + str(json["cantidad"]) + " --> DNI: " + str(reqJson["dni"]))

			# Esto imprime si el stock alcanza para satisfacer el pedido
			if(objPed.diferencia < 0):
				print("Suficiente: no")
				reservar = False
			else:
				print("Suficiente: sí")

			lstPed.append(objPed.__dict__)

		# Cierra el cursor
		cursor.close()

		reqJson["pedidos"] = lstPed
		reqJson["reservar"] = reservar

		# Devuelve la lista de Comunicados
		return reqJson
	## Fin getMensaje()