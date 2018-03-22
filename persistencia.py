from anotacao import *
import os


class AnotacaoDAO:

	def obter(self, pk):
		vet = self.listar()
		for anotacao in vet:
			if(anotacao.pk == pk): return anotacao


	def listar(self):
		arq = open("banco.txt","r")
		vet = []
		for linha in arq:
			aux = linha.strip().split(";")
			anotacao = Anotacao(aux[0], aux[1], str(aux[2]), int(aux[3]))
			vet.append(anotacao)
		arq.close()
		return sorted(vet, key=lambda obj: obj.data)

	def adicionar(self, anotacao):
		arq = open("banco.txt", "a+")
		arq.write(anotacao.obj2CSV())
		arq.close()	


	def excluir(self, pk):
		vet = self.listar()
		vetAux = []
		for anotacao in vet:
			if (anotacao.pk != pk):
				vetAux.append(anotacao)

		arq = open("banco.txt", "w")
		arq.close()		
		for e in vetAux:
			self.adicionar(e)

	def lixeira(self,pk):
		arq = open("lixeira.txt", "a+")
		vet = self.listar()
		for a in vet:
			if(a.pk == pk):
				arq.write(a.obj2CSV())
		arq.close()
		self.excluir(pk)

	def lixeiraLimpa(self, pk):
		vet = self.listarLixeira()
		vetAux = []
		for anotacao in vet:
			if (anotacao.pk != pk):
				vetAux.append(anotacao)

		arq = open("lixeira.txt", "w")
		arq.close()		
		for e in vetAux:
			self.adicionar(e)

	def listarLixeira(self):
		arq = open("lixeira.txt","r")
		vet = []
		for linha in arq:
			aux = linha.strip().split(";")
			anotacao = Anotacao(aux[0], aux[1], aux[2], int(aux[3]))
			vet.append(anotacao)
		arq.close()
		return vet	
		
	def restaurar(self,pk):
		vet = self.listarLixeira()
		arq = open("banco.txt","a+")
		for a in vet:
			if(a.pk == pk):
				arq.write(a.obj2CSV())
		arq.close()
		self.lixeiraLimpa(pk)

	def alterar(self, anotacao):
		vet = self.listar()
		vetAux = []
		for a in vet:
			if (a.pk == anotacao.pk):
				vetAux.append(anotacao)
			else:
				vetAux.append(a)			
		arquivo = open("banco.txt", "w")
		arquivo.close()		
		for e in vetAux: 
			self.adicionar(e)

	def duplicar(self,anotacao):
		a = self.obter(anotacao.pk)
		an = Anotacao(a.titulo,a.descricao,a.data,a.pk)
		self.adicionar(an)

	def exportar(self):
		meses = ["","janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
		qtdePorMes = [0,0,0,0,0,0,0,0,0,0,0,0,0]
		vet = self.listar()

		for m in meses:
			arquivo = open(m+".txt","w")
			arquivo.close()
			
		for n in vet:
			ab = n.data.split("-")
			mes = int(ab[1])
			qtdePorMes[mes] = qtdePorMes[mes] + 1
			arquivo = open(meses[mes]+".txt","a")
			arquivo.write(n.obj2CSV())
			arquivo.close()

		i = 0
		while i < len(qtdePorMes):
			if (qtdePorMes[i] == 0):
				os.remove(meses[i]+".txt")
			i = i + 1	
		