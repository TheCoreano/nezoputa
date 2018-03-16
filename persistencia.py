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
			anotacao = Anotacao(aux[0], aux[1], aux[2], int(aux[3]))
			vet.append(anotacao)
		arq.close()
		return vet

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