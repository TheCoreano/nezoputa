class Anotacao:
	def __init__(self, titulo, data, descricao, pk):
		self.titulo = titulo
		self.data = data
		self.descricao = descricao
		self.pk = pk

	def obj2CSV(self):
		return self.titulo + ";"+ self.data + ";" + self.descricao + ";" + str(self.pk)+";\n"

	def csv2OBJ(self, linha):
		aux = linha.strip().split(";")
		return Anotacao(aux[0], aux[1], aux[2], int(aux[3]))

	def __repr__(self):
		return self.titulo