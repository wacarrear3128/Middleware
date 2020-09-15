# Para empacar lo que llega del módulo de Operaciones
# tiene nombre de producto
# y cantidad que se desea reservar
class Requerimiento:

	def __init__(self, nombre = "", cantidad = 0, dni = ""):
		self.nombre = nombre
		self.cantidad = cantidad
		self.dni = dni


# Para comunicarme con Cxc
class Cuentas:

	def __init__(self, nom, mnt):
		self.nom = nom
		self.mnt = mnt


# Para saber si hay stock suficiente de un objeto
# tiene id de producto
# dif es la diferencia entre el stock y la cantidad requerida
class Mensaje:

	def __init__(self, idp, nom, cnt, dif = 0, cst = 0, dni = ""):
		self.idp = idp
		self.nom = nom
		self.cnt = cnt
		self.dif = dif
		self.cst = cst
		self.dni = dni
