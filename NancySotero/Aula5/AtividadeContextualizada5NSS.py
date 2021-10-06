#Atividade Contextualizada 5

#Fazer download manual - arquivo csv
    #Arquivo HIST_PAINEL_COVIDBR_2021_Parte1

#Criar lista e tupla com arquivos
#Região, Estado, regiaoSaude, semanaEpi, populacao, casosAcumulado, casosNovos, obitosAcumulado, obitosNovos

listaDados = ['Brasil', 'Brasil', 'GERAL', 53, 210147125, 7700578, 24605, 195411, 462, 
'Norte', 'RO', 'ZONA DA MATA', 53, 22945, 1291, 3, 16, 0,
'Norte', 'RO', 'CONE SUL', 4, 5312, 364, 0, 9, 0,
'Norte', 'AC', 'ALTO ACRE', 22, 7417, 1644,	4, 24, 0,
'Norte', 'AM', 'RIO NEGRO E SOLIMOES', 2, 97377, 4754, 28, 184, 2,
'Norte','AM', 'REGIONAL PURUS', 4, 19426, 1831, 6, 13, 0,
'Norte','PA', 'BAIXO AMAZONAS', 20, 34109, 3326, 1, 42, 0,
'Norte', 'PA', 'XINGU', 3, 114594, 6681, 77, 137, 0,
'Norte','AP', 'AREA CENTRAL', 8, 7780, 1158, 0, 6, 0,
'Norte', 'RR', 'CENTRO NORTE', 14, 11290, 433, 0, 24, 0,
'Norte', 'TO', 'AMOR PERFEITO', 19, 1112, 113, 0, 1, 0,
'Nordeste',	'MA', 'CAXIAS', 3, 26532, 947, 0, 11, 0,
'Nordeste',	'MA', 'CHAPADINHA', 6, 46440, 589, 0, 10, 0,
'Nordeste', 'PI', 'VALE DO SAMBITO', 4, 3951, 65, 0, 1,	0,
'Nordeste', 'PI', 'COCAIS', 19, 8329, 473, 0, 9, 0,
'Nordeste', 'CE', '5 REGIAO CANINDE', 13, 19691, 775, 5, 25, 0,
'Nordeste', 'RN', '3A REGIAO DE SAUDE - JOAO CAMARA', 2, 73497, 1043, 2, 50, 0,
'Nordeste', 'RN', '6 REGIAO DE SAUDE - PAU DOS FERROS', 16, 3579, 218, 0, 6, 0,
'Nordeste', 'PB',	'7A REGIAO', 3, 18982, 811, 0, 12, 0,
'Nordeste', 'PE', 'RECIFE', 21, 99990, 2677, 6, 197, 0,
'Nordeste', 'PE', 'PETROLINA', 1, 18908, 811, 1, 3, 0,
'Nordeste', 'AL', '7A REGIAO DE SAUDE', 16, 24219, 994, 2, 16, 0,
'Nordeste', 'SE', 'LAGARTO', 1, 104408, 3579, 12, 104, 2,
'Nordeste', 'BA', 'FEIRA DE SANTANA', 7, 25102, 1149, 8, 20, 0,
'Nordeste', 'BA', 'SANTO ANTONIO DE JESUS', 20, 4058, 350, 0, 6, 0,
'Sudeste', 'MG', 'UBERLANDIA / ARAGUARI', 17, 6869, 1591, 17, 22, 0,
'Sudeste', 'MG', 'ITAJUBA', 24, 14459, 775, 0, 28, 0,
'Sudeste', 'RJ', 'METROPOLITANA', 23, 162485, 3413, 10, 432, 4,
'Sudeste', 'RJ', 'CENTRO-SUL', 11, 18614, 1206, 0, 4, 0,
'Sudeste', 'ES', 'SUL', 12, 208972, 19632, 51, 377, 2,
'Sudeste', 'SP', 'ALTA SOROCABANA', 4, 4166, 119, 0, 4, 0,
'Sudeste', 'SP', 'BAURU', 10, 5735, 277, 0, 3, 0,
'Sul', 'PR', '19A RS JACAREZINHO', 9, 3860, 202, 1, 4, 0,
'Sul', 'SC', 'EXTREMO OESTE', 22, 2428,	260, 3, 3, 0,
'Sul', 'RS', 'REGIAO 30', 20, 34116, 3407, 6, 69, 0,
'Centro-Oeste',	'GO', 'SERRA DA MESA', 26, 46388, 3930, 1, 81, 1,
'Centro-Oeste',	'MT', 'TELES PIRES', 7, 13705, 1186, 0, 15,	0,
'Centro-Oeste', 'MS', 'DOURADOS', 14, 9110, 111, 0, 3, 0,]

tuplaDados = ('Brasil', 'Brasil', 'GERAL', 53, 210147125, 7700578, 24605, 195411, 462, 
'Norte', 'RO', 'ZONA DA MATA', 53, 22945, 1291, 3, 16, 0,
'Norte', 'RO', 'CONE SUL', 4, 5312, 364, 0, 9, 0,
'Norte', 'AC', 'ALTO ACRE', 22, 7417, 1644,	4, 24, 0,
'Norte', 'AM', 'RIO NEGRO E SOLIMOES', 2, 97377, 4754, 28, 184, 2,
'Norte','AM', 'REGIONAL PURUS', 4, 19426, 1831, 6, 13, 0,
'Norte','PA', 'BAIXO AMAZONAS', 20, 34109, 3326, 1, 42, 0,
'Norte', 'PA', 'XINGU', 3, 114594, 6681, 77, 137, 0,
'Norte','AP', 'AREA CENTRAL', 8, 7780, 1158, 0, 6, 0,
'Norte', 'RR', 'CENTRO NORTE', 14, 11290, 433, 0, 24, 0,
'Norte', 'TO', 'AMOR PERFEITO', 19, 1112, 113, 0, 1, 0,
'Nordeste',	'MA', 'CAXIAS', 3, 26532, 947, 0, 11, 0,
'Nordeste',	'MA', 'CHAPADINHA', 6, 46440, 589, 0, 10, 0,
'Nordeste', 'PI', 'VALE DO SAMBITO', 4, 3951, 65, 0, 1,	0,
'Nordeste', 'PI', 'COCAIS', 19, 8329, 473, 0, 9, 0,
'Nordeste', 'CE', '5 REGIAO CANINDE', 13, 19691, 775, 5, 25, 0,
'Nordeste', 'RN', '3A REGIAO DE SAUDE - JOAO CAMARA', 2, 73497, 1043, 2, 50, 0,
'Nordeste', 'RN', '6 REGIAO DE SAUDE - PAU DOS FERROS', 16, 3579, 218, 0, 6, 0,
'Nordeste', 'PB',	'7A REGIAO', 3, 18982, 811, 0, 12, 0,
'Nordeste', 'PE', 'RECIFE', 21, 99990, 2677, 6, 197, 0,
'Nordeste', 'PE', 'PETROLINA', 1, 18908, 811, 1, 3, 0,
'Nordeste', 'AL', '7A REGIAO DE SAUDE', 16, 24219, 994, 2, 16, 0,
'Nordeste', 'SE', 'LAGARTO', 1, 104408, 3579, 12, 104, 2,
'Nordeste', 'BA', 'FEIRA DE SANTANA', 7, 25102, 1149, 8, 20, 0,
'Nordeste', 'BA', 'SANTO ANTONIO DE JESUS', 20, 4058, 350, 0, 6, 0,
'Sudeste', 'MG', 'UBERLANDIA / ARAGUARI', 17, 6869, 1591, 17, 22, 0,
'Sudeste', 'MG', 'ITAJUBA', 24, 14459, 775, 0, 28, 0,
'Sudeste', 'RJ', 'METROPOLITANA', 23, 162485, 3413, 10, 432, 4,
'Sudeste', 'RJ', 'CENTRO-SUL', 11, 18614, 1206, 0, 4, 0,
'Sudeste', 'ES', 'SUL', 12, 208972, 19632, 51, 377, 2,
'Sudeste', 'SP', 'ALTA SOROCABANA', 4, 4166, 119, 0, 4, 0,
'Sudeste', 'SP', 'BAURU', 10, 5735, 277, 0, 3, 0,
'Sul', 'PR', '19A RS JACAREZINHO', 9, 3860, 202, 1, 4, 0,
'Sul', 'SC', 'EXTREMO OESTE', 22, 2428,	260, 3, 3, 0,
'Sul', 'RS', 'REGIAO 30', 20, 34116, 3407, 6, 69, 0,
'Centro-Oeste',	'GO', 'SERRA DA MESA', 26, 46388, 3930, 1, 81, 1,
'Centro-Oeste',	'MT', 'TELES PIRES', 7, 13705, 1186, 0, 15,	0,
'Centro-Oeste', 'MS', 'DOURADOS', 14, 9110, 111, 0, 3, 0,)

#Printar dados acumulados RJ
print('Número de casos acumulados do Estado do RJ: ', listaDados[248])
print('Número de casos acumulados do Estado do RJ: ', tuplaDados[248])

#Printar todos os óbitos acumulados dos estados
obitoSoma = [listaDados[17]+listaDados[26]+listaDados[35]+listaDados[44]+listaDados[53]+listaDados[62]+listaDados[71]+listaDados[80]+listaDados[89]+listaDados[98]+listaDados[107]+listaDados[116]+listaDados[125]+listaDados[134]+listaDados[143]+listaDados[152]+listaDados[161]+listaDados[170]+listaDados[179]+listaDados[188]+listaDados[197]+listaDados[206]+listaDados[215]+listaDados[224]+listaDados[233]+listaDados[242]+listaDados[251]+listaDados[260]+listaDados[269]+listaDados[278]+listaDados[287]+listaDados[296]+listaDados[305]+listaDados[314]+listaDados[323]]
print('Total de óbitos acumulados de todos os estados: ', sum(obitoSoma))

#Corrigir dados para novos óbitos de PB
print('Total de novos óbitos da PB: ', listaDados[170])
obitoCorrecaoPB = int(input('Inserir número de óbitos da Paraíba corrigido: '))
listaDados[170] = obitoCorrecaoPB
print('Números de óbitos da Paraíba corrigidos: ', listaDados[170])
    #Na Tupla os dados são imutáveis, operação possível apenas na lista

#Criar nova lista com dados de um estado / todos os municípios dia 01/01/2021
#Região, Estado, Municipio, regiaoSaude, semanaEpi, populacao, casosAcumulado, casosNovos, obitosAcumulado, obitosNovos
listaRoraima = ['Norte',	'RR', 'Amajari', 'CENTRO NORTE', 53, 12796, 592, 0, 16,	0,
'Norte', 'RR', 'Alto Alegre', 'CENTRO NORTE', 53, 15510, 836, 1, 18, 0,
'Norte', 'RR', 'Boa Vista', 'CENTRO NORTE', 53, 399213, 51619, 18, 576, 3,
'Norte', 'RR', 'Bonfim', 'CENTRO NORTE', 53, 12409, 1339, 0, 14, 0,
'Norte', 'RR', 'Canta', 'CENTRO NORTE', 53, 18335, 1431, 0, 16, 2,
'Norte', 'RR', 'Caracarai', 'SUL', 53, 21926, 1390, 0, 17, 0,
'Norte', 'RR', 'Caroebe', 'SUL', 53, 10169, 1208, 0, 8, 0, 
'Norte', 'RR', 'Iracema', 'SUL', 53, 11950, 620, 0, 7, 0,
'Norte', 'RR', 'Mucajai', 'CENTRO NORTE', 53, 17853, 1527, 0, 18, 0,
'Norte', 'RR', 'Normandia', 'CENTRO NORTE', 53, 11290, 411, 0, 20, 1,
'Norte', 'RR', 'Pacaraima', 'CENTRO NORTE', 53, 17401, 1769, 0, 29, 0,
'Norte', 'RR', 'Rorainopolis', 'SUL', 53, 30163, 1962, 1, 28, 0,
'Norte', 'RR', 'Sao Joao da Baliza', 'SUL', 53, 8201, 908, 0, 3, 0,
'Norte', 'RR', 'Sao Luiz', 'SUL', 53, 7986, 280, 0, 5, 0,
'Norte', 'RR', 'Uiramuta', 'CENTRO NORTE', 53, 10559, 1004, 0, 6, 0,]

for i in range (len(listaRoraima)):
    listaDados.append(listaRoraima[i])

#Remover regiões de saúde da lista
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('SUL')
listaRoraima.remove('SUL')
listaRoraima.remove('SUL')
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('CENTRO NORTE')
listaRoraima.remove('SUL')
listaRoraima.remove('SUL')
listaRoraima.remove('SUL')
listaRoraima.remove('CENTRO NORTE')


#Verificar soma dos dados dos municípios - REGIÃO CENTRO NORTE APENAS
    #(se é igual ao dado da lista, mostrando apenas se for verdadeiro)
    #populacao, casosAcumulado, casosNovos, obitosAcumulado, obitosNovos

populacao = 399213
casosAcumulado = 51619 
casosNovos = 18 
obitosAcumulado = 576  
obitosNovos = 6

populacaoCN = 0
casosAcumuladoCN = 0
casosNovosCN = 0 # [listaRoraima[8]+listaRoraima[18]+listaRoraima[28]+listaRoraima[38]+listaRoraima[48]+listaRoraima[88]+listaRoraima[98]+listaRoraima[108]+listaRoraima[148]]
obitosAcumuladoCN = 0 # [listaRoraima[9]+listaRoraima[19]+listaRoraima[29]+listaRoraima[39]+listaRoraima[49]+listaRoraima[89]+listaRoraima[99]+listaRoraima[109]+listaRoraima[149]]  
obitosNovosCN = 0 # [listaRoraima[10]+listaRoraima[206]+listaRoraima[30]+listaRoraima[40]+listaRoraima[50]+listaRoraima[90]+listaRoraima[100]+listaRoraima[110]+listaRoraima[150]]


for i in range (len(listaRoraima)):
    if (i==0):
        i = i + 1
    if ((i-4)%9)==0:
        populacaoCN = populacaoCN + listaRoraima[i]
    if ((i-5)%9)==0:
        casosAcumuladoCN = casosAcumuladoCN + listaRoraima[i]
    if ((i-6)%9)==0:
        casosNovosCN = casosNovosCN + listaRoraima[i]
    if ((i-7)%9)==0:
        obitosAcumuladoCN = obitosAcumuladoCN + listaRoraima[i]
    if ((i-8)%9)==0:
        obitosNovosCN = obitosNovosCN + listaRoraima[i]

varPop = populacao != populacaoCN
varCaso = casosAcumulado != casosAcumuladoCN
varNov = casosNovos != casosNovosCN
varObi = obitosAcumulado != obitosAcumuladoCN
varObin = obitosNovos != obitosNovosCN
if (varPop == False):
    print('Popuação total igual.')
if(varCaso == False):
    print('Número de casos acumulados igual.')
if(varNov == False):
    print('Número de casos novos igual.')
if(varObi == False): 
    print('Número de óbitos acumulados igual.')
if(varObin== False):
    print('Número de óbitos novos igual.')

#Printar o tamanho total da lista
print('Tamanho total da lista: ', len(listaRoraima))

#Verificar maior e menor valor  de óbitos novos 

maiorRoraima = listaRoraima[8]
menorRoraima = listaRoraima[8]
for i in range (len(listaRoraima)):
    if ((i-8)%9==0):
        if listaRoraima[i]>maiorRoraima:
            maiorRoraima = listaRoraima[i]
        if listaRoraima[i]<menorRoraima:
            menorRoraima = listaRoraima[i]

print('Maior número de óbitos novos: ', maiorRoraima, '\n Menor número de óbitos novos: ', menorRoraima)

#Criar dicionário para encontrar os municípios de um estado 
    #extrair os dados de casos novos apenas com um comando



#Extrair os dados de Teresina/PI
    #printar casos novos


