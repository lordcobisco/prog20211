###REPETIÇÃO CONTADA

Liste = [1,2,3,4,5,6,7,8]
for conteudoLista in Lista: #pegue o conteúdo da lista um a um e coloque na variável conteúdolistta até que você chegue no final da lista.
  print(conteudoLista) 
 

lista1 = [6,7,8,9,1,2,3,4,5]
lista2 = [1,2,3,4,5]
  for i in range(5):  #quando usa essa estrutura, está pegando o I e repetindo o for 5 vezes.
    print(i, lista1[i+4],lista2[i])
    
    
lista1 = [6,7,8,9,1,2,3,4,5]
lista2 = [1,2,3,4,5]
for i in range (4,-1,-2):
  print(i, lista1[i+4],lista2[i]) 

lista1 = [6,7,8,9,1,2,3,4,5]
lista2 = [1,2,3,4,5]
for i in range (3,5,1):
  print(i, lista1[i+4],lista2[i]) 


listaGenerica = [1,1.4, 'thiago', 
                [1,2,'anderson'],
                {'chave':'conteuudo'}]
for conteudoLista in listaGenerica:
  print(conteudoLista)
  
print('Fim de programa)
      
listaRange = range(5)
      print(listaRange)
conteudoLista = listaGenerica[i]
      print(conteudoLista)
  
  
dadosDeIMU = {'head':[1,2,3,4,5]
             'spine_01': {1,2,3,4,5]
             'calf_r': [1,2,3,4,5,6,7,8,9]}
for chave in dadosDeIMU:
  print(chave, dadosDeIMU[chave])
print ('Fim de programa')


covid = {'Brasil': 
          {'Nordeste': 
            {'RN':
              {'macaíba':
                {'ObitosAcumulados':{1,2,3,4,5,6,7,8,9]
                }
              }
            }
          }
        }
                        
for regiao in covid{'Brasil'}
print[regiao]
  for estados in covid['Brasil'][regiao]:
  print (estado)
  
  
comidas = ['bacon','fritas','picanha']
bebidas = ['cerveja','refri','suco']
for comida, bebida in zip(comidas,bebidas):
  print(comida,bebida)
         

###REPETIÇÃO CONDICIONAL

while True:
         print('Entrou pq a condição é verdadeira')
         
condição = bool(int(input('Digite 0 ou 1"\n))):
while condição:
  print('Entrou pq a condição é verdadeira')
  condição = bool(int(input('Digite 0 ou 1"\n)))
         
condição = bool(int(input('Digite 0 ou 1"\n))):
while not condição:
  print('Entrou pq a condição é verdadeira')
  condição = bool(int(input('Digite 0 ou 1"\n)))
         
         
contador = 0
while contador < 5:
  print(contador)
  #contador = contador + 1
  contador +=1
  if contador == 3:
    break #significa sair de uma estrutura de repetição, interromper a estrutura de repetição.

dados_covid = [[1,2,3,4,5,6,7,8,9,10,0,1]]
contador = 0
while contador < 2:
  if sum(dados_covid[contador]) >= 25:
  contador +=1
  continue
print(dados_covid[contador])
contador +=1
if contador < 2:
    break #significa sair de uma estrutura de repetição, interromper a estrutura de repetição.
                            
                            
             
                            
                            
                            








