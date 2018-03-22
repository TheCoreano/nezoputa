import sys
import os
from persistencia import *
from anotacao import *

'''print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")'''

if __name__ == '__main__':

	adao = AnotacaoDAO()
	arq = open("banco.txt", "a+")
	arq.close()
	while(1):
		op = input("Anotacao: (1) Adicionar, (2) Listar, (3) Excluir, (4) Alterar, (5) Duplicar, (6) Exportar  (7) Ir para lixeira (0) Sair: ")
		if(op == 1):
			print("---------------- Adicionando Anotacao ----------------")
			titulo = raw_input("Titulo: ")
			data = datetime.now().strftime("%d-%m-%y-%H-%M")
			desc = raw_input("Descricao: ")
			a = adao.listar()
			if(len(a) == 0): pk = 1
			else:
				pk = adao.listar()[-1].pk+1
			an = Anotacao(titulo,desc,str(data),pk)
			adao.adicionar(an)
			print(" >> Adicionada com sucesso" + "\n") 
		elif(op == 2):
			print("---------------- Listando Anotacao ----------------")
			vet = adao.listar()
			for n in vet:
				print "Titulo: " + n.titulo + "  " + "Descricao: " + n.descricao + "  " + "Codigo: " + str(n.pk) + "  " + "Data: " + str(n.data) +"\n"	

		elif(op == 3):
			print("---------------- Excluindo Anotacao ----------------")
			pk = input("Digite o id da anotacao: ")
			question = raw_input("Excluir permanentemente (s/n): ")
			if(question == "s"):
				adao.excluir(pk)
				print(" >> Excluida com sucesso" + "\n")
			else:
				adao.lixeira(pk)
				print(" >> Movida para a lixeira" + "\n")
		elif(op == 4):
			print("---------------- Alterando Anotacao ----------------")
			pk = input("Digite o id da anotacao: ")
			t = raw_input("Novo titulo: ")
			d = raw_input("Nova descricao: ")
			a = adao.obter(pk)
			if(t != ""): a.titulo = t
			if(d != ""): a.descricao = d
			adao.alterar(a)
			print(" >> Alterada com sucesso" + "\n")
		elif(op == 5):
			print("---------------- Duplicando Anotacao ----------------")
			pk = input("Digite o id da anotacao: ")
			a = adao.obter(pk)
			adao.duplicar(a)
			print(" >> Duplicada com sucesso" + "\n")
		elif(op == 6):
			print("---------------- Exportando Anotacoes ----------------")
			adao.exportar()
			print(" >> Exportadas com sucesso")
		elif (op == 0): break
		elif(op == 7):
			while(1):
				x = input("Lixeira: (1) Restaurar, (2) Listar, (3) Excluir (0) Voltar:  ")
				if(x == 1):
					print("---------------- Restaurando Anotacao ----------------")
					pk = input("Digite o id da anotacao: ")
					print(" >> Restaurada com sucesso" + "\n")
					adao.restaurar(pk)
				if(x == 2 ):
					print("---------------- Listando Anotacao ----------------")
					vet = adao.listarLixeira()
					for n in vet:
						print "Titulo: " + n.titulo + "  " + "Descricao: " + n.descricao + "  " + "Codigo: " + str(n.pk) + "  " + "Data: " + str(n.data) +"\n"	
				if(x == 3):
					print("---------------- Deletando Anotacao ----------------")
					pk = input("Digite o id da anotacao: ")
					adao.lixeiraLimpa(pk)
					print(" >> Apagada com sucesso" + "\n")		
				if(x == 0): break;	