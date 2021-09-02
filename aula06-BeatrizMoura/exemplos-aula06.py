# -----------------   Aula Repeticoes  ---------------------

#lista = [1,2,3,4,5,6,7,8]

#for conteudoLista in lista: # pega o conteudo da lista 1 a 1 e coloca na variavel conteudoLista ate que se chegue no final da lista
 #   print(conteudoLista)

#print('Fim do programa')


#lista1 = [6,7,8,9,1,2,3,4,5]
#lista2 = [1,2,3,4,5]

#for i in range(5):
 #   print(i, lista1[i+4], lista2[i])

#print('Fim do programa')


#lista1 = [6,7,8,9,1,2,3,4,5]
#lista2 = [1,2,3,4,5]

#for i in range(4, -1,-1):
 #   print(i, lista1[i+4], lista2[i])

#print('Fim do programa')


#listaGenerica = [1,1.4,'bea',1,2,'andre',{'chave':'conteudo'}]

#for conteudoLista in listaGenerica:
 #   print(conteudoLista)

#for i in range(4):
 #   conteudoLista = listaGenerica[i]
  #  print(conteudoLista)

#print('Fim do programa')

#dadosIMU = {'head':[1,2,3,4,5],
 #           'spine_01':[1,2,3,4,5,6],
  #          'calf_R':[1,2,3,4,5,6,7,8,9]}

#for chave in dadosIMU:
 #   print(chave,dadosIMU[chave])

#print('end program')

#covid = {'Brasil':
   #         {'Nordeste':
    #            {'RN':
     #               {'Macaiba':
      #                {'Obitos acumulados': [1,2,3,4,5]
       #               
        #              }
         #           }   
          #      }
           # },
            #'Norte':
             #   {'AM':
              #      {'Manaus':
               #       {'Obitos acumulados': [1,2,3,4,5]
                #      
                 #     }
                  #  }   
                #}
            #
        #}

#for regiao in covid['Brasil']:
 #   print(regiao)
  #  for estados in covid['Brasil'][regiao]:
   #     print(estados)
    

#comidas = ['bacon', 'fritas', 'picanha']
#bebidas = ['cerveja', 'refri','suco']

#for comida, bebida in zip(comidas, bebidas):
 #   print(comidas, bebidas)



#condicao = bool(int(input('Digite 0 ou 1\n')))

#while condicao:
 #   print('entrou pq a condicao eh verdadeira')



#contador=0

#while contador < 5:
 #   print('computador')
  #  #contador = contador + 1
   # contador +=1
    #if contador == 3:
     #   break


dadosCovid = [[1,2,3,4,5,6],[7,8,9,10,0,1]]
contador = 0

 while contador < 2:
    if sum (dadosCovid[contador]) >= 25:
        contador =+1
        continue
    print(dadosCovid[contador])
    contador =+ 1
