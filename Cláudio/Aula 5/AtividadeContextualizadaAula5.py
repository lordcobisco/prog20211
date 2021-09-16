print ('\nBem vind@ a central de informações sobre Covid-19\n')
'''
Sequência das informações presentas na lista
Região, Estado, Município, Código do estado, Código do município, Código da região de saúde, Nome da região de Saúde, Data, População, Caso acumulado, Caos novos, Obitos acumulados, Obitos novos.
'''
lista = ['Norte',	'RO',	'Alta Floresta DOeste',	11,	110001,	11005,	'ZONA DA MATA',	        '12/09/2021',	22945,	4069,	0,	66,	0,			0, #0-13
         'Norte',	'RO',	'Vale do Paraíso',	    11,	110180,	11003,	'CENTRAL',	            '12/09/2021',	6825,	847,	0,	26,	0,			0, #14-27
         'Norte',	'AC',	'Acrelândia',	        12,	120001,	12002,	'BAIXO ACRE E PURUS'	'12/09/2021',	15256,	1796,	0,	37,	0,			0, #28-40
         'Norte',	'AC',	'Xapuri',           	12,	120070,	12001,	'ALTO ACRE',        	'12/09/2021',	19323,	3029,	0,	31,	0,			0, #41-54
         'Norte',	'AM',	'Anori',             	13,	130010,	13002,	'RIO NEGRO E SOLIMOES',	'12/09/2021',	21010,	1918,	0,	33,	0,			0, #55-68
         'Norte',	'AM',	'Urucurituba',	        13,	130440,	13004,	'MEDIO AMAZONAS'	    '12/09/2021',   23065,	2727,	0,	36,	0,			0, #69-81
         'Norte',	'RR',	'Amajari',          	14,	140002,	14001,	'CENTRO NORTE',     	'12/09/2021',   12796,	1170,	2,	21,	0,			0, #82-95
         'Norte',	'RR',	'São Luiz',             14,	140060,	14002,	'SUL',              	'12/09/2021',   7986,	689,	0,	12,	0,			0, #96-109
         'Norte',	'PA',	'Água Azul do Norte',	15,	150034,	15001,	'ARAGUAIA',	            '12/09/2021',   27430,	1259,	0,	18,	0,			0, #110-123
         'Norte',	'PA',	'Viseu',            	15,	150830,	15009,	'RIO CAETES',       	'12/09/2021',   61403,	1549,	0,	36,	0,			0, #124-137
         'Norte',	'AP',	'Serra do Navio',	    16,	160005,	16001,	'AREA CENTRAL',     	'12/09/2021',	5397,	1311,	0,	5,	0,			0, #138-151
         'Norte',	'AP',	'Tartarugalzinho',  	16,	160070,	16002,	'AREA NORTE',       	'12/09/2021',	17315,	1966,	0,	13,	0,			0, #152-165
         'Norte',	'TO',	'Almas',            	17,	170040,	17003,	'SUDESTE',	            '12/09/2021',	7055,	239,	0,	5,	0,			0, #166-179
         'Norte',	'TO',	'Palmas',           	17,	172100,	17006,	'CAPIM DOURADO',    	'12/09/2021',	299127,	51115,	58,	625,0,			1, #180-193
         'Nordeste','MA',	'Afonso Cunha',     	21,	2100100,210050,	'CAXIAS',	            '12/09/2021',	6524,	267,	0,	3,	0,			0, #194-207
         'Nordeste','MA',	'Viana',            	21,	211280,	21018,	'VIANA',            	'12/09/2021',	52441,	330,	0,	42,	0,			0, #208-221
         'Nordeste','PI',	'Altos',             	22,	220040,	22004,	'ENTRE RIOS',       	'12/09/2021',	40524,	4675,	8,	90,	0,			1, #222-235
         'Nordeste','PI',	'Wall Ferraz',         	22,	221170,	22009,	'VALE DO RIO GUARIBAS',	'12/09/2021',	4462,	333,	0,	3,	0,			0, #236-249
         'Nordeste','CE',	'Acarape',          	23,	230015,	23003,	'3ª REGIAO MARACANAU',	'09/09/2021',	14929,	2837,	0,	32,	0,			0, #250-263
         'Nordeste','CE',	'Varjota',          	23,	231395,	23011,	'11ª REGIAO SOBRAL',	'12/09/2021',	18420,	2593,	0,	30,	0,			0, #264-277
         'Nordeste','RN',	'Currais Novos',    	24,	240310,	24004,	'4ª REGIAO DE SAUDE',	'12/09/2021',	44786,	3951,	0,	83,	0,			0, #278-291
         'Nordeste','RN',	'Natal',            	24,	240810,	24007,	'7ª REGIAO DE SAUDE',	'12/09/2021',	884122,	99755,	9,2685, 0,			1, #292-305
         'Nordeste','PB',	'Alagoa Grande',    	25,	250030,	25003,	'3ª REGIAO',         	'12/09/2021',	28496,	4140,	0,	72,	0,			0, #306-319
         'Nordeste','PB',	'Pocinhos',         	25,	251200,	25016,	'16ª REGIAO',	        '12/09/2021',	18564,	1445,	0,	22,	0,			0, #320-333
         'Nordeste','PE',	'Caruaru',          	26,	260410,	26003,	'CARUARU',          	'12/09/2021',	361118,	34920,	18,709, 0,			0, #334-347
         'Nordeste','PE',	'Olinda',           	26,	260960,	26010,	'RECIFE',           	'12/09/2021',	392482,	24456,	60,981,	0,			1, #348-361
         'Nordeste','AL',	'Branquinha',       	27,	270110,	27003,	'3ª REGIAO DE SAUDE',	'12/09/2021',	10494,	700,	0,	14,	0,			0, #362-375
         'Nordeste','AL',	'Taquarana',        	27,	270910,	270070,	'7ª REGIAO DE SAUDE',	'12/09/2021',	19980,	746,	0,	24,	0,			0, #376-389
         'Nordeste','SE',	'Boquim',           	28,	280067,	28002,	'ESTANCIA',	            '12/09/2021',	26816,	2688,	0,	67,	0,			0, #390-403
         'Nordeste','SE',	'Telha',            	28,	280730,	28007,	'PROPRIA',          	'12/09/2021',	3227,	406,	0,	10,	0,			0, #404-417
         'Nordeste','BA',	'Aiquara',          	29,	290060,	29015,	'JEQUIE',              	'12/09/2021',	4446,	501,	0,	12,	0,			0, #418-431
         'Nordeste','BA',	'Wagner',           	29,	293340,	29011,	'ITABERABA',	        '12/09/2021',	9345,	960,	0,	9,	0,			0, #432-445
         'Sudeste',	'MG',	'Abre Campo',       	31,	310030,	31059,	'MANHUACU',         	'12/09/2021',	13454,	1267,	0,	16,	0,			0, #446-459
         'Sudeste',	'MG',	'Tombos',           	31,	316920,	31042,	'CARANGOLA',        	'12/09/2021',	8022,	1039,	0,	19,	0,			0, #460-473
         'Sudeste',	'ES',	'Castelo',          	32,	320140,	32004,	'SUL',	                '12/09/2021',	37534,	6616,	9, 126, 0,			0, #474-487
         'Sudeste',	'ES',	'Rio Bananal',      	32,	320435,	32001,	'CENTRAL',	            '12/09/2021',	19141,	2955,  14,	34,	0,			0, #488-501
         'Sudeste',	'RJ',	'Areal',            	33,	330022,	33003,	'CENTRO-SUL',       	'12/09/2021',	12572,	1647,	0,	51,	0,			0, #502-515
         'Sudeste',	'RJ',	'Trajano de Moraes',	33,	330590,	33009,	'SERRANA',          	'12/09/2021',	10626,	753,	0,	5,	0,			0, #516-529
         'Sudeste',	'SP',	'Agudos',           	35,	350070,	35062,	'BAURU',            	'12/09/2021',	37214,	4673,  -1,110,	0,			0, #530-543
         'Sudeste',	'SP',	'Tanabi',           	35,	355340,	35155,	'SAO JOSE DO RIO PRETO','12/09/2021',	25967,	4812,	0,112,	0,			0, #544-557
         'Sul', 	'PR',	'Alto Piquiri',     	41,	410070,	41012,	'12ª RS UMUARAMA',      '12/09/2021',	9836,	1107,	0,	27,	0,			0, #558-571
         'Sul',	    'PR',	'Uniflor',          	41,	412830,	41015,	'15ª RS MARINGA',   	'12/09/2021',	2605,	118,	0,	4,	0,			0, #572-585
         'Sul', 	'SC',	'Alfredo Wagner',   	42,	420070,	42007,	'GRANDE FLORIANOPOLIS',	'12/09/2021',	10036,	1098,	0,	7,	0,			0, #586-599
         'Sul', 	'SC',	'Urubici',          	42,	421890,	42013,	'SERRA CATARINENSE',	'12/09/2021',	11235,	731,	0,	25,	0,			0, #600-613
         'Sul', 	'RS',	'Agudo',            	43,	430010,	43001,	'REGIAO 01',        	'12/09/2021',	16461,	1840,	0,	29,	0,			0, #614-627
         'Sul', 	'RS',	'Tavares',          	43,	432135,	43005,	'REGIAO 05',        	'12/09/2021',	5481,	506,	0,	11,	0,			0, #628-641
    'Centro-Oeste',	'MS',	'Bonito',           	50,	500220,	50001,	'CAMPO GRANDE',     	'12/09/2021',	21976,	3205,  -1,	75,	0,			0, #642-655
    'Centro-Oeste',	'MS',	'Taquarussu',       	50,	500797,	50003,	'DOURADOS',	            '12/09/2021',	3588,	268,	0,	6,	0,			0, #656-669
    'Centro-Oeste',	'MT',	'Alta Floresta',    	51,	510025,	51001,	'ALTO TAPAJOS',     	'12/09/2021',	51782,	10121,	1,145,	0,			0, #670-683
    'Centro-Oeste',	'MT',	'Nova Guarita',     	51,	510880,	51010,	'NORTE MATOGROSSENSE',	'12/09/2021',	4519,	850,	0,	15,	0,			0, #684-697
    'Centro-Oeste',	'GO',	'Alto Horizonte',   	52,	520055,	52014,	'SERRA DA MESA',    	'12/09/2021',	6414,	1107,	0,	14,	0,			0, #698-711
    'Centro-Oeste',	'GO',	'Orizona',          	52,	521530,	52002,	'CENTRO SUL',	        '12/09/2021',	15615,	617,	0,	30,	0,			0,] #712-725

tupla = ('Norte',	'RO',	'Alta Floresta DOeste',	11,	110001,	11005,	'ZONA DA MATA',	        '12/09/2021',	22945,	4069,	0,	66,	0,			0,
         'Norte',	'RO',	'Vale do Paraíso',	    11,	110180,	11003,	'CENTRAL',	            '12/09/2021',	6825,	847,	0,	26,	0,			0,
         'Norte',	'AC',	'Acrelândia',	        12,	120001,	12002,	'BAIXO ACRE E PURUS'	'12/09/2021',	15256,	1796,	0,	37,	0,			0,
         'Norte'	'AC',	'Xapuri',           	12,	120070,	12001,	'ALTO ACRE',        	'12/09/2021',	19323,	3029,	0,	31,	0,			0,
         'Norte',	'AM',	'Anori',             	13,	130010,	13002,	'RIO NEGRO E SOLIMOES',	'12/09/2021',	21010,	1918,	0,	33,	0,			0,
         'Norte',	'AM',	'Urucurituba',	        13,	130440,	13004,	'MEDIO AMAZONAS'	    '12/09/2021',   23065,	2727,	0,	36,	0,			0,
         'Norte',	'RR',	'Amajari',          	14,	140002,	14001,	'CENTRO NORTE',     	'12/09/2021',   12796,	1170,	2,	21,	0,			0,
         'Norte',	'RR',	'São Luiz',             14,	140060,	14002,	'SUL',              	'12/09/2021',   7986,	689,	0,	12,	0,			0,
         'Norte',	'PA',	'Água Azul do Norte',	15,	150034,	15001,	'ARAGUAIA',	            '12/09/2021',   27430,	1259,	0,	18,	0,			0,
         'Norte',	'PA',	'Viseu',            	15,	150830,	15009,	'RIO CAETES',       	'12/09/2021',   61403,	1549,	0,	36,	0,			0,
         'Norte',	'AP',	'Serra do Navio',	    16,	160005,	16001,	'AREA CENTRAL',     	'12/09/2021',	5397,	1311,	0,	5,	0,			0,
         'Norte',	'AP',	'Tartarugalzinho',  	16,	160070,	16002,	'AREA NORTE',       	'12/09/2021',	17315,	1966,	0,	13,	0,			0,
         'Norte',	'TO',	'Almas',            	17,	170040,	17003,	'SUDESTE',	            '12/09/2021',	7055,	239,	0,	5,	0,			0,
         'Norte',	'TO',	'Palmas',           	17,	172100,	17006,	'CAPIM DOURADO',    	'12/09/2021',	299127,	51115,	58,	625,0,			1,
         'Nordeste','MA',	'Afonso Cunha',     	21,	2100100,210050,	'CAXIAS',	            '12/09/2021',	6524,	267,	0,	3,	0,			0,
         'Nordeste','MA',	'Viana',            	21,	211280,	21018,	'VIANA',            	'12/09/2021',	52441,	330,	0,	42,	0,			0,
         'Nordeste','PI',	'Altos',             	22,	220040,	22004,	'ENTRE RIOS',       	'12/09/2021',	40524,	4675,	8,	90,	0,			1,
         'Nordeste','PI',	'Wall Ferraz',         	22,	221170,	22009,	'VALE DO RIO GUARIBAS',	'12/09/2021',	4462,	333,	0,	3,	0,			0,
         'Nordeste','CE',	'Acarape',          	23,	230015,	23003,	'3ª REGIAO MARACANAU',	'09/09/2021',	14929,	2837,	0,	32,	0,			0,
         'Nordeste','CE',	'Varjota',          	23,	231395,	23011,	'11ª REGIAO SOBRAL',	'12/09/2021',	18420,	2593,	0,	30,	0,			0,
         'Nordeste','RN',	'Currais Novos',    	24,	240310,	24004,	'4ª REGIAO DE SAUDE',	'12/09/2021',	44786,	3951,	0,	83,	0,			0,
         'Nordeste','RN',	'Natal',            	24,	240810,	24007,	'7ª REGIAO DE SAUDE',	'12/09/2021',	884122,	99755,	9,2685, 0,			1,
         'Nordeste','PB',	'Alagoa Grande',    	25,	250030,	25003,	'3ª REGIAO',         	'12/09/2021',	28496,	4140,	0,	72,	0,			0,
         'Nordeste','PB',	'Pocinhos',         	25,	251200,	25016,	'16ª REGIAO',	        '12/09/2021',	18564,	1445,	0,	22,	0,			0,
         'Nordeste','PE',	'Caruaru',          	26,	260410,	26003,	'CARUARU',          	'12/09/2021',	361118,	34920,	18,709, 0,			0,
         'Nordeste','PE',	'Olinda',           	26,	260960,	26010,	'RECIFE',           	'12/09/2021',	392482,	24456,	60,981,	0,			1,
         'Nordeste','AL',	'Branquinha',       	27,	270110,	27003,	'3ª REGIAO DE SAUDE',	'12/09/2021',	10494,	700,	0,	14,	0,			0,
         'Nordeste','AL',	'Taquarana',        	27,	270910,	270070,	'7ª REGIAO DE SAUDE',	'12/09/2021',	19980,	746,	0,	24,	0,			0,
         'Nordeste','SE',	'Boquim',           	28,	280067,	28002,	'ESTANCIA',	            '12/09/2021',	26816,	2688,	0,	67,	0,			0,
         'Nordeste','SE',	'Telha',            	28,	280730,	28007,	'PROPRIA',          	'12/09/2021',	3227,	406,	0,	10,	0,			0,
         'Nordeste','BA',	'Aiquara',          	29,	290060,	29015,	'JEQUIE',              	'12/09/2021',	4446,	501,	0,	12,	0,			0,
         'Nordeste','BA',	'Wagner',           	29,	293340,	29011,	'ITABERABA',	        '12/09/2021',	9345,	960,	0,	9,	0,			0,
         'Sudeste',	'MG',	'Abre Campo',       	31,	310030,	31059,	'MANHUACU',         	'12/09/2021',	13454,	1267,	0,	16,	0,			0,
         'Sudeste',	'MG',	'Tombos',           	31,	316920,	31042,	'CARANGOLA',        	'12/09/2021',	8022,	1039,	0,	19,	0,			0,
         'Sudeste',	'ES',	'Castelo',          	32,	320140,	32004,	'SUL',	                '12/09/2021',	37534,	6616,	9, 126, 0,			0,
         'Sudeste',	'ES',	'Rio Bananal',      	32,	320435,	32001,	'CENTRAL',	            '12/09/2021',	19141,	2955,  14,	34,	0,			0,
         'Sudeste',	'RJ',	'Areal',            	33,	330022,	33003,	'CENTRO-SUL',       	'12/09/2021',	12572,	1647,	0,	51,	0,			0,
         'Sudeste',	'RJ',	'Trajano de Moraes',	33,	330590,	33009,	'SERRANA',          	'12/09/2021',	10626,	753,	0,	5,	0,			0,
         'Sudeste',	'SP',	'Agudos',           	35,	350070,	35062,	'BAURU',            	'12/09/2021',	37214,	4673,  -1,110,	0,			0,
         'Sudeste',	'SP',	'Tanabi',           	35,	355340,	35155,	'SAO JOSE DO RIO PRETO','12/09/2021',	25967,	4812,	0,112,	0,			0,
         'Sul', 	'PR',	'Alto Piquiri',     	41,	410070,	41012,	'12ª RS UMUARAMA',      '12/09/2021',	9836,	1107,	0,	27,	0,			0,
         'Sul',	    'PR',	'Uniflor',          	41,	412830,	41015,	'15ª RS MARINGA',   	'12/09/2021',	2605,	118,	0,	4,	0,			0,
         'Sul', 	'SC',	'Alfredo Wagner',   	42,	420070,	42007,	'GRANDE FLORIANOPOLIS',	'12/09/2021',	10036,	1098,	0,	7,	0,			0,
         'Sul', 	'SC',	'Urubici',          	42,	421890,	42013,	'SERRA CATARINENSE',	'12/09/2021',	11235,	731,	0,	25,	0,			0,
         'Sul', 	'RS',	'Agudo',            	43,	430010,	43001,	'REGIAO 01',        	'12/09/2021',	16461,	1840,	0,	29,	0,			0,
         'Sul', 	'RS',	'Tavares',          	43,	432135,	43005,	'REGIAO 05',        	'12/09/2021',	5481,	506,	0,	11,	0,			0,
    'Centro-Oeste',	'MS',	'Bonito',           	50,	500220,	50001,	'CAMPO GRANDE',     	'12/09/2021',	21976,	3205,  -1,	75,	0,			0,
    'Centro-Oeste',	'MS',	'Taquarussu',       	50,	500797,	50003,	'DOURADOS',	            '12/09/2021',	3588,	268,	0,	6,	0,			0,
    'Centro-Oeste',	'MT',	'Alta Floresta',    	51,	510025,	51001,	'ALTO TAPAJOS',     	'12/09/2021',	51782,	10121,	1,145,	0,			0,
    'Centro-Oeste',	'MT',	'Nova Guarita',     	51,	510880,	51010,	'NORTE MATOGROSSENSE',	'12/09/2021',	4519,	850,	0,	15,	0,			0,
    'Centro-Oeste',	'GO',	'Alto Horizonte',   	52,	520055,	52014,	'SERRA DA MESA',    	'12/09/2021',	6414,	1107,	0,	14,	0,			0,
    'Centro-Oeste',	'GO',	'Orizona',          	52,	521530,	52002,	'CENTRO SUL',	        '12/09/2021',	15615,	617,	0,	30,	0,			0,)

print ('Agora irá aparecer os caos acumulados no estado do Rio de Janeiro!\nTanto na lista quanto na tupla.\n')

casoAcumuladoRJlista = lista[512] + lista[526]
casoAcumuladoRJtupla = tupla[511] + tupla[525]

print ('Na lista os os casos acumulados do Rio de Janeiro são', casoAcumuladoRJlista)
print ('Na tupla os os casos acumulados do Rio de Janeiro são', casoAcumuladoRJtupla)

print ('\nSerão apresentados agora os óbitos acumulados dos estados!\n')
print (lista [1], lista[12]+lista[26])
print (lista [29], lista[39]+lista[53])
print (lista [56], lista[67]+lista[80])
print (lista [83], lista[95]+lista[108])
print (lista [111], lista[123]+lista[134])
print (lista [139], lista[151]+lista[162])
print (lista [167], lista[178]+lista[192])
print (lista [195], lista[206]+lista[218])
print (lista [223], lista[234]+lista[246])
print (lista [251], lista[262]+lista[274])
print (lista [279], lista[290]+lista[304])
print (lista [307], lista[318]+lista[332])
print (lista [335], lista[346]+lista[360])
print (lista [363], lista[374]+lista[388])
print (lista [391], lista[402]+lista[416])
print (lista [419], lista[430]+lista[444])
print (lista [447], lista[458]+lista[472])
print (lista [475], lista[486]+lista[500])
print (lista [503], lista[514]+lista[528])
print (lista [531], lista[542]+lista[556])
print (lista [559], lista[570]+lista[584])
print (lista [587], lista[598]+lista[612])
print (lista [615], lista[626]+lista[640])
print (lista [643], lista[654]+lista[668])
print (lista [671], lista[682]+lista[696])
print (lista [699], lista[710]+lista[724])

print ('\nInfelizemente os dados de óbitos novos para o estado da Paraíba estão errados.\nSerá apresentado agora os dados corretos.\nAs alterações serão feitas tanto na Lista quanto na tupla.\n')
atualizacaoObitosnovosPB = (lista[319]+lista[333])-10
lista[333] = atualizacaoObitosnovosPB
print ('Óbitos novos para o estado da Paraíba na lista é de ',lista [699],atualizacaoObitosnovosPB)
print ('Não foi possível apresentar os resultados na tupla, pois, não é possível sobrescrever informações em uma tupla!\n')

listanova = ['Norte',	'RR',	'Amajari',	    14,	140002,	14001,	'CENTRO NORTE',	'12/09/2021',	12796,	1170,	2,	21,	0,			0,
             'Norte',	'RR',	'Alto Alegre',	14,	140005,	14001,	'CENTRO NORTE',	'12/09/2021',	15510,	1604,	4,	37,	0,			1,
             'Norte',	'RR',	'Boa Vista',	14,	140010,	14001,	'CENTRO NORTE',	'12/09/2021',  399213, 95998, 111,1501,	1,			1,
             'Norte',	'RR',	'Bonfim',   	14,	140015,	14001,	'CENTRO NORTE',	'12/09/2021',	12409,	2495,	6,	33,	0,			1,
             'Norte',	'RR',	'Cantá',    	14,	140017,	14001,	'CENTRO NORTE',	'12/09/2021',	18335,	2460,	0,	39,	0,			1,
             'Norte',	'RR',	'Carcará',	    14,	140020,	14002,	'SUL',      	'12/09/2021',	21926,	2692,	2,	56,	0,			0,
             'Norte',	'RR',	'Caroebe',  	14,	140023,	14002,	'SUL',      	'12/09/2021',	10169,	1997,	0,	21,	0,			0,
             'Norte',	'RR',	'Iracema',  	14,	140028,	14002,	'SUL',      	'12/09/2021',	11950,	1371,	0,	15,	0,			0,
             'Norte',	'RR',	'Mucajá',   	14,	140030,	14001,	'CENTRO NORTE',	'12/09/2021',	17853,	2328,	0,	43,	0,			1,
             'Norte',	'RR',	'Normandia',	14,	140040,	14001,	'CENTRO NORTE',	'12/09/2021',	11290,	597,	2,	31,	0,			0,
             'Norte',	'RR',	'Pacaraima',	14,	140045,	14001,	'CENTRO NORTE',	'12/09/2021',	17401,	2358,	5,	46,	0,			0,
             'Norte',	'RR',	'Rorainópolis',	14,	140047,	14002,	'SUL',      	'12/09/2021',	30163,	3364,	1,	68,	0,			0,
      'Norte',	'RR',	'São João da Baliza',	14,	140050,	14002,	'SUL',      	'12/09/2021',	8201,	1632,	0,	12,	0,			0,
      'Norte',	'RR',	'São Luiz',         	14,	140060,	14002,	'SUL',      	'12/09/2021',	7986,	689,	0,	12,	0,			0,
      'Norte',	'RR',	'Uiramutã',         	14,	140070,	14001,	'CENTRO NORTE',	'12/09/2021',	10559,	1189,	0,	15,	0,			0,]

print ('Para termos um dado mais robusto, todas as cidades do estado de Roraíma serão adicionadas a lista')

lista.append(listanova)
print ('\nAgora iremos verificar se a soma dos dados da cidade de Caruaru no dia 18/08/2020 é igual aos dados da lista.\nSerá somado os Caso acumulado, Caos novos, Obitos acumulados, Obitos novos.\n')
dadosanopassado = 5868
dadosesteano = (lista[344]+lista[345]+lista[346]+lista[347])

print("A afirmativa que os dados são iguais é",dadosanopassado == dadosesteano)
print('O total da data 18/08/2020 é',dadosanopassado,'e o total da data 12/09/2021 é',dadosesteano)

print('\nO maior valor numérico de óbitos novos é', lista[361])
print('O menor valor numérico de óbitos novos é',lista[487])

print ('\nSegue os casos de algumas cidades do Piauí.\nAs informações foram organizadas em um dicionário.')
casosNovosPI = {'Agricolândia':[0],'Água branca':[0],'Barras':[1],'Currais':[0],'Oeiras':[1],'Teresina':[44]}
print (casosNovosPI)

print('\nOs novos óbitos da cidade do Piauí em Teresina é de', casosNovosPI['Teresina'])

# lista2 = (lista[6],lista[20],lista[34],lista[47],lista[61],lista[75],lista[88],lista[102],lista[116],lista[130],lista[144],lista[158],lista[172],lista[186],lista[200],lista[214],lista[228],lista[242],lista[256],lista[270],lista[284],lista[298],lista[312],lista[326],lista[340],lista[354],lista[368],lista[382],lista[396],lista[410],lista[424],lista[438],lista[452],lista[466],lista[480],lista[494],lista[508],lista[522],lista[536],lista[550],lista[564],lista[578],lista[592],lista[606],lista[620],lista[634],lista[648],lista[662],lista[676],lista[690],lista[704],lista[718])
# lista.remove(lista2)