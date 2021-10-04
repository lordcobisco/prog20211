'''
Atividade contextualizada 05 - Tainá
'''
#Planilha COVID 2021/2 - Semana 36

#Listas com estados escolhidos
lista_estado = ['PA', 'RN', 'CE', 'PB', 'PE', 'AL', 'BA', 'SP', 'RJ', 'MG']
lista_populacao = [8602865, 3506853, 9132078, 4018127, 9557071, 3337357, 14873064, 45919049, 17264943, 21168791]
lista_casosacum = [585403, 365683, 933490, 435822, 610740, 236777, 1224174, 4291993, 1137927, 2081186]
lista_casosnov = [12, 131, 171, 93, 443, 173, 195, 1534, 334, 590]
lista_obitosacum = [16506, 7282, 24065, 9217, 19469, 6106, 26577, 146567, 63243, 53323]
lista_obitosnov = [2, 1, 0, 5, 7, 5, 5, 18, 9, 0]

#Tuplas com estados escolhidos
tupla_estado = ('PA', 'RN', 'CE', 'PB', 'PE', 'AL', 'BA', 'SP', 'RJ', 'MG')
tupla_populacao = (8602865, 3506853, 9132078, 4018127, 9557071, 3337357, 14873064, 45919049, 17264943, 21168791)
tupla_casosacum = (585403, 365683, 933490, 435822, 610740, 236777, 1224174, 4291993, 1137927, 2081186)
tupla_casosnov = (12, 131, 171, 93, 443, 173, 195, 1534, 334, 590)
tupla_obitosacum = (16506, 7282, 24065, 9217, 19469, 6106, 26577, 146567, 63243, 53323)
tupla_obitosnov = (2, 1, 0, 5, 7, 5, 5, 18, 9, 0)

dadosCOVID = [lista_estado, lista_populacao, lista_casosacum, lista_casosnov, lista_obitosacum, lista_obitosnov]
dadosCOVID_tupla = (tupla_estado, tupla_populacao, tupla_casosacum, tupla_casosnov, tupla_obitosacum, tupla_obitosnov)

#RJ - Casos Acumulados
if 'RJ' in dadosCOVID [0]:
    print ('Quantidade de casos acumulados no Rio de Janeiro: ', dadosCOVID[2][8])
if 'RJ' in dadosCOVID_tupla [0]:
    print ('Quantidade de casos acumulados no Rio de Janeiro: ', dadosCOVID_tupla[2][8])

#Óbitos acumulados nos estados - listas
print (dadosCOVID[0][0], dadosCOVID [4][0])
print (dadosCOVID[0][1], dadosCOVID [4][1])
print (dadosCOVID[0][2], dadosCOVID [4][2])
print (dadosCOVID[0][3], dadosCOVID [4][3])
print (dadosCOVID[0][4], dadosCOVID [4][4])
print (dadosCOVID[0][5], dadosCOVID [4][5])
print (dadosCOVID[0][6], dadosCOVID [4][6])
print (dadosCOVID[0][7], dadosCOVID [4][7])
print (dadosCOVID[0][8], dadosCOVID [4][8])
print (dadosCOVID[0][9], dadosCOVID [4][9])
#Óbitos acumulados nos estados - tuplas
print (dadosCOVID_tupla[0][0], dadosCOVID_tupla [4][0])
print (dadosCOVID_tupla[0][1], dadosCOVID_tupla [4][1])
print (dadosCOVID_tupla[0][2], dadosCOVID_tupla [4][2])
print (dadosCOVID_tupla[0][3], dadosCOVID_tupla [4][3])
print (dadosCOVID_tupla[0][4], dadosCOVID_tupla [4][4])
print (dadosCOVID_tupla[0][5], dadosCOVID_tupla [4][5])
print (dadosCOVID_tupla[0][6], dadosCOVID_tupla [4][6])
print (dadosCOVID_tupla[0][7], dadosCOVID_tupla [4][7])
print (dadosCOVID_tupla[0][8], dadosCOVID_tupla [4][8])
print (dadosCOVID_tupla[0][9], dadosCOVID_tupla [4][9])

#Sobrescrever dados de óbitos novos na PB
if 'PB' in dadosCOVID[0]:
    dadosCOVID[5][3] += 10
    print ('Dados corrigidos com sucesso. Óbitos novos na Paraíba: ', dadosCOVID[5][3])
    print ('Lista atualizada de óbitos novos: ', dadosCOVID[5])

#Não é possível realizar mudança na tupla, por ser imutável
# if 'PB' in dadosCOVID_tupla[0]:
#     dadosCOVID_tupla[5][3] += 10
#     print ('Dados corrigidos com sucesso. Óbitos novos na Paraíba: ', dadosCOVID_tupla[5][3])
#     print ('Tupla atualizada de óbitos novos: ', dadosCOVID_tupla[5])

#Estado escolhido: Pará (10 municípios selecionados)
municipioPA = ['Abaetetuba', 'Altamira', 'Ananindeua', 'Barcarena', 'Belém', 'Benevides', 'Bragança', 'Breves', 'Cametá', 'Castanhal']
regiaoPA = ['Tocantins', 'Xingu', 'Metropolitana I', 'Tocantins', 'Metropolitana I', 'Metropolitana I', 'Rio Caetes', 'Marajó II', 'Tocantins', 'Metropolitana III']
populacaoPA = [157698, 114594, 530598, 124680, 1492745, 62737, 127686, 102701, 137890, 200793]
casosacumPA = [9298, 14125, 25625, 11827, 105806, 4102, 4210, 4083, 9826, 9311]
casosnovPA = [0, 0, 0, 0, 9, 0, 0, 0, 0, 0]
obitosacumPA = [224, 306, 822, 238, 5108, 105, 174, 120, 266, 474]
obitosnovPA = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

dadosCOVID_PA = [municipioPA, regiaoPA, populacaoPA, casosacumPA, casosnovPA, obitosacumPA, obitosnovPA]

dadosCOVID.append(dadosCOVID_PA)  #dados PA acrescentados
print(dadosCOVID)

dadosCOVID_PA.remove(regiaoPA)  #regiões removidas
print(dadosCOVID_PA, dadosCOVID)

#Soma de dados
somaPA = [sum(dadosCOVID_PA[1]), sum(dadosCOVID_PA[2]),sum(dadosCOVID_PA[3]), sum(dadosCOVID_PA[4]), sum(dadosCOVID_PA[5])]

if (somaPA[0] == dadosCOVID[1][0]):
    if(somaPA[1] == dadosCOVID[2][0]):
        if(somaPA[2] == dadosCOVID[3][0]):
            if(somaPA[3] == dadosCOVID[4][0]):
                if(somaPA[4] == dadosCOVID[5][0]):
                    print("As somas são iguais.")

#Tamanho da lista
print ("Tamanho da lista: ", len(dadosCOVID))

#Maior e menor número de óbitos novos
print (dadosCOVID[5])
print ('O menor número de óbitos novos foi de ', min(dadosCOVID[5]), ' pessoas.')
print ('O maior número de óbitos novos foi de ', max(dadosCOVID[5]), ' pessoas.')

#Dicionário