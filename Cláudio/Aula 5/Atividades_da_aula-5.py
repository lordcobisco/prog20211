# lista = [1,2,3,4,5,6,7,8]
# lista = list ([])

# '''
# .Index diz a posição
# .remove tira
# .insert coloca
# .append adiciona em ordem consecutiva
# .reverse ordena em ordem decrescente
# .sort ordena em ordem crescente
# .count diz quantas vezes aquilo se repete
# '''

# for conteudolista in lista: 
#     '''
#     o nome "conteudlista" é o nome da lista,
#     mas você pode colocar o que quiser. 
#     OBRIGATÓRIO TER O FOR O IN E OS :
#     Ele repete o conteúdo pegue o conteúdo da lista
#     '''
#     print (conteudolista)
lista1 = [6,7,8,9,1,2,3,4,5]
lista2 = [1,2,3,4,5]
for i in range (5):
    print (lista1[i+4], lista2[i])

# lista1 = [6,7,8,9,1,2,3,4,5]
# lista2 = [1,2,3,4,5]
# for i in range (4,-1,-1):
#     print (lista1[i+4], lista2[i])

# print ('Fim de programa')

# lista1 = [6,7,8,9,1,2,3,4,5]
# lista2 = [1,2,3,4,5]
# for i in range (4,-1,-2):
#     print (lista1[i+4], lista2[i])

# print ('Fim de programa')

# listagenerica = [1,1.4,'andre',
#                  [1,2,'felipe'],
#                  {'chave' : 'conteudo'}]
# for conteudolista in listagenerica:
#     print (conteudolista)

# for i in range (2):
#      print (listagenerica[i])


# dadosdeIMU = {'head':[1,2,3,4,5],
#               'spine_01':[1,2,3,4,5,5],
#               'calf_r':[1,2,3,4,5,6,7,8,9]}
# for chave in dadosdeIMU:
#     print (chave, dadosdeIMU [chave])

# comidas = ['bacon', 'fritas', 'picanha']
# bebidas = [ 'cerveja', 'refri', 'suco']
# for comida,bebida in zip(comidas,bebidas):
#     print (comida,bebida)
# condicao = bool(int(input('Digite 0 ou 1\n')))

# while condicao: 
#     print ('Entrou pq a condição é verdadeira')
#     condicao = bool(int(input('Digite 0 ou 1\n')))

# contador = 0
# while contador < 5:
#     print (contador)
#     # contador = contador+1
#     contador +=1
#     if contador == 3:
#             break

# dados_covid = [[1,2,3,4,5,6],[7,8,9,10,0,1]]
# contador = 1
# while contador < 2:
#     if sum (dados_covid [contador]) >= 25:
#        contador +=1
#     continue
# print(dados_covid [contador])

# dicionario = {}
# dicionario = dict()
# # dicionario['biblioteca'] = 'Estantes'
# # print (dicionario['biblioteca'])

# dicionario['biblioteca'] = {'Estantes':[1,2,3,4,5,6,7,8], 'livros':[]}
# print (dicionario)
# print (dicionario['biblioteca'])
# print (dicionario ['biblioteca']['Estantes'])
# print (dicionario ['biblioteca']['Estantes'][0])
# print (dicionario.keys())
# print (dicionario['biblioteca'].keys())

# print (dicionario.get('biblioteca'),None)
# print (dicionario.get('Estantes'),None)