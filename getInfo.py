def test(string):
	if string == "" or string == " ":return(False)
	else:return(True)

def testDate(l):
	value = False

	if 0 in l or l == []:
		print("O valor do Dia/Mês/Ano não pode ser 0 ou vazio.")
		
	elif len(l) != 3:
		print("Faltou informar algum(uns) valor(es).")

	elif l[0] > 31 or l[0] < 1:
		print("O valor do Dia não pode ser maior que 31 ou menor que 1.")

	elif l[1] > 12 or l[1] < 1:
		print("O valor do Mês não pode ser maior que 12 ou menor que 1.")

	elif len(str(l[2])) != 4:
		print("O valor do Ano precisa ter 4 digitos.")

	else:
		value=True

	return(value)

def main():
	while True:
		origem = input("Qual a cidade de Origem?: ")
		origem = origem.capitalize()

		if test(origem): break
		print("Não deixe o campo vazio!")

	while True:
		destino = input("Qual a cidade de Destino?: ")
		destino = destino.capitalize()
		if test(destino): break
		print("Não deixe o campo vazio!")

	while True:
		data = input("Qual a data de partida? Ex: DD/MM/AAAA: ")
		try:
			data = [int(c) for c in data.split("/")]
			if testDate(data): break

		except:
			print("Digite apenas valores numéricos!")

	while True:
		assento = int(input("Qual o Assento? 1-100 "))
		if assento > 0 or assento < 101: break
		else:
			print("Insira um número de 1 a 100.")
	return(origem,destino,data,assento)