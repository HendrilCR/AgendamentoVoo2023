def wrap(lista):
	with open("dados.txt","a") as file:
		string = ""

		for i in range(len(lista)):
			string += str(lista[i])

			if i != len(lista)-1:
				string+=","
			else:
				string+="-"
		file.write(string)

def unwrap():
	file = open("dados.txt","a")
	file.close()
		
	with open("dados.txt","r") as fil:

	    data = fil.read()
	    dataHeaders = data.split("-")
	    del(dataHeaders[-1])
	        	
	    temp = []
	        	
	    for i in dataHeaders:
	        tempData = i.split(",")
	        temp.append([a for a in tempData])
	            	
	    dataHeaders = []
	    dataHeaders = [b for b in temp]
	        	
	    return(dataHeaders)

def ler(voo):
	data = str(voo[2])+"/"+str(voo[3])+"/"+str(voo[4])

	print("-"*30)
	print("ORIGEM:",voo[0])
	print("DESTINO:",voo[1])
	print("DATA:",data)
	print("H. CHEGADA:",voo[5])
	print("H. PARTIDA:",voo[6])
	print("ASSENTO:",voo[7])
	print("NOME:",voo[8])
	print("PASSAPORTE:",voo[9])
	print("-"*30)