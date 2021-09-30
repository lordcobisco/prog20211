
import csv
import math 
import numpy as np


from numpy import genfromtxt 
my_data = genfromtxt('coletaFlexJoelho.csv', delimiter=',') # acesando os dados

ang =  np.array(my_data) 
print(ang)


list_A = []

for line in ang: # operacao soma

    soma = line[0] + line[1] 
    list_A.append(soma)

print(list_A)


list_B = []

for line in ang: # operacao media

    med = ang.mean() 
    list_B.append(med)

print(list_B)


list_C = []

for line in ang: # operacao menor angulo

    menor = ang.min() 
    list_C.append(menor)

print(list_C)


list_D = []

for line in ang: # operacao maior angulo

    maior = ang.max() 
    list_D.append(maior)

print(list_D)


list_E = []

for line in ang: # operacao de integracao 

    integ = ang.sum() 
    list_E.append(integ)

print(list_E)


list_F = []

for line in ang: # diferenca media

    dif = med - (ang**2)
    div = dif/len(ang)
    list_F.append(div)

print(list_F)


list_G = []

for line in ang: # variacao angular 

    variacao = np.diff(ang)
    list_G.append(variacao)

print(list_G)


list_H = []

for line in ang: # arredondamento 

    roun = np.around(ang, decimals = 3)
    list_H.append(roun)

print(list_H)
