# Exercício Contextualizado 5
# Letra "a":

lista = [['Norte','RO','Porto Velho',11,110020,11004,'MADEIRA-MAMORE','2021-07-01',26,529544,82740,33,2431,0,1],
['Norte','AC','Rio Branco',12,120040,12002,'BAIXO ACRE E PURUS','2021-07-01',26,407319,37650,34,1058,1,1],
['Norte','AM','Manaus',13,130260,13001,'ENTORNO E ALTO RIO NEGRO','2021-07-01',26,2182763,187452,522,9169,5,1],
['Norte','RR','Boa Vista',14,140010,14001,'CENTRO NORTE','2021-07-01',26,399213,86703,425,1352,2,1],
['Norte','PA','Belém',15,150140,15006,'METROPOLITANA I','2021-07-01',26,1492745,103430,183,4940,2,1],
['Norte','TO','Palmas',17,172100,17006,'CAPIM DOURADO','2021-07-01',26,299127,45781,54,583,0,1],
['Norte','AP','Macapá',16,160030,16001,'AREA CENTRAL','2021-07-01',26,503327,56905,88,1403,3,1],
['Nordeste','MA','São Luís',21,211130,21016,'SAO LUIS','2021-07-01',26,1101884,42709,105,2364,5,1],
['Nordeste','PE','Recife',26,261160,26010,'RECIFE','2021-07-01',26,1645727,135212,194,4684,11,1],
['Nordeste','PE','Petrolina',26,261110,26009,'PETROLINA','2021-07-01',26,349145,27768,136,467,1,0],
['Nordeste','PB','João Pessoa',25,250750,25001,'1ª REGIAO MATA ATLANTICA','2021-07-01',26,809015,99212,68,2793,7,1],
['Nordeste','PB','Campina Grande',25,250400,25016,'16ª REGIAO','2021-07-01',26,	409731,	37159,85,1010,2,0],
['Nordeste','PB','Bayeux',25,250180,25001,'1ª REGIAO MATA ATLANTICA','2021-07-01',26,96880,7451,3,236,2,1],
['Nordeste','AL','Maceió',27,270430,27001,'1ª REGIAO DE SAUDE','2021-07-01',26,1018948,82860,76,2342,9,1,],
['Nordeste','SE','Aracaju',28,280030,28001,'ARACAJU','2021-07-01',26,657013,120810,328,2316,4,1],
['Nordeste','BA','Salvador',29,292740,29020,'SALVADOR','2021-07-01	26',2872347,224988,375,7415,24,1],
['Nordeste','BA','Feira de Santana',29,291080,29006,'FEIRA DE SANTANA','2021-07-01',26,614872,49460,169,952,4,0],
['Nordeste','PI','Teresina',22,221100,22004,'ENTRE RIOS','2021-07-01',26,864845,100323,108,2462,11,1],
['Nordeste','CE','Fortaleza',23,230440,23001,'1ª REGIAO FORTALEZA','2021-07-01',26,2669342,249953,199,9205,14,1,],
['Nordeste','CE','Crato',23,230420,23020,'20ª REGIAO CRATO','2021-07-01',26,132123,16691,8,214,1,0],
['Nordeste','RN','Natal',24,240810,24007,'7ª REGIAO DE SAUDE - METROPOLITANA','2021-07-01',26,884122,94198,954,2525,5,1],
['Sudeste','SP','São Paulo',35,355030,35016,'SAO PAULO','2021-07-01',26,12252023,857318,2155,33603,93,1],
['Sudeste','SP','Campinas',35,350950,35072,'REGIAO METROPOLITANA DE CAMPINAS','2021-07-01',26,1204073,94658,395,3760,23,1],
['Sudeste','SP','Santos',35,354850,35041,'BAIXADA SANTISTA','2021-07-01',26,433311,54682,88,1899,10,0],
['Sudeste','SP','Osasco',35,353440,35014,'ROTA DOS BANDEIRANTES','2021-07-01',26,698418,39720,97,2284,9,1],
['Sudeste','RJ','Rio de Janeiro',33,330455,33005,'METROPOLITANA I','2021-07-01',26,6718903,368354,775,28731,115,1],
['Sudeste','RJ','Paraty',33,330380,33001,'BAIA DA ILHA GRANDE','2021-07-01',26,43165,2632,1,74,1,0],
['Sudeste','RJ','São Gonçalo',33,330490,33006,'METROPOLITANA II','2021-07-01',26,1084839,50684,125,2675,16,1],
['Sudeste','ES','Vitória',32,320530,32002,'METROPOLITANA','2021-07-01',26,362097,55122,63,1199,2,1],
['Sudeste','MG','Belo Horizonte',31,310620,31016,'BELO HORIZONTE/ NOVA LIMA/ CAETE','2021-07-01',26,2512070,236958,359,5746,31,1],
['Sudeste','MG','Tiradentes',31,316880,31015,'SAO JOAO DEL REI','2021-07-01',26,7981,474,2,17,0,0],
['Sudeste','MG','Uberlândia',31,317020,31075,'UBERLANDIA / ARAGUARI','2021-07-01',26,691305,102011,265,2552,5,0],
['Centro-Oeste','MT','Cuiabá',51,510340,51002,'BAIXADA CUIABANA','2021-07-01',26,612547,93427,239,3046,8,1],
['Centro-Oeste','MS','Campo Grande',50,500270,50001,'CAMPO GRANDE','2021-07-01',26,895982,119906,161,3381,7,1],
['Centro-Oeste','MS','Dourados',50,500370,50003,'DOURADOS','2021-07-01',26,222949,36037,70,602,2,0],
['Centro-Oeste','GO','Goiânia',52,520870,52001,'CENTRAL','2021-07-01',26,1516113,163154,711,5406,10,1],
['Centro-Oeste','DF','Brasília',53,530010,53001,'DISTRITO FEDERAL','2021-07-01',26,3015268,431151,690,9264,13,1],
['Sul','PR','Curitiba',41,410690,41002,'2ª RS METROPOLITANA','2021-07-01',26,1933105,171593,892,5884,28,1],
['Sul','PR','Maringá',41,411520,41015,'15ª RS MARINGA','2021-07-01',26,423666,55696,518,1298,12,0],
['Sul','SC','Florianópolis',42,420540,42007,'GRANDE FLORIANOPOLIS','2021-07-01',26,500973,77190,62,1009,-1,1],
['Sul','SC','Jaraguá do Sul',42,420890,42011,'NORDESTE','2021-07-01',26,177697,30233,176,367,1,0],
['Sul','RS','Porto Alegre',43,431490,43010,'REGIAO 10','2021-07-01',26,1483771,135629,57,5130,17,1],
['Sul','RS','Santa Maria',43,431690,43001,'REGIAO 01','2021-07-01',26,282123,34003,24,755,2,0]]

tupla = (('Norte','RO','Porto Velho',11,110020,11004,'MADEIRA-MAMORE','2021-07-01',26,529544,82740,33,2431,0,1),
('Norte','AC','Rio Branco',12,120040,12002,'BAIXO ACRE E PURUS','2021-07-01	26',407319,37650,34,1058,1,1),
('Norte','AM','Manaus',13,130260,13001,'ENTORNO E ALTO RIO NEGRO','2021-07-01',26,2182763,187452,522,9169,5,1),
('Norte','RR','Boa Vista',14,140010,14001,'CENTRO NORTE','2021-07-01',26,399213,86703,425,1352,2,1),
('Norte','PA','Belém',15,150140,15006,'METROPOLITANA I','2021-07-01',26,1492745,103430,183,4940,2,1),
('Norte','TO','Palmas',17,172100,17006,'CAPIM DOURADO','2021-07-01',26,299127,45781,54,583,0,1),
('Norte','AP','Macapá',16,160030,16001,'AREA CENTRAL','2021-07-01',26,503327,56905,88,1403,3,1),
('Nordeste','MA','São Luís',21,211130,21016,'SAO LUIS','2021-07-01',26,1101884,42709,105,2364,5,1),
('Nordeste','PE','Recife',26,261160,26010,'RECIFE','2021-07-01',26,1645727,135212,194,4684,11,1),
('Nordeste','PE','Petrolina',26,261110,26009,'PETROLINA','2021-07-01',26,349145,27768,136,467,1,0),
('Nordeste','PB','João Pessoa',25,250750,25001,'1ª REGIAO MATA ATLANTICA','2021-07-01',26,809015,99212,68,2793,7,1),
('Nordeste','PB','Campina Grande',25,250400,25016,'16ª REGIAO','2021-07-01',26,	409731,	37159,85,1010,2,0),
('Nordeste','PB','Bayeux',25,250180,25001,'1ª REGIAO MATA ATLANTICA','2021-07-01',26,96880,7451,3,236,2,1),
('Nordeste','AL','Maceió',27,270430,27001,'1ª REGIAO DE SAUDE','2021-07-01',26,1018948,82860,76,2342,9,1,),
('Nordeste','SE','Aracaju',28,280030,28001,'ARACAJU','2021-07-01',26,657013,120810,328,2316,4,1),
('Nordeste','BA','Salvador',29,292740,29020,'SALVADOR','2021-07-01	26',2872347,224988,375,7415,24,1),
('Nordeste','BA','Feira de Santana',29,291080,29006,'FEIRA DE SANTANA','2021-07-01',26,614872,49460,169,952,4,0),
('Nordeste','PI','Teresina',22,221100,22004,'ENTRE RIOS','2021-07-01',26,864845,100323,108,2462,11,1),
('Nordeste','CE','Fortaleza',23,230440,23001,'1ª REGIAO FORTALEZA','2021-07-01',26,2669342,249953,199,9205,14,1,),
('Nordeste','CE','Crato',23,230420,23020,'20ª REGIAO CRATO','2021-07-01',26,132123,16691,8,214,1,0),
('Nordeste','RN','Natal',24,240810,24007,'7ª REGIAO DE SAUDE - METROPOLITANA','2021-07-01',26,884122,94198,954,2525,5,1),
('Sudeste','SP','São Paulo',35,355030,35016,'SAO PAULO','2021-07-01',26,12252023,857318,2155,33603,93,1),
('Sudeste','SP','Campinas',35,350950,35072,'REGIAO METROPOLITANA DE CAMPINAS','2021-07-01',26,1204073,94658,395,3760,23,1),
('Sudeste','SP','Santos',35,354850,35041,'BAIXADA SANTISTA','2021-07-01',26,433311,54682,88,1899,10,0),
('Sudeste','SP','Osasco',35,353440,35014,'ROTA DOS BANDEIRANTES','2021-07-01',26,698418,39720,97,2284,9,1),
('Sudeste','RJ','Rio de Janeiro',33,330455,33005,'METROPOLITANA I','2021-07-01',26,6718903,368354,775,28731,115,1),
('Sudeste','RJ','Paraty',33,330380,33001,'BAIA DA ILHA GRANDE','2021-07-01',26,43165,2632,1,74,1,0),
('Sudeste','RJ','São Gonçalo',33,330490,33006,'METROPOLITANA II','2021-07-01',26,1084839,50684,125,2675,16,1),
('Sudeste','ES','Vitória',32,320530,32002,'METROPOLITANA','2021-07-01',26,362097,55122,63,1199,2,1),
('Sudeste','MG','Belo Horizonte',31,310620,31016,'BELO HORIZONTE/ NOVA LIMA/ CAETE','2021-07-01',26,2512070,236958,359,5746,31,1),
('Sudeste','MG','Tiradentes',31,316880,31015,'SAO JOAO DEL REI','2021-07-01',26,7981,474,2,17,0,0),
('Sudeste','MG','Uberlândia',31,317020,31075,'UBERLANDIA / ARAGUARI','2021-07-01',26,691305,102011,265,2552,5,0),
('Centro-Oeste','MT','Cuiabá',51,510340,51002,'BAIXADA CUIABANA','2021-07-01',26,612547,93427,239,3046,8,1),
('Centro-Oeste','MS','Campo Grande',50,500270,50001,'CAMPO GRANDE','2021-07-01',26,895982,119906,161,3381,7,1),
('Centro-Oeste','MS','Dourados',50,500370,50003,'DOURADOS','2021-07-01',26,222949,36037,70,602,2,0),
('Centro-Oeste','GO','Goiânia',52,520870,52001,'CENTRAL','2021-07-01',26,1516113,163154,711,5406,10,1),
('Centro-Oeste','DF','Brasília',53,530010,53001,'DISTRITO FEDERAL','2021-07-01',26,3015268,431151,690,9264,13,1),
('Sul','PR','Curitiba',41,410690,41002,'2ª RS METROPOLITANA','2021-07-01',26,1933105,171593,892,5884,28,1),
('Sul','PR','Maringá',41,411520,41015,'15ª RS MARINGA','2021-07-01',26,423666,55696,518,1298,12,0),
('Sul','SC','Florianópolis',42,420540,42007,'GRANDE FLORIANOPOLIS','2021-07-01',26,500973,77190,62,1009,-1,1),
('Sul','SC','Jaraguá do Sul',42,420890,42011,'NORDESTE','2021-07-01',26,177697,30233,176,367,1,0),
('Sul','RS','Porto Alegre',43,431490,43010,'REGIAO 10','2021-07-01',26,1483771,135629,57,5130,17,1),
('Sul','RS','Santa Maria',43,431690,43001,'REGIAO 01','2021-07-01',26,282123,34003,24,755,2,0))

# Letra "b":

lista.index(['Sudeste','RJ','Rio de Janeiro',33,330455,33005,'METROPOLITANA I','2021-07-01',26,6718903,368354,775,28731,115,1]) # O índice é 25
lista.index(['Sudeste','RJ','Paraty',33,330380,33001,'BAIA DA ILHA GRANDE','2021-07-01',26,43165,2632,1,74,1,0]) # O índice é 26
lista.index(['Sudeste','RJ','São Gonçalo',33,330490,33006,'METROPOLITANA II','2021-07-01',26,1084839,50684,125,2675,16,1]) # O índice é 27

print("\nA soma do número de casos acumulados para o Estado do Rio de Janeiro (apenas os municípios de 'Rio de Janeiro', 'Paraty e 'São Gonçalo) até a data de 01/07/2021 é:",lista[25][-5]+lista[26][-5]+lista[27][-5])

tupla.index(('Sudeste','RJ','Rio de Janeiro',33,330455,33005,'METROPOLITANA I','2021-07-01',26,6718903,368354,775,28731,115,1)) # O índice é 25
tupla.index(('Sudeste','RJ','Paraty',33,330380,33001,'BAIA DA ILHA GRANDE','2021-07-01',26,43165,2632,1,74,1,0)) # O índice é 26
tupla.index(('Sudeste','RJ','São Gonçalo',33,330490,33006,'METROPOLITANA II','2021-07-01',26,1084839,50684,125,2675,16,1)) # O índice é 27

print("A soma do número de casos acumulados para o Estado do Rio de Janeiro (apenas os municípios de 'Rio de Janeiro', 'Paraty e 'São Gonçalo) até a data de 01/07/2021 é:",tupla[25][-5]+tupla[26][-5]+tupla[27][-5])

# Letra "c":

print("\nA soma do número de óbitos acumulados de todos os Estados até a data 01/07/2021 é (obs.: apenas aqueles municípios presentes na lista):",lista[0][-3]+
lista[1][-3]+lista[2][-3]+lista[3][-3]+lista[4][-3]+lista[5][-3]+lista[6][-3]+lista[7][-3]+lista[8][-3]+lista[9][-3]+lista[10][-3]+
lista[11][-3]+lista[12][-3]+lista[13][-3]+lista[14][-3]+lista[15][-3]+lista[16][-3]+lista[17][-3]+lista[18][-3]+lista[19][-3]+lista[20][-3]+
lista[21][-3]+lista[22][-3]+lista[23][-3]+lista[24][-3]+lista[25][-3]+lista[26][-3]+lista[27][-3]+lista[28][-3]+lista[29][-3]+lista[30][-3]+
lista[31][-3]+lista[32][-3]+lista[33][-3]+lista[34][-3]+lista[35][-3]+lista[36][-3]+lista[37][-3]+lista[38][-3]+lista[39][-3]+lista[40][-3]+
lista[41][-3]+lista[42][-3])

print("\nO Estado de Rondônia tem o seguinte número de casos acumulados:",lista[0][-5])
print("O Estado do Acre tem o seguinte número de casos acumulados:",lista[1][-5])
print("O Estado do Amazonas tem o seguinte número de casos acumulados:",lista[2][-5])
print("O Estado de Roraima tem o seguinte número de casos acumulados:",lista[3][-5])
print("O Estado do Pará tem o seguinte número de casos acumulados:",lista[4][-5])
print("O Estado do Tocantins tem o seguinte número de casos acumulados:",lista[5][-5])
print("O Estado do Amapá tem o seguinte número de casos acumulados:",lista[6][-5])
print("O Estado do Maranhão tem o seguinte número de casos acumulados:",lista[7][-5])
print("O Estado de Pernambuco tem o seguinte número de casos acumulados:",lista[8][-5]+lista[9][-5])
print("O Estado da Paraíba tem o seguinte número de casos acumulados:",lista[10][-5]+lista[11][-5]+lista[12][-5])
print("O Estado de Alagoas tem o seguinte número de casos acumulados:",lista[13][-5])
print("O Estado de Sergipe tem o seguinte número de casos acumulados:",lista[14][-5])
print("O Estado da Bahia tem o seguinte número de casos acumulados:",lista[15][-5]+lista[17][-5])
print("O Estado do Piauí tem o seguinte número de casos acumulados:",lista[17][-5])
print("O Estado do Ceará tem o seguinte número de casos acumulados:",lista[18][-5]+lista[19][-5])
print("O Estado do Rio Grande do Norte tem o seguinte número de casos acumulados:",lista[20][-5])
print("O Estado de São Paulo tem o seguinte número de casos acumulados:",lista[21][-5]+lista[22][-5]+lista[23][-5]+lista[24][-5])
print("O Estado do Rio de Janeiro tem o seguinte número de casos acumulados:",lista[25][-5]+lista[26][-5]+lista[27][-5])
print("O Estado do Espírito Santo tem o seguinte número de casos acumulados:",lista[28][-5])
print("O Estado de Minas Gerais tem o seguinte número de casos acumulados:",lista[29][-5]+lista[30][-5]+lista[31][-5])
print("O Estado do Mato Grosso tem o seguinte número de casos acumulados:",lista[32][-5])
print("O Estado do Mato Grosso do Sul tem o seguinte número de casos acumulados:",lista[33][-5]+lista[34][-5])
print("O Estado do Goiás tem o seguinte número de casos acumulados:",lista[35][-5])
print("O Distrito Federal tem o seguinte número de casos acumulados:",lista[36][-5])
print("O Estado do Paraná tem o seguinte número de casos acumulados:",lista[37][-5]+lista[38][-5])
print("O Estado de Santa Catarina tem o seguinte número de casos acumulados:",lista[39][-5]+lista[40][-5])
print("O Estado do Rio Grande do Sul tem o seguinte número de casos acumulados:",lista[41][-5]+lista[42][-5])

# Letra "d" (lista):

print("\nA Paraíba (representada aqui pelos municípios de 'João Pessoa','Campina Grande' e 'Bayeux') registrou pela 'lista', no dia 1 de julho de 2021,",lista[10][-2]+lista[11][-2]+lista[12][-2],"novos óbitos.")

lista[10][-2] += 5
lista[11][-2] += 3 
lista[12][-2] += 2

print("Ops, parece que temos um erro de contagem aqui. Na verdade, o Estado da Paraíba registrou pela 'lista', no dia 1 de julho de 2021,",lista[10][-2]+lista[11][-2]+lista[12][-2],"novos óbitos.")

# Letra "d" (tupla):

print("\nA Paraíba (representada aqui pelos municípios de 'João Pessoa','Campina Grande' e 'Bayeux') registrou pela 'tupla', no dia 1 de julho de 2021,",tupla[10][-2]+tupla[11][-2]+tupla[12][-2],"novos óbitos.")

# tupla[10][-2] += 5 # Esta linha de código foi 'desativada' pois incorreria em erro na execução do programa.
# tupla[11][-2] += 3 # Esta linha de código foi 'desativada' pois incorreria em erro na execução do programa.
# tupla[12][-2] += 2 # Esta linha de código foi 'desativada' pois incorreria em erro na execução do programa.

print("Ops, parece que temos um erro de contagem aqui. Infelizmente, não conseguimos alterar os dados na 'tupla', então o Estado da Paraíba registrou, no dia 1 de julho de 2021,",tupla[10][-2]+tupla[11][-2]+tupla[12][-2],"novos óbitos.")

# Letra "e":

print("\nAs duas operações foram possíveis (lista e tupla)? Justifique.")
print("\nNão, apenas a operação com a 'lista' foi possível, pois elementos de 'tuplas' são imutáveis enquanto os elementos de 'listas' são mutáveis.")

# Letra "f":

lista_RR_18_08_2020 = [['Norte','RR','Amajari',14,140002,14001,'CENTRO NORTE','2020-08-18',34,12796,277,0,6,0,0],
['Norte','RR','Alto Alegre',14,	140005,	14001,'CENTRO NORTE','2020-08-18',34,15510,493,25,14,0,1],
['Norte','RR','Boa Vista',14,140010,14001,'CENTRO NORTE','2020-08-18',34,399213,29978,408,444,5,1],
['Norte','RR','Bonfim',14,140015,14001,'CENTRO NORTE','2020-08-18',34,12409,609,20,11,0,1],
['Norte','RR','Cantá',14,140017,14001,'CENTRO NORTE','2020-08-18',34,18335,839,7,9,0,1],
['Norte','RR','Caracaraí',14,140020,14002,'SUL','2020-08-18',34,21926,750,2,8,0,0],
['Norte','RR','Caroebe',14,140023,14002,'SUL','2020-08-18',34,10169,832,4,4,0,0],
['Norte','RR','Iracema',14,140028,14002,'SUL','2020-08-18',34,11950,234,1,4,0,0],
['Norte','RR','Mucajaí',14,140030,14001,'CENTRO NORTE','2020-08-18',34,17853,1036,19,12,0,1],
['Norte','RR','Normandia',14,140040,14001,'CENTRO NORTE','2020-08-18',34,11290,272,0,9,0,0],
['Norte','RR','Pacaraima',14,140045,14001,'CENTRO NORTE','2020-08-18',34,17401,1246,17,26,1,0],
['Norte','RR','Rorainópolis',14,140047,14002,'SUL','2020-08-18',34,30163,1401,8,20,0,0],
['Norte','RR','São João da Baliza',14,140050,14002,'SUL','2020-08-18',34,8201,736,0,3,0,0],
['Norte','RR','São Luiz',14,140060,14002,'SUL',	'2020-08-18',34,7986,197,2,2,0,0],
['Norte','RR','Uiramutã',14,140070,14001,'CENTRO NORTE','2020-08-18',34,10559,596,2,2,0,0]]

lista.append(lista_RR_18_08_2020)

# Letra "g":

lista[0].pop(6)
lista[1].pop(6)
lista[2].pop(6)
lista[3].pop(6)
lista[4].pop(6)
lista[5].pop(6)
lista[6].pop(6)
lista[7].pop(6)
lista[8].pop(6)
lista[9].pop(6)
lista[10].pop(6)
lista[11].pop(6)
lista[12].pop(6)
lista[13].pop(6)
lista[14].pop(6)
lista[15].pop(6)
lista[16].pop(6)
lista[17].pop(6)
lista[18].pop(6)
lista[19].pop(6)
lista[20].pop(6)
lista[21].pop(6)
lista[22].pop(6)
lista[23].pop(6)
lista[24].pop(6)
lista[25].pop(6)
lista[26].pop(6)
lista[27].pop(6)
lista[28].pop(6)
lista[29].pop(6)
lista[30].pop(6)
lista[31].pop(6)
lista[32].pop(6)
lista[33].pop(6)
lista[34].pop(6)
lista[35].pop(6)
lista[36].pop(6)
lista[37].pop(6)
lista[38].pop(6)
lista[39].pop(6)
lista[40].pop(6)
lista[41].pop(6)
lista[42].pop(6)
lista[43][0].pop(6)
lista[43][1].pop(6)
lista[43][2].pop(6)
lista[43][3].pop(6)
lista[43][4].pop(6)
lista[43][5].pop(6)
lista[43][6].pop(6)
lista[43][7].pop(6)
lista[43][8].pop(6)
lista[43][9].pop(6)
lista[43][10].pop(6)
lista[43][11].pop(6)
lista[43][12].pop(6)
lista[43][13].pop(6)
lista[43][14].pop(6)

# Letra "h":

somaCasosRR = lista[43][0][-5]+lista[43][1][-5]+lista[43][2][-5]+lista[43][3][-5]+lista[43][4][-5]+lista[43][5][-5]+lista[43][6][-5]+lista[43][7][-5]+lista[43][8][-5]+lista[43][9][-5]+lista[43][10][-5]+lista[43][11][-5]+lista[43][12][-5]+lista[43][13][-5]+lista[43][14][-5]

somaObitosRR = lista[43][0][-3]+lista[43][1][-3]+lista[43][2][-3]+lista[43][3][-3]+lista[43][4][-3]+lista[43][5][-3]+lista[43][6][-3]+lista[43][7][-3]+lista[43][8][-3]+lista[43][9][-3]+lista[43][10][-3]+lista[43][11][-3]+lista[43][12][-3]+lista[43][13][-3]+lista[43][14][-3]

if somaCasosRR == lista[3][-5]:
    print('\nA soma de casos acumulados de todos os municípios de Roraima em 18 de agosto de 2020 é igual ao número de casos acumulados no Estado de Roraima em 1 de julho de 2021 (representado na lista antiga apenas pelo município de "Boa Vista"). São',somaCasosRR,'casos acumulados.')
else:
    print('\nA soma de casos acumulados de todos os municípios de Roraima em 18 de agosto de 2020 não é igual ao número de casos acumulados no Estado de Roraima em 1 de julho de 2021 (representado na lista antiga apenas pelo município de "Boa Vista").')

if somaObitosRR == lista[3][-3]:
    print('\nA soma de óbitos acumulados de todos os municípios de Roraima em 18 de agosto de 2020 é igual ao número de óbitos acumulados no Estado de Roraima em 1 de julho de 2021 (representado na lista antiga apenas pelo município de "Boa Vista"). São',somaObitosRR,'óbitos acumulados.')
else:
    print('\nA soma de óbitos acumulados de todos os municípios de Roraima em 18 de agosto de 2020 não é igual ao número de óbitos acumulados no Estado de Roraima em 1 de julho de 2021 (representado na lista antiga apenas pelo município de "Boa Vista").\n')

# Letra "i":

print(len(lista))

# Letra "j":

obitosNovos = [lista[0][-2],lista[1][-2],lista[2][-2],lista[3][-2],lista[4][-2],lista[5][-2],lista[6][-2],lista[7][-2],
lista[8][-2],lista[9][-2],lista[10][-2],lista[11][-2],lista[12][-2],lista[13][-2],lista[14][-2],lista[15][-2],
lista[16][-2],lista[17][-2],lista[18][-2],lista[19][-2],lista[20][-2],lista[21][-2],lista[22][-2],lista[23][-2],
lista[24][-2],lista[25][-2],lista[26][-2],lista[27][-2],lista[28][-2],lista[29][-2],lista[30][-2],lista[31][-2],
lista[32][-2],lista[33][-2],lista[34][-2],lista[35][-2],lista[36][-2],lista[37][-2],lista[38][-2],lista[39][-2],
lista[40][-2],lista[41][-2],lista[42][-2],lista[43][0][-2],lista[43][1][-2],lista[43][2][-2],lista[43][3][-2],
lista[43][4][-2],lista[43][5][-2],lista[43][6][-2],lista[43][7][-2],lista[43][8][-2],lista[43][9][-2],
lista[43][10][-2],lista[43][11][-2],lista[43][12][-2],lista[43][13][-2],lista[43][14][-2]]

print(max(obitosNovos))
print(min(obitosNovos))

# Letra "k":

dicionario_01_07_2021 = {'Porto Velho/RO': [lista[0][-4]],'Rio Branco/AC': [lista[1][-4]],'Manaus/AM': [lista[2][-4]],
'Boa Vista/RR': [lista[3][-4]],'Belém/PA': [lista[4][-4]],'Palmas/TO': [lista[5][-4]],'Macapá/AP': [lista[6][-4]],
'São Luís/MA': [lista[7][-4]],'Recife/PE': [lista[8][-4]],'Petrolina/PE': [lista[9][-4]],'João Pessoa/PE': [lista[10][-4]],
'Campina Grande/PB': [lista[11][-4]],'Bayeux/PB': [lista[12][-4]],'Maceió/AL': [lista[13][-4]],'Aracaju/SE': [lista[14][-4]],
'Salvador/BA': [lista[15][-4]],'Feira de Santana/BA': [lista[16][-4]],'Teresina/PI': [lista[17][-4]],'Fortaleza/CE': [lista[18][-4]],
'Crato/CE': [lista[19][-4]],'Natal/RN': [lista[20][-4]],'São Paulo/SP': [lista[21][-4]],'Campinas/SP': [lista[22][-4]],
'Santos/SP': [lista[23][-4]],'Osasco/SP': [lista[24][-4]],'Rio de Janeiro/RJ': [lista[25][-4]],'Paraty/RJ': [lista[26][-4]],
'São Gonçalo/RJ': [lista[27][-4]],'Vitória/ES': [lista[28][-4]],'Belo Horizonte/MG': [lista[29][-4]],'Tiradentes/MG': [lista[30][-4]],
'Uberlândia/MG': [lista[31][-4]],'Cuiabá/MT': [lista[32][-4]],'Campo Grande/MS': [lista[33][-4]],'Dourados/MS': [lista[34][-4]],
'Goiânia/GO': [lista[35][-4]],'Brasília/DF': [lista[36][-4]],'Curitiba/PR': [lista[37][-4]],'Maringá/PR': [lista[38][-4]],
'Florianópolis/SC': [lista[39][-4]],'Jaraguá do Sul/SC': [lista[40][-4]],'Porto Alegre/RS': [lista[41][-4]],'Santa Maria/RS': [lista[42][-4]],}

comando = input("\nDigite o nome do município e a sigla do respectivo Estado que você deseja verificar o número de casos novos (01/07/2021): [Município/BR] ")
if comando in dicionario_01_07_2021:
    print(comando,"registrou",dicionario_01_07_2021[comando],"novos casos no dia 1 de julho de 2021.")
else:
    print("Infelizmente, o referido município não está contido em nosso dicionário, por favor, digite outro.")

# Letra "l":

print("\nTeresina, capital do Estado do Piauí, registrou",dicionario_01_07_2021['Teresina/PI'],"novos casos no dia 1 de julho de 2021.")
