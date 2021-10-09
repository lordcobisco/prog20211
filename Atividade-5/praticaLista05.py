# lista=[]
# print(lista)

listaFase1 = ["BRASIL",1,"ARGENTINA",2,"URUGUAI",3,"EUA",4]
listaFase2 = ['CHINA', 1,'FRANÇA',2,'ALEMANHA',3]
# print(lista[0])
# print(lista[1])
# print(lista[3])
print('\n')
listaFase1.append("EGITO")
listaFase2.append("AFRICA DO SUL")

listaFase1.extend(listaFase2)

for elementoLista in listaFase1:
    print("Ordem da Lista:  \n",elementoLista)

# listaFase1.pop(4) #retira o elemento da lista de acordo com o index apontado
# print(listaFase1)
# listaFase1.remove("EUA") # remove o elemento da lista de acordo com o valor apontado
# print(listaFase1)
# listaFase1.sort()#ordena de forma crescente os elementos da lista
# print(listaFase1)
# listaFase1.reverse()#ordena de forma descrente os elementos da lista
# print(listaFase1)
# #Operações com listas
# print('Concatenado: ',listaFase1+listaFase1)#concatenação com +
# print(len(listaFase1))
# print(listaFase1*2)#mostrando o conteúdo da lista duas vezes

listaFase1=listaFase2#passei o end. da lista 2 para a lista 1
print('O endereço das listas são iguais? ',listaFase1 is listaFase2)#o endereço de uma lista é igual a da outro lista
print('O contéudo das listas são iguais? ', listaFase1==listaFase2)
listaFase1.append("COREIA")
print(listaFase2)
# print(listaFase1==listaFase2)
# print(listaFase1 is listaFase2)

#criando tupla com um item
thisTuple = ("Casa",)
print(type(thisTuple))