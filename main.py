import sys
import os
from persistencia import *
from anotacao import *

'''print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")'''

if __name__ == '__main__':

	adao = AnotacaoDAO()
	cont = 1
	while(1):
		op = input("Escolha: (1) Adicionar, (2) Listar, (3) Excluir, (4) Ir para lixeira (0) Sair ")
		if(op == 1):
			titulo = raw_input("Titulo: ")
			data = raw_input("Data (dd/mm/aaaa): ")
			desc = raw_input("Descricao: ")
			pk = cont
			an = Anotacao(titulo,data,desc,pk)
			adao.adicionar(an)
		elif(op == 2):
			vet = adao.listar()
			for n in vet:
				print n.titulo + " - " + n.data + " - " + n.descricao + " - " + str(n.pk) +"\n"	

		elif(op == 3):
			pk = input("Digite o id da anotacao: ")
			question = raw_input("Excluir permanentemente (s/n): ")
			if(question == "s"): adao.excluir(pk)
			else:
				adao.lixeira(pk)
				print("Anotacao movida para a lixeira")
		elif (op == 0): break
		elif(op == 4):
			while(1):
				x = input("Lixeira: (1) Restaurar, (2) Listar, (0) Voltar ")
				if(x == 1):
					pk = input("Digite o id da anotacao: ")
					adao.restaurar(pk)
				if(x == 2 ):
					vet = adao.listarLixeira()
					for aa in vet:
						print aa.titulo + " - " + aa.data + " - " + aa.descricao + " - " + str(aa.pk) +"\n"	
				if(x == 0): break;	
		cont = cont + cont