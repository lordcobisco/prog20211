contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1

##################

condicao = True

while (condicao): #<1>
    print("BLOCO while() e condicao==True") #<2>
    condicao = False #<2>
else:
    print("BLOCO EELSE e condicao==False")

#################

count = 0

while count <= 5:
    print(count)
    count += 1
    if count > 3: break

#################

count = -1

while count < 5:
    count += 1
    if count == 3: continue
    print(count)