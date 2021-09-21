for i in range(5):
    print(i)

#####################

for item in range(9,-1,-1):
    print(item)

#####################

for caractere in "André Felipe":
    print(caractere)

#####################

listaNomes = ['Pedro','João','Letícia']

for nome in listaNomes:
    print(nome)

#####################

linguagens = ['Python','PHP','C#','PowerBuilder','Cobol']
tamanho = len(linguagens)
indices = range(tamanho)

for i in indices:
    print(linguagens[i])

####################

for key, value in enumerate(['p','y','t','h','o','n']):
    print(key, value)

####################

linguagens = ['Python','PHP','C#','PowerBuilder','Cobol']

for i, valor in enumerate(linguagens):
    print("Linguagem: "+ valor)
    print("Índice: "+ str(i))

####################

from numpy import random

listaValores = random.rand(10)

for valorIndividual in listaValores:
    print(valorIndividual, "\n")

####################

lista_1 = ['bacon','fritas','picanha']
lista_2 = ['cerveja','refri','suco']

for alimento, bebida in zip(lista_1, lista_2):
    print(alimento, bebida)

###################

listaNomes = ['Pedro','João','Letícia']

for nome in listaNomes:
    print(nome)
else:
    print('Todos os nomes foram listados com sucesso')