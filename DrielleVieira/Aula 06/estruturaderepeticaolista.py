# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:34:26 2021

@author: driellevieira
"""

#Aula 06 - Estruturas de repetição

#lista = [1,3,5,7,9]

# for conteudoLista in lista: #repetição contada
#     print (conteudoLista)
    
# print ("Fim do programa")

# lista1 =[1,3,5,7,9,11,13,15,17]
# lista2 = [0,2,4,6,8]

# #for i in range (5):
#     # print(i, lista1[i], lista2[i])
#     # print(i, lista1[i+4], lista2[i])
#     # print (lista1[i])
#     # print (lista2[i])
# #    print (i)
    
# #print ("Fim")

# for i in range (4, 0, -1):
#     print (i, lista1[i], lista2[i])

listastring = [1, 1.5,"Drielle", [2, 3, "Vieira"], {"Chave":"Conteúdo"}]
# for conteudoLista in listastring:
#     print (conteudoLista)
# print ("Fim")

listaRange = range(5)
print(listaRange)

for i in range (5):
    conteudoLista = listastring[i]
    print(listastring[i])
print ("It's Overrrrr")


