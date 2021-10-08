#lista = [1,2,3,4,5,6,7,8]

#for conteudoLista in lista:# pegue o conteudo da lista um a um e coloque na variavel conteudoLista ate que voce chegue no final da lista
    #print(conteudo Lista)
#   print(conteudoLista)

#lista1 = [6,7,8,9,1,2,3,4,5]
#lista2 = [1,2,3,4,5]
#for i in range(3,5,1):
 #   print(i, lista1[i+4],lista2[i])

#print ('fim de programa')

#listaGenérica = [1, 1.4, 'andre', 
 #                [1,2,'felipe'],
 #                {'chave':'conteudo'}]
#for conteudoLista in listaGenerica:
 #   print(conteudoLista)

#listaRange = range(5)
#print(listaRange)
#for i in range(5):
#    conteudoLista = listaGenerica[i]
#    print(conteudoLista)

#print ('fim de programa')

#dadosDeIMU = {'head :[1,2,3,4,5'],
#             'spine_01':[1,2,3,4,5,5],
# 3            'calf_r':[1,2,3,4,5,6,7,8,9]}
# for chave in dadosDeIMU:
#    print(dadosDeIMU[chave])

#print ('fim de programa')

#covi = {'Brasil':
#           {'Nordeste':
#               {'RN':
#                   {'macaiba':
#                       {'Obtosacumulados':[1,2,3,4,5,6,7,8]
#                       }
#                'PB':
#                   {'joão pessoa':
#                       {'Obtosacumulados':[1,2,3,4,5,6,7,8]   
#                   }
#               }
#           'Norte':
#               {'AM':
#                   {'Manaus':
#                       {'Obtosacumulados':[1,2,3,4,5,6,7,8]
#                       }
#                   }
#               }
#           }
#       }
# for regiao in covid['Brasil]
#      print(regioes)
#      for estado in covid['Brasil'[regioes]:
#           print(estado)
#       

# comidas = ['bacon','fritas','picanha']
# bebidas = ['cerveja','refri','suco']
# for comida,bebida in zip(comidas,bebidas):
#     print(comida,bebida)


#condição = bool(int(input('digite 0 ou 1\n')))
#while True:
#    print('Entrou pq a condição é verdadeira')
#    condição = bool(int(input('digite 0 ou 1\n')))

#contador = 0
#while contador < 5:
#    print(contador)
#    contador +=1
#    if contador == 3:
#        break

dados_covid = [[1,2,3,4,5,6],[7,8,9,10,0,1]]
contador = 0
while True:
    if sum(dados_covid[contador]) >= 25:
        contador +=1
        continue
    print(dados_covid[contador])
    contador +=1
    if contador < 2:
        break

