
# Listas

estados = ['AC', 'PA', 'RR', 'SC', 'MA', 'CE', 'RN','PB','SP', 'RJ']
populacao = [906876, 8777124,625713,7338473,9240580,356903,3365351,46649132,17463349]
casos = [87914,586468,126855,1167047, 352470,934494,366360,436603, 4300644,1159247]
obitos = [1816,16534,1968,19953,10106,24127,7302,9246,147258,63880]

# Tuplas
estados = ('AC', 'PA', 'RR', 'SC', 'MA', 'CE', 'RN','PB','SP', 'RJ')
populacao = (906876, 8777124,625713,7338473,9240580,356903,3365351,46649132,17463349)
casos = (87914,586468,126855,1167047, 352470,934494,366360,436603, 4300644,1159247)
obitos = (1816,16534,1968,19953,10106,24127,7302,9246,147258,63880)

dados_lista = [estados,populacao,casos,obitos]
dados_tupla = (estados,populacao,casos,obitos)


if 'RJ' in dados_lista[0]:
    print("Numero de casos no estado do Rio de Janeiro em lista eh de: ", dados_lista[3][9])

if 'RJ' in dados_tupla[0]:
    print("Numero de casos no estado do Rio de Janeiro eh em tupla eh de: ",dados_tupla[3][9])

# obitos acumulados

print(dados_lista[0][0],dados_lista[3][0])
print(dados_lista[0][1],dados_lista[3][1])
print(dados_lista[0][2],dados_lista[3][2])
print(dados_lista[0][3],dados_lista[3][3])
print(dados_lista[0][4],dados_lista[3][4])
print(dados_lista[0][5],dados_lista[3][5])
print(dados_lista[0][6],dados_lista[3][6])
print(dados_lista[0][7],dados_lista[3][7])
print(dados_lista[0][8],dados_lista[3][8])
print(dados_lista[0][9],dados_lista[3][9])

print(dados_tupla[0][0],dados_tupla[3][0])
print(dados_tupla[0][1],dados_tupla[3][1])
print(dados_tupla[0][2],dados_tupla[3][2])
print(dados_tupla[0][3],dados_tupla[3][3])
print(dados_tupla[0][4],dados_tupla[3][4])
print(dados_tupla[0][5],dados_tupla[3][5])
print(dados_tupla[0][6],dados_tupla[3][6])
print(dados_tupla[0][7],dados_tupla[3][7])
print(dados_tupla[0][8],dados_tupla[3][8])
print(dados_tupla[0][9],dados_tupla[3][9])

# Sobrescrevendo os dados PB

if 'PB' in dados_lista[3]:
    dados_lista[3][7] = dados_lista[3][7] + 10
    print("Os dados da Paraiba foram corrigidos!")
    print(dados_lista)
 
print("Os dados da Paraiba foram corrigidos!")

if 'PB' in dados_tupla[3]:
    dados_tupla[3][7] = dados_tupla[3][7] + 10
    print("Os dados da Paraiba foram corrigidos!")
    print(dados_tupla)
    
#Os dados da lista podem ser corrigidos porque a estrutura permite, no entanto, a tupla nao eh passivel de correcao

# Adicionando o estado do Espirito Santo

municipios_ES = ['Afonso Cláudio','Alegre','Alfredo Chaves','Anchieta','Aracruz','Baixo Guandu','Barra de São Francisco','Brejetuba','Cachoeiro de Itapemirim','Cariacica','Castelo','Colatina','Domingos Martins','Ecoporanga','Fundão','Guarapari','Iconha','Jaguaré','João Neiva','Marechal Floriano','Muqui','Nova Venécia','Piúma', 'Santa Leopoldina','Santa Teresa','São Mateus','Serra','Vila Velha','Vitória']
regiao_ES = ['Metropolitana','Sul','Sul','Sul','Central','Central','Norte','Metropolina','Sul','Metropolitana','Sul','Central','Metropolitana','Norte','Metropolitana','Metropolitana','Sul','Norte','Central','Metropolitana','Sul','Norte','Sul','Metropolitana','Metropolitana','Norte','Metropolitana', 'Metropolitana']
populacao_ES = [30586,30084,14601,29263,101220,30998,44650,12404,208972,381285,37534,122499,33850,22923,21509,124859,13860,30477,16668,16694,15449,50110,21711,12224,23590,130611,517510,493838,362097]
casos_ES = [3405,2416,2407,4788,15823,3476,4741,1641,26398,39930,5881,19142,3837,3294,2589,15847,2615,3633,2649,3295,1907,5613,2609,1116,4218,12191,65385,64279,55059]
obitos_ES = [56,52,35,86,222,71,192,14,560,1320,115,330,72,64,65,403,19,48,51,50,50,118,77,28,58,253,1383,1570,1197]

dados_ES = [municipios_ES,regiao_ES,populacao_ES,casos_ES, obitos_ES]

dados_lista.append(dados_ES)
print(dados_lista)

dados_lista.remove(dados_ES)
print(dados_lista)


# Soma dos dados

soma_ES = (sum(obitos_ES))

print(soma_ES)

'''
if (soma_ES[0] == dados_lista[1][0]):
    if(soma_ES[1] == dados_lista[2][0]):
        if(soma_ES[2] == dados_lista[3][0]):
            if(soma_ES[3] == dados_lista[4][0]):
                    print("As somas sao verdeiras.")
                    
print ("O tamanho da lista: ", len(dados_lista))

#Valores dos óbitos

print (dados_lista[5])
print ("O numero maximo de obitos eh: ", max(dados_lista[4]))
print ("O numero minimo de obitos eh: ", min(dados_lista[4]))

dicionario_ES = {'Afonso Cláudio: ', dados_ES[3][0], 'Alegre:', dados_ES[3][1], 'Anchieta: ',dados_ES[3][2], 'Aracruz:', dados_ES[3][3],'Baixo Guandu:',dados_ES[3][4], 'Barra de São Francisco: ',dados_ES[3][5], 'Brejetuba: ',dados_ES[3][6],'Cachoeiro de Itapemirim:', dados_ES[3][7],'Cariacica:',dados_ES[3][8],'Castelo:', dados_ES[3][9],'Colatina:', dados_ES[3][10],'Domingos Martins:', dados_ES[3][11],'Ecoporanga:', dados_ES[3][12],'Fundão:',dados_ES[3][13],'Guarapari: ', dados_ES[3][14],'Iconha:', dados_ES[3][15],'Jaguaré:',dados_ES[3][16],'João Neiva:', dados_ES[3][17],'Marechal Floriano:', dados_ES[3][18],'Muqui:', dados_ES[3][19],'Nova Venécia: ', dados_ES[3][20],'Piúma: ', dados_ES[3][21],'Santa Leopoldina: ',dados_ES[3][22],'Santa Teresa:',dados_ES[3][23],'São Mateus:',dados_ES[3][24],'Serra:',dados_ES[3][25],'Vila Velha:',dados_ES[3][26],'Vitória:',dados_ES[3][27]}

municipio = input("Digite o nome do município que você deseja saber a quantidade de casos novos?\n")
print("O municipio: ",municipio," registrou ",dicionario_ES[municipio]," casos.")
'''

# Extraindo dados de CE

casos_CE = dados_lista[3][6]

print(' Casos no Ceara:', casos_CE) 