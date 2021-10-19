# Aula de Estrutura de Repetição
lista = [1,2,3,4,5,6,7,8]

for conteudoLista in lista:# peque o conteudo da lista
    print(conteudoLista)

print(' fim de programa')

# dados com variedades diferentes 
for i in range (5):
  print(i)

lista1 = [1,2,3,4,5,6,7,8,9] 
lista2 = [1,2,3,4,5]
for i in range (5):
    print(i,lista1[i+4],lista2[i])


lista1 = [1,2,3,4,5,6,7,8,9] 
lista2 = [1,2,3,4,5]
for i in range (4,-1,-2):
   print(i,lista1[i+4],lista2[i])

listaGenerica = [1,1.4, 'Raquel',
                [1,2,'Felipe',],
              {'chave':'conteudo'}]   
for conteudoLista in listaGenerica:
  print(conteudoLista)

listaRange = range (5)
print(listaRange)
for i in range(5):

 print(listaGenerica)

listaGenerica[0]
listaGenerica[1]
listaGenerica[2]

dadosDeIMU = {'head':[1,2,3,4,5,],
              'spine_01':[1,2,3,4,5,], 
              'calf_r':[1,2,3,4,5,6,7,8,9]}
for chave in dadosDeIMU:
 print(dadosDeIMU[chave])


comidas= ['maçã', 'banana','chocolate']
bebidas = ['água','café','suco'] 
for comida, bebida in zip (comidas,bebidas):
  print(comida,bebida)

#repetição condicional

#condição verdadeira #while repetir semmpre que é verdadeira

condição = True
condição= bool(int (input('digite 0 ou 1\n')))
while condição :
  print('entrou a condição é verdadeira')
  condição= bool(int (input('digite 0 ou 1\n')))

contador = 0
while contador <5:
 print(contador)
contador = contador +1
contador+=1


#quanto eu quero interroper #acabar

contador = 0
while contador <=5:
 print(contador)
 contador+=1
 if contador >3:break


#para parar de executar uma tarefa #parar

dados_covid= [[1,2,3,4,5,6],[7,8,9,10,0,1]]
contador =0
while contador <2:
  if dados_covid [contador]==10:
    contador+=1
    continue
  print(dados_covid[contador]) 
  contador +=1
  
