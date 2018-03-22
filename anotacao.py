from datetime import datetime
class Anotacao:
	def __init__(self, titulo, descricao,data,pk):
		self.titulo = titulo
		self.descricao = descricao
		self.data = data
		self.pk = pk

	def obj2CSV(self):
		return self.titulo + ";" + self.descricao + ";" + self.data + ";" + str(self.pk)+";\n"

	def csv2OBJ(self, linha):
		aux = linha.strip().split(";")
		return Anotacao(aux[0], aux[1], aux[2], int(aux[3]))

	def __repr__(self):
		return self.titulo