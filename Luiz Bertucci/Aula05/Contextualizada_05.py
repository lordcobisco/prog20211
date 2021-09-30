'''
Fundamentos de Programação - IINELS
Atividade Contextualizada 05 - Lista Covid
Nome: Luiz Henrique Bertucci
Site com informações COVID https://covid.saude.gov.br/
'''

#Exercício 1
#   a)
#Lista e Tupla com informações importadas manualmente do database 

# regiao, estado, data,	semanaEpi, populacao, casosAcumul, casosNovos, obitosAcumul, obitosNovos


listaCovid = [
'Norte',        'RO ',      11,             '2021-06-30',	26,	1777225,	247607,	202,	6136,	5,
'Norte',    	'AM',	    13,             '2021-06-30',	26,	4144597,	402089,	342,	13313,	14,
'Norte',    	'PA',       15,             '2021-06-30', 	26,	8602865,	552937,	1797,	15469,	25,
'Norte',    	'RR',   	14,             '2021-06-30',	26,	605761,	    112133,	275, 	1745,	14,
'Norte',    	'AC',   	12,             '2021-06-30',	26,	881935,	    85556,	30, 	1738,	0,
'Norte',    	'AP',		16,				'2021-06-30',	26,	845731, 	117188,	197,	1835,	2,
'Norte',	    'TO',		17,				'2021-06-30',	26,	1572866, 	197636,	370,	3213,	8,
'Nordeste', 	'MA',		21,				'2021-06-30',	26,	7075181, 	317446,	839,	9043,	20,
'Nordeste', 	'PI',	    22,				'2021-06-30',	26,	3273227, 	295781,	281,	6597,	23,
'Nordeste', 	'CE',	    23,				'2021-06-30',	26,	9132078, 	885980,	512,	22571,	17,
'Nordeste', 	'RN',		24,				'2021-06-30',	26,	3506853, 	340165,	2871,	6768,	20,
'Nordeste', 	'PB',		25,				'2021-06-30',	26,	4018127, 	396442,	1733,	8606,	20,
'Nordeste', 	'PE',		26,				'2021-06-30',	26,	9557071, 	550292,	975,	17685,	45,
'Nordeste', 	'AL',		27,				'2021-06-30',	26,	3337357, 	216717,	516,	5340,	20,
'Nordeste', 	'SE',		28,				'2021-06-30',	26,	2298696, 	263512,	398,	5698,	17,
'Nordeste', 	'BA',		29,				'2021-06-30',	26,	14873064,	1124994,1683,	24012,	106,
'Sudeste',	    'MG',		31,				'2021-06-30',	26,	21168791,	1803748,8686,	46242,	281,
'Sudeste',	    'ES',		32,				'2021-06-30',	26,	4018650, 	517873,	1108,	11475,	13,
'Sudeste',	    'RJ',		33,				'2021-06-30',	26,	17264943,	958199,	775,	55470,	133,
'Sudeste',	    'SP',		35,				'2021-06-30',	26,	45919049,	3727348,7762,	127681,	744,
'Sul',      	'PR',		41,				'2021-06-30',	26,	11433957,	1284806,5789,	30711,	201,
'Sul',      	'SC',		42,				'2021-06-30',	26,	7164788,	1052455,1591,	16861,	37,
'Sul',	        'RS',	    43,			    '2021-06-30',	26,	11377239,	1215519,1228,	31398,	118,
'Centro-Oeste',	'MS',	    50,				'2021-06-30',	26,	2778986, 	335411,	730,	8204,	51,
'Centro-Oeste',	'MT',	    51,				'2021-06-30',	26,	3484466,	449705,	1374,	11817,	25,
'Centro-Oeste',	'GO',	    52,				'2021-06-30',	26,	7018354,	675141,	947,	19187,	103,
'Centro-Oeste',	'DF',	    53,				'2021-06-30',	26,	3015268,	430461,	825,	9251,	19,
]


tuplaCovid = (
'Norte',        'RO ',      11,             '2021-06-30',	26,	1777225,	247607,	202,	6136,	5,
'Norte',    	'AM',	    13,             '2021-06-30',	26,	4144597,	402089,	342,	13313,	14,
'Norte',    	'PA',       15,             '2021-06-30', 	26,	8602865,	552937,	1797,	15469,	25,
'Norte',    	'RR',   	14,             '2021-06-30',	26,	605761,	    112133,	275, 	1745,	14,
'Norte',    	'AC',   	12,             '2021-06-30',	26,	881935,	    85556,	30, 	1738,	0,
'Norte',    	'AP',		16,				'2021-06-30',	26,	845731, 	117188,	197,	1835,	2,
'Norte',	    'TO',		17,				'2021-06-30',	26,	1572866, 	197636,	370,	3213,	8,
'Nordeste', 	'MA',		21,				'2021-06-30',	26,	7075181, 	317446,	839,	9043,	20,
'Nordeste', 	'PI',	    22,				'2021-06-30',	26,	3273227, 	295781,	281,	6597,	23,
'Nordeste', 	'CE',	    23,				'2021-06-30',	26,	9132078, 	885980,	512,	22571,	17,
'Nordeste', 	'RN',		24,				'2021-06-30',	26,	3506853, 	340165,	2871,	6768,	20,
'Nordeste', 	'PB',		25,				'2021-06-30',	26,	4018127, 	396442,	1733,	8606,	20,
'Nordeste', 	'PE',		26,				'2021-06-30',	26,	9557071, 	550292,	975,	17685,	45,
'Nordeste', 	'AL',		27,				'2021-06-30',	26,	3337357, 	216717,	516,	5340,	20,
'Nordeste', 	'SE',		28,				'2021-06-30',	26,	2298696, 	263512,	398,	5698,	17,
'Nordeste', 	'BA',		29,				'2021-06-30',	26,	14873064,	1124994,1683,	24012,	106,
'Sudeste',	    'MG',		31,				'2021-06-30',	26,	21168791,	1803748,8686,	46242,	281,
'Sudeste',	    'ES',		32,				'2021-06-30',	26,	4018650, 	517873,	1108,	11475,	13,
'Sudeste',	    'RJ',		33,				'2021-06-30',	26,	17264943,	958199,	775,	55470,	133,
'Sudeste',	    'SP',		35,				'2021-06-30',	26,	45919049,	3727348,7762,	127681,	744,
'Sul',      	'PR',		41,				'2021-06-30',	26,	11433957,	1284806,5789,	30711,	201,
'Sul',      	'SC',		42,				'2021-06-30',	26,	7164788,	1052455,1591,	16861,	37,
'Sul',	        'RS',	    43,			    '2021-06-30',	26,	11377239,	1215519,1228,	31398,	118,
'Centro-Oeste',	'MS',	    50,				'2021-06-30',	26,	2778986, 	335411,	730,	8204,	51,
'Centro-Oeste',	'MT',	    51,				'2021-06-30',	26,	3484466,	449705,	1374,	11817,	25,
'Centro-Oeste',	'GO',	    52,				'2021-06-30',	26,	7018354,	675141,	947,	19187,	103,
'Centro-Oeste',	'DF',	    53,				'2021-06-30',	26,	3015268,	430461,	825,	9251,	19,
)


#Exercício 1
#   b)
#Printar obitos acumulados para estado do Rio de Janeiro, em lista e tupla. 

print('****lista****\n O número de óbito acumulados no estado do rio de janeiro é: ', listaCovid[188])

print('\n\n****tupla****\n O número de óbito acumulados no estado do rio de janeiro é: ', tuplaCovid[188])


#Exercício 1
#   c)
#Printar todos os óbitos acumulados dos estados.

somaObitos = 0
print('\n\nEstado****Óbitos')
for i in range(1, 270, 10 ):
    
    print(listaCovid[i],'     ', listaCovid[i+7])
    temp = listaCovid[i+7]
    somaObitos = temp + somaObitos
 
print('\nA soma de óbitos acumulados em todos os estados é: ',somaObitos)

#Exercício 1
#   d)
#Somar 10 óbitos novos no estado da Paraíba.
print('Óbitos novos na Paraíba: ', listaCovid[119])
listaCovid[119]+= 10
print('Óbitos novos na Paraíba [ATUALIZADO]: ', listaCovid[119])

#Exercício 1
#   e)
#RESPOSTA:
print('\nRESPOSTA LETRA D:\nNão foi possível realizar a operação em tupla, pois uma das suas caracteristicas principais é ser imutável.\n')

#Exercício 1
#   f)
#Crie uma nova lista com apenas dados de 1 estado e todos os municípios e adicione essa lista nova a lista já existente

listaAC= [
'Norte',	'AC',	'Acrelândia',       	12,	120001,	12002,	'BAIXO ACRE E PURUS',	'2021-09-11',	36,	15256,	1796,	0,	37,	0,
'Norte',	'AC',	'Assis Brasil',     	12,	120005,	12001,	'ALTO ACRE',	'2021-09-12',	37	,7417,	1829,	0,	24,	0,
'Norte',	'AC',	'Brasiléia',        	12, 120010,	12001,	'ALTO ACRE',	'2021-09-12',	37,	26278,	2997,	0,	43,	0,
'Norte',	'AC',	'Bujari',	            12,	120013,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12',	37,	10266,	1139,	0,	17,	0,
'Norte',    'AC',	'Capixaba',	            12,	120017,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12',	37,	11733,	675,	0,	17,	0,
'Norte',	'AC',	'Cruzeiro do Sul',  	12,	120020,	12003,	'JURUA E TARAUACA/ENVIRA',	'2021-09-12',	37,	88376,	7893,	0,	165,	0,
'Norte',	'AC',	'Epitaciolândia',   	12,	120025,	12001,	'ALTO ACRE',	'2021-09-12',	37,	18411,	1583,	0,	35,	0,
'Norte',	'AC',	'Feijó',            	12,	120030,	12003,	'JURUA E TARAUACA/ENVIRA',	'2021-09-12',	37,	34780,	3337,	0,	63,	0,			
'Norte',	'AC',	'Jordão',	            12,	120032,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12',	37,	8317,	706,	0,	2,	0,
'Norte',	'AC',	'Mâncio Lima',	        12,	120033,	12003,	'JURUA E TARAUACA/ENVIRA',	'2021-09-12',	37,	18977,	2995,	0,	32,	0,
'Norte',	'AC',	'Manoel Urbano',	    12,	120034,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12	37',	9459,	907,	0,	14,	0,
'Norte',	'AC',	'Marechal Thaumaturgo',	12,	120035,	12003,	'JURUA E TARAUACA/ENVIRA',	'2021-09-12',	37,	18867,	1358,	0,	12,	0,
'Norte',	'AC',	'Plácido de Castro',	12,	120038,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12',	37,	19761,	1787,	0,	19,	0,
'Norte',	'AC',	'Porto Walter ',    	12,	120039,	12003,	'JURUA E TARAUACA/ENVIRA',	'2021-09-12	37',	11982,	551,	0,	6,	0,
'Norte',	'AC',	'Rio Branco',	        12,	120040,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12',	37,	407319,	38088,	4,	1086,	0,
'Norte',	'AC',	'Rodrigues Alves',	    12,	120042,	12003,	'JURUA E TARAUACA/ENVIRA',	'2021-09-12',	37,	18930,	1015,	0,	13,	0,
'Norte',	'AC',	'Santa Rosa do Purus',	12,	120043,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12',	37,	6540,	1014,	0,	7,	0,
'Norte',	'AC',	'Senador Guiomard',	    12,	120045,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12',	37	,23024,	1202,	0,	42,	0,
'Norte',	'AC',	'Sena Madureira',   	12,	120050,	12002,	'BAIXO ACRE E PURUS',   '2021-09-12',	37,	45848,	5871,	0,	67,	0,
'Norte',	'AC',	'Tarauacá',         	12,	120060,	12003,	'JURUA E TARAUACA/ENVIRA',    	'2021-09-12',	37,	42567,	6589,	0,	46,	0,
'Norte',	'AC',	'Xapuri',	            12,	120070,	12001,	'ALTO ACRE',	'2021-09-12',	37,	19323,	3029,	0,	31,	0,
'Norte',	'AC',	'Porto Acre',       	12,	120080,	12002,	'BAIXO ACRE E PURUS',	'2021-09-12	37',	18504,	1550,	0,	38,	0,
]


#concatenar comm lista covid
listaCovid.append(listaAC)

#Exercício 1
#   g)
#Remova da lista os dados das regiões de saúde.


listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('ALTO ACRE')
listaAC.remove('ALTO ACRE')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('JURUA E TARAUACA/ENVIRA')
listaAC.remove('ALTO ACRE')
listaAC.remove('JURUA E TARAUACA/ENVIRA')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('JURUA E TARAUACA/ENVIRA')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('JURUA E TARAUACA/ENVIRA')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('JURUA E TARAUACA/ENVIRA')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('JURUA E TARAUACA/ENVIRA')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('BAIXO ACRE E PURUS')
listaAC.remove('JURUA E TARAUACA/ENVIRA')
listaAC.remove('ALTO ACRE')
listaAC.remove('BAIXO ACRE E PURUS')


#Exercício 1
#   h)
# Verifique se a soma dos dados dos municípios na data de 18/08/2020 é igual ao dado da lista,
#  mostrando na tela apenas se for verdadeiro.
somaObitosAC = listaAC[11] + listaAC[24] + listaAC[37] + listaAC[50] + listaAC[63] + listaAC[76] + listaAC[89] + listaAC[102]+ listaAC[115] + listaAC[128] + listaAC[140] + listaAC[153] + listaAC[166] + listaAC[178] + listaAC[191] + listaAC[204] + listaAC[217]+ listaAC[230] + listaAC[243] + listaAC[256] + listaAC[269]
print('\nA soma de óbitos na lista geral é: ', listaCovid[48],'\nA soma de óbito na lista do estado é: ', somaObitosAC, '\nA igualdade entre os valores é: ', listaCovid[48]==somaObitosAC)

#Exercício 1
#   i)
#Retorne o tamanho total da lista.
print ("O tamanho da lista é: ", len(listaCovid))

#Exercício 1
#   j)
#Verifique qual é o maior valor numérico de óbitos
#  novos e o menor valor numérico de óbitos novos.

listaCovid_obitosNovos = [1108,775,7762,8686,1797,839,202,30,1591,1733]
print ("O número máximo de óbitos novos é: ", max(listaCovid_obitosNovos))
print ("O número mínimo de óbitos novos é: ", min(listaCovid_obitosNovos))

#Exercício 1
#   k)
#Crie um dicionário de forma que seja possível encontrar os municípios associados 
# a um estado específico e extrair os dados de casos novos em apenas um comando.


#Exercício 1
#   L)
#Extraia os dados de Teresina/PI apresentando os casos novos com um print.


