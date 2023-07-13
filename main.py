#Código feito por Hêndril Cordeiro Ribeiro - 2023

from gerarVoo import gen
import getInfo
from os import system,name
import dataHandler as dh

arquivoVoos = dh.unwrap()

if name == "nt":  #Importa a função para limpar a tela no caso de ser Windows e Linux
	def clear():
		system("cls")
else:
	def clear():
		system("clear")

clear()

def criarVoo():
	info = getInfo.main()
	listaVoos = gen(info)

	a = 0
	for voo in listaVoos:
		a += 1
		print(a,"-",end=" ")
		print("ORIGEM:",voo[0],end=" ")
		print("| DESTINO:",voo[1],end=" ")
		print("| DATA:",str(voo[2])+"/"+str(voo[3])+"/"+str(voo[4]),end="\n")
		print("| H. PARTIDA:",voo[5],end=" ")
		print("| H. CHEGADA:",voo[6],end="")
		print("| ASSENTO:",voo[7],end="\n")
		print("")

	v = int(input("Qual voo você deseja?: "))
	vooEscolhido = listaVoos[v-1]
	vooEscolhido.append(input("Qual o seu nome completo?: "))
	vooEscolhido.append(input("Qual o número do seu passaporte?: "))
	

	dh.wrap(vooEscolhido)

	arquivoVoos = dh.unwrap()

	dh.ler(arquivoVoos[-1])

while True:
	op = int(input("O que deseja fazer?\n1- Agendar Voo\n2- Checar lista de resevas\n"))
	clear()
	if op == 1:
		criarVoo()
	if op == 2:
		for a in arquivoVoos: 
			dh.ler(a)



