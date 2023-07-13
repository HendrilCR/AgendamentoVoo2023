from random import randint
import getInfo

def genHora(n):
    
    lista = []
    
    for i in range(n):
        a = randint(0,23)
        b = randint(0,59)
        
        temp,temp2 = [str(a),":",str(b)],""
        
        if a < 10:
            temp.insert(0,"0")
        if b < 10:
            temp.insert(-1,"0")
        
        for x in temp:
            temp2+= x
        
        lista.append(temp2)

    return(sorted(lista))

def gen(info):
    voos = []
    for baluga in range(5):
        temp = []
        temp.append(info[0])
        temp.append(info[1])

        for k in info[2]:
            temp.append(k)

        hora = genHora(2)

        for k in hora:
            temp.append(k)

        temp.append(info[3])

        voos.append(temp)
        

    return(voos)
    