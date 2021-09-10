# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 13:46:17 2021

@author: driellevieira
"""

#Atividade Contextualizada 07
#COVID-19

#Estados escolhidos aleatoriamente
#Listas

estadosBrasil = ['ES','RJ','SP','MG','PA','MA','RO','AC','SC','PB']
pop = [4018650, 17264943, 45919049, 21168791, 8602865, 7075181, 1777225, 881935, 7164788, 4018127]
acumulados_casos = [517873,958199,3727348,552937,317446,247607,85556,1052455,396442]
novos_casos = [1108,775,7762,8686,1797,839,202,30,1591,1733]
acumulados_obitos = [11475,55470,127681,46242,15469,9043,6136,1738,16861,8606]
novos_obitos = [13,133,744,281,25,20,5,0,37,20]

#Tuplas

estadosBrasi_tp = ('ES','RJ','SP','MG','PA','MA','RO','AC','SC','PB')
pop_tp = (4018650, 17264943, 45919049, 21168791, 8602865, 7075181, 1777225, 881935, 7164788, 4018127)
acumulados_casostp = (517873,958199,3727348,552937,317446,247607,85556,1052455,396442)
novos_casostp = (1108,775,7762,8686,1797,839,202,30,1591,1733)
acumulados_obitostp = (11475,55470,127681,46242,15469,9043,6136,1738,16861,8606)
novos_obitostp = (13,133,744,281,25,20,5,0,37,20)

dadosCovid = [estadosBrasil, pop, acumulados_casos, novos_casos, acumulados_obitos, novos_obitos]
dadosCovidtp = (estadosBrasi_tp,pop_tp,acumulados_casostp, novos_casostp, acumulados_obitostp, novos_obitostp)

#Rio de Janeiro
#Casos acumulados

if 'RJ' in dadosCovid[0]:
    print("A quantidade de casos acumulados no estado do Rio de Janeiro é de: ", dadosCovid[2][1])

if 'RJ' in dadosCovidtp[0]:
    print("A quantidade de casos acumulados no estado do Rio de Janeiro é de: ",dadosCovidtp[2][1])

#Óbitos acumulados nos estados

print(dadosCovid[0][0], dadosCovid[4][0])
print(dadosCovid[0][1], dadosCovid[4][1])
print(dadosCovid[0][2], dadosCovid[4][2])
print(dadosCovid[0][3], dadosCovid[4][3])
print(dadosCovid[0][4], dadosCovid[4][4])
print(dadosCovid[0][5], dadosCovid[4][5])
print(dadosCovid[0][6], dadosCovid[4][6])
print(dadosCovid[0][7], dadosCovid[4][7])
print(dadosCovid[0][8], dadosCovid[4][8])
print(dadosCovid[0][9], dadosCovid[4][9])

print(dadosCovidtp[0][0], dadosCovidtp[4][0])
print(dadosCovidtp[0][1], dadosCovidtp[4][1])
print(dadosCovidtp[0][2], dadosCovidtp[4][2])
print(dadosCovidtp[0][3], dadosCovidtp[4][3])
print(dadosCovidtp[0][4], dadosCovidtp[4][4])
print(dadosCovidtp[0][5], dadosCovidtp[4][5])
print(dadosCovidtp[0][6], dadosCovidtp[4][6])
print(dadosCovidtp[0][7], dadosCovidtp[4][7])
print(dadosCovidtp[0][8], dadosCovidtp[4][8])
print(dadosCovidtp[0][9], dadosCovidtp[4][9])

#Sobrescrevendo os dados da Paraíba
#Novos óbitos

if 'PB' in dadosCovid[0]:
    dadosCovid[5][9] = dadosCovid[5][9] + 10
    print("Os dados da Paraíba já foram corrigidos")
    print(dadosCovid)

if 'PB' in dadosCovidtp[0]:
    dadosCovidtp[5][9] = dadosCovidtp[5][9] + 10
    print("Os dados da Paraíba já foram corrigidos")
    print(dadosCovidtp)
    
#Os dados da lista foram corrigidos pois eles são mutáveis, na tupla não foi possível a correção
#pois os dados uma vez postos lá não são possíveis de serem mudados.

#Munícipios do Espírito Santo
#Criação de nova lista
#Adição e remoção
#Comparação entre municípios e estado
#Criação de dicionário

municipiosES = ['Afonso Cláudio','Alegre','Alfredo Chaves','Anchieta','Aracruz','Baixo Guandu','Barra de São Francisco','Brejetuba','Cachoeiro de Itapemirim','Cariacica','Castelo','Colatina','Domingos Martins','Ecoporanga','Fundão','Guarapari','Iconha','Jaguaré','João Neiva','Marechal Floriano','Muqui','Nova Venécia','Piúma', 'Santa Leopoldina','Santa Teresa','São Mateus','Serra','Vila Velha','Vitória']
regiaoES = ['Metropolitana','Sul','Sul','Sul','Central','Central','Norte','Metropolina','Sul','Metropolitana','Sul','Central','Metropolitana','Norte','Metropolitana','Metropolitana','Sul','Norte','Central','Metropolitana','Sul','Norte','Sul','Metropolitana','Metropolitana','Norte','Metropolitana', 'Metropolitana']
popES = [30586,30084,14601,29263,101220,30998,44650,12404,208972,381285,37534,122499,33850,22923,21509,124859,13860,30477,16668,16694,15449,50110,21711,12224,23590,130611,517510,493838,362097]
acumulados_casosES = [3405,2416,2407,4788,15823,3476,4741,1641,26398,39930,5881,19142,3837,3294,2589,15847,2615,3633,2649,3295,1907,5613,2609,1116,4218,12191,65385,64279,55059]
novos_casosES = [10,6,7,8,34,15,21,9,42,105,16,27,20,11,6,74,8,8,19,7,2,30,4,3,20,15,89,91,54]
acumulados_obitosES = [56,52,35,86,222,71,192,14,560,1320,115,330,72,64,65,403,19,48,51,50,50,118,77,28,58,253,1383,1570,1197]
novos_obitosES = [0,0,0,0,1,0,0,0,0,3,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,2,0,2]

dadosCovidES = [municipiosES,regiaoES,popES,acumulados_casosES,novos_casosES,acumulados_obitosES,novos_obitosES]

dadosCovid.append(dadosCovidES)
print(dadosCovid)

dadosCovidES.remove(regiaoES)
print(dadosCovid)

somatoriaES = [sum(dadosCovidES[1]),sum(dadosCovidES[2]),sum(dadosCovidES[3]),sum(dadosCovidES[4]),sum(dadosCovidES[5])]

if (somatoriaES[0] == dadosCovid[1][0]):
    if(somatoriaES[1] == dadosCovid[2][0]):
        if(somatoriaES[2] == dadosCovid[3][0]):
            if(somatoriaES[3] == dadosCovid[4][0]):
                if(somatoriaES[4] == dadosCovid[5][0]):
                    print("As somas são iguais.")
                    
print ("O tamanho da lista é: ", len(dadosCovid))

#Valores numéricos de óbitos novos

print (dadosCovid[5])
print ("O número máximo de novos óbitos é: ", max(dadosCovid[5]))
print ("O número mínimo de novos óbitos é: ", min(dadosCovid[5]))

dicionarioES = {'Afonso Cláudio':dadosCovidES[4][0],'Alegre'::dadosCovidES[4][1], 'Anchieta':dadosCovidES[4]][2], 'Aracruz': dadosCovidES[4][3],'Baixo Guandu': dadosCovidES[4][4], 'Barra de São Francisco':dadosCovidES[4][5], 'Brejetuba':dadosCovidES[4][6],'Cachoeiro de Itapemirim':dadosCovidES[4][7],'Cariacica':dadosCovidES[4][8],'Castelo':dadosCovidES[4][9],'Colatina':dadosCovidES[4][10],'Domingos Martins':dadosCovidES[4][11],'Ecoporanga':dadosCovidES[4][12],'Fundão':dadosCovidES[4][13],'Guarapari':dadosCovidES[4][14],'Iconha':dadosCovidES[4][15],'Jaguaré':dadosCovidES[4][16],'João Neiva':dadosCovidES[4][17],'Marechal Floriano':dadosCovidES[4][18],'Muqui':dadosCovidES[4][19],'Nova Venécia':dadosCovidES[4][20],'Piúma':dadosCovidES[4][21],'Santa Leopoldina':dadosCovidES[4][22],'Santa Teresa':dadosCovidES[4][23],'São Mateus':dadosCovidES[4][24],'Serra':dadosCovidES[4][25],'Vila Velha',dadosCovidES[4][26],'Vitória':dadosCovidES[4][27]}
municipio = input("Qual município você deseja saber a quantidade de casos novos?\n")
print("O município: ",municipio,"teve ",dicionarioES[municipio],"novos casos.")
