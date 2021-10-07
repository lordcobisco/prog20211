# dados gerais de covid dos estados de 04/10
# dados da população geral são estimativas do IBGE para 2021

# LEGENDA 
# valor0 = população
# valor1 = casos acumulados
# valor2 = casos novos
# valor3 = obtos acumulados
# valor4 = obtos novos

Estados = ['AM,PB,RJ,GO']

# Questão A

# LISTAS

dados_gerais_lista_AM = [4269995,427000,55,13729,1]
Baixo_Amazonas = [19207,997,0,12,0]
Regional_Purus = [34308,2671,0,27,0]
Rio_Madeira = [41161,2509,0,69,0]
Rio_Negro = [13081,695,0,22,0]
Regional_Jurua = [28294,6726,0,56,0]
Manaus_entorno_e_alto_Rio_Negro = [30225,1028,0,25,0]
Rio_Negro_e_Solimões = [28637,2638,0,25,0]
Alto_Solimões = [17609,1600,0,39,0]
Médio_Amazonas = [101337,10538,5,316,0]
Triangulo = [2755,954,0,7,0]

dados_gerais_lista_PB = [4059905,442000,29,9325,5]
PBR1 = [19588,2467,0,39,0]
PBR2 = [14489,2087,1,25,0]
PBR3 = [20849,1756,3,31,0]
PBR4 = [4892,709,1,9,0]
PBR5 = [2238,178,0,4,0]
PBR6 = [2128,222,0,4,0]
PBR7 = [5640,533,0,5,0]
PBR8 = [7342,534,0,6,0]
PBR9 = [18034,1436,4,33,0]
PBR10 = [8347,1012,0,14,0]

dados_gerais_lista_RJ = [17463349,1290000,2323,66648,183]
Baia_da_Ilha_Grande = [203785,16886,65,535,4]
Noroeste = [203785,16886,65,535,4]
Baixada_Litorânea = [132400,7338,7,480,3]
Médio_Paraíba = [184412,29801,64,658,0]
Metropolitana1 = [510906,23708,16,895,6]
Serrana = [27446,2022,0,50,0]
Norte = [16301,1762,2,16,0]
Centro_Sul = [8561,821,0,32,0]
Metropolitana2 = [240592,15427,28,824,1]

dados_gerais_lista_GO = [7206589,870000,1460,23637,68]
Central = [8773,1882,31,37,0]
Pirineus = [20042,506,0,43,0]
Sudoeste1 = [22366,2603,1,61,0]
Oeste2 = [2516,230,0,4,0]
Entorno_Norte = [5735,336,0,10,0]
Sul = [1850,185,0,4,0]
Entorno_Sul = [212440,9595,3,330,0]
Serra_da_Mesa = [6414,1137,0,14,0]
Estrada_de_Ferro = [8660,836,2,11,0]
Nordeste2 = [6111,860,1,23,0]

# TUPLAS

dados_gerais_tupla_AM = (4269995,427000,55,13729,1)
Baixo_Amazonas = (19207,997,0,12,0)
Regional_Purus = (34308,2671,0,27,0)
Rio_Madeira = (41161,2509,0,69,0)
Rio_Negro = (13081,695,0,22,0)
Regional_Jurua = (28294,6726,0,56,0)
Manaus_entorno_e_alto_Rio_Negro = (30225,1028,0,25,0)
Rio_Negro_e_Solimões = (28637,2638,0,25,0)
Alto_Solimões = (17609,1600,0,39,0)
Médio_Amazonas = (101337,10538,5,316,0)
Triangulo = (2755,954,0,7,0)

dados_gerais_tupla_PB = (4059905,442000,29,9325,5)
PBR1 = (19588,2467,0,39,0)
PBR2 = (14489,2087,1,25,0)
PBR3 = (20849,1756,3,31,0)
PBR4 = (4892,709,1,9,0)
PBR5 = (2238,178,0,4,0)
PBR6 = (2128,222,0,4,0)
PBR7 = (5640,533,0,5,0)
PBR8 = (7342,534,0,6,0)
PBR9 = (18034,1436,4,33,0)
PBR10 = (8347,1012,0,14,0)

dados_gerais_tupla_RJ = (17463349,1290000,2323,66648,183)
Baia_da_Ilha_Grande = (203785,16886,65,535,4)
Noroeste = (203785,16886,65,535,4)
Baixada_Litorânea = (132400,7338,7,480,3)
Médio_Paraíba = (184412,29801,64,658,0)
Metropolitana1 = (510906,23708,16,895,6)
Serrana = (27446,2022,0,50,0)
Norte = (16301,1762,2,16,0)
Centro_Sul = (8561,821,0,32,0)
Metropolitana2 = (240592,15427,28,824,1)

dados_gerais_tupla_GO = (7206589,870000,1460,23637,68)
Central = (8773,1882,31,37,0)
Pirineus = (20042,506,0,43,0)
Sudoeste1 = (22366,2603,1,61,)
Oeste2 = (2516,230,0,4,0)
Entorno_Norte = (5735,336,0,10,0)
Sul = (1850,185,0,4,0)
Entorno_Sul = (212440,9595,3,330,0)
Serra_da_Mesa = (6414,1137,0,14,0)
Estrada_de_Ferro = (8660,836,2,11,0)
Nordeste2 = (6111,860,1,23,0)

# Questão B

print(dados_gerais_lista_RJ [1], dados_gerais_tupla_RJ [1])

# Questão C

print(dados_gerais_lista_AM [3], dados_gerais_lista_PB [3], dados_gerais_lista_RJ [3], dados_gerais_lista_GO [3])

# Questão D

correção_de_Obtos_PB = (int(input in dados_gerais_lista_PB('Inserir número de obtos corrigidos (15): Obtos novos = ')))
correção_de_Obtos_PB = (int(input in dados_gerais_tupla_PB('Inserir número de obtos corrigidos (15): Obtos novos =  ')))

# Questão E

# Deu erro tanto na lista quanto na tupla

# Questão F

dados_gerais_lista_AM = [4269995,427000,55,13729,1]
Baixo_Amazonas = [19207,997,0,12,0]
Regional_Purus = [34308,2671,0,27,0]
Rio_Madeira = [41161,2509,0,69,0]
Rio_Negro = [13081,695,0,22,0]
Regional_Jurua = [28294,6726,0,56,0]
Manaus_entorno_e_alto_Rio_Negro = [30225,1028,0,25,0]
Rio_Negro_e_Solimões = [28637,2638,0,25,0]
Alto_Solimões = [17609,1600,0,39,0]
Médio_Amazonas = [101337,10538,5,316,0]
Triangulo = [2755,954,0,7,0]

lista_cidades_AM_questaoF = [ 'Alvarães', 16041,2908,0,46,0, 'Amaturá', 11536,2393,1,18,0, 'Anamã', 13614,2013,0,10,0, 'Anori', 21010,1921,0,33,0, 'Apuí', 21973,1485,0,32,0, 'Atalaia_do_Norte', 19921,2834,0,10,0, 'Autazes', 39565,2906,0,95,0,
'Barcelos', 27502,4490,0,60,0, 'Barreirinha', 32041,2438,0,63,0, 'Benjamin_Constant', 42984,2712,0,88,0, 'Beruri', 19679,2294,0,34,0, 'Boa_Vista_do_Ramos', 19207,997,0,12,0, 'Boca_do_Acre', 34308,2671,0,27,0, 'Borba', 41161,2509,0,69,0, 'Caapiranga', 13081,695,0,22,0,
'Canutama', 15629,1461,0,8,0, 'Caruari', 28294,6726,0,56,0, 'Careiro', 37869,4514,0,85,0, 'Careiro_da_Várzea', 30225,1028,0,25,0, 'Coari', 85097,9549,0,233,0, 'Codajás', 28637,2638,0,25,0, 'Eirunepé', 35273,4206,0,33,0, 'Envira', 20033,2712,0,13,0, 'Fonte_Boa', 17609,1600,0,39,0, 'Guajará', 16678,1693,0,28,0,
'Humaitá', 55080,8063,0,151,0, 'Ipixuna', 29689,5498,0,19,0, 'Iranduba', 48296,8966,0,166,0, 'Itacoatiara', 101337,10538,5,316,0, 'Itamarati', 7851,965,0,9,0, 'Itapiranga', 9148,3097,0,43,0, 'Juruá', 14712,985,0,16,0, 'Jutaí', 14317,3092,6,35,0, 'Lábrea', 46069,7044,0,80,0, 'Manacapuru', 97377,9602,2,398,0,
'Manaquiri', 32105,1582,0,46,0, 'Manaus', 2182763,187452,522,9169, 'Manicoré', 55751,4697,1,103,0, 'Maraã', 18224,2561,2,23,0, 'Maués', 63905,4930,0,129,0, 'Nhamundá', 21173,1884,0,37,0, 'Nova_Olinda_do_Norte', 37378,2635,0,69,0, 'Novo_Airão', 19454,2416,5,33,0, 'Novo_aripuanã', 25644,2046,0,31,0,
'Parintins', 114273,10054,0,357,0, 'Pauini', 19426,2767,0,22,0, 'Presidente_Figueiredo', 36279,6261,0,103,0, 'Rio_Preto_da_Eva', 33347,4879,0,83,0, 'Santa_Isabel_do_Rio_Negro', 25156,2748,0,53,0, 'Santo_Antônio_do_Içá', 21602,1861,0,45,0,
'São_Gabriel_da_Cachoeira', 45564,8141,1,108,0, 'São_Paulo_de_Olivença', 39299,5301,0,66,0, 'São_Sebastião_do_Uatumã', 14020,1612,0,19,0, 'Silves', 9171,1386,0,22,0, 'Tabatinga', 65844,3341,0,126,0, 'Tapauá',17156,1972,0,24,0,
'Tefé', 59849,9840,0,198,0, 'Tonantins', 18755,1379,2,33,0, 'Uarini', 13540,1970,0,26,0 , 'Urucá', 16256,2545,0,54,0, 'Urucurituba', 23065,2728,0,36,0]

lista_cidades_AM_questaoF.append(dados_gerais_lista_AM)

# QUESTÃO G

Baixo_Amazonas.remove([0], [1], [2], [3], [4])
Regional_Purus.remove([0], [1], [2], [3], [4])
Rio_Madeira.remove([0], [1], [2], [3], [4])
Rio_Negro.remove([0], [1], [2], [3], [4])
Regional_Jurua.remove([0], [1], [2], [3], [4])
Manaus_entorno_e_alto_Rio_Negro.remove([0], [1], [2], [3], [4])
Rio_Negro_e_Solimões.remove([0], [1], [2], [3], [4])
Alto_Solimões.remove([0], [1], [2], [3], [4])
Médio_Amazonas.remove([0], [1], [2], [3], [4])
Triangulo.remove([0], [1], [2], [3], [4])

# QUESTÃO J

Alvarães = [16041,2908,0,46,0]
Amaturá = [11536,2393,1,18,0]
Anamã = [13614,2013,0,10,0]
Anori =[21010,1921,0,33,0]
Apuí = [21973,1485,0,32,0]
Atalaia_do_Norte = [19921,2834,0,10,0]
Autazes = [39565,2906,0,95,0]
Barcelos = [27502,4490,0,60,0]
Barreirinha = [32041,2438,0,63,0]
Benjamin_Constant = [42984,2712,0,88,0]
Beruri = [19679,2294,0,34,0]
Boa_Vista_do_Ramos = [19207,997,0,12,0]
Boca_do_Acre = [34308,2671,0,27,0]
Borba = [41161,2509,0,69,0]
Caapiranga = [13081,695,0,22,0]
Canutama = [15629,1461,0,8,0]
Caruari = [28294,6726,0,56,0]
Careiro = [37869,4514,0,85,0]
Careiro_da_Várzea = [30225,1028,0,25,0]
Coari = [85097,9549,0,233,0]
Codajás = [28637,2638,0,25,0]
Eirunepé = [35273,4206,0,33,0]
Envira = [20033,2712,0,13,0]
Fonte_Boa = [17609,1600,0,39,0]
Guajará = [16678,1693,0,28,0]
Humaitá = [55080,8063,0,151,0]
Ipixuna = [29689,5498,0,19,0]
Iranduba = [48296,8966,0,166,0]
Itacoatiara = [101337,10538,5,316,0]
Itamarati = [7851,965,0,9,0]
Itapiranga = [9148,3097,0,43,0]
Juruá = [14712,985,0,16,0]
Jutaí = [14317,3092,6,35,0]
Lábrea = [46069,7044,0,80,0]
Manacapuru = [97377,9602,2,398,0]
Manaquiri = [32105,1582,0,46,0]
Manaus = [2182763,187452,522,9169,5]
Manicoré =[55751,4697,1,103,0]
Maraã = [18224,2561,2,23,0]
Maués = [63905,4930,0,129,0]
Nhamundá = [21173,1884,0,37,0]
Nova_Olinda_do_Norte = [37378,2635,0,69,0]
Novo_Airão = [19454,2416,5,33,0]
Novo_aripuanã = [25644,2046,0,31,0]
Parintins = [114273,10054,0,357,0]
Pauini = [19426,2767,0,22,0]
Presidente_Figueiredo = [36279,6261,0,103,0]
Rio_Preto_da_Eva = [33347,4879,0,83,0]
Santa_Isabel_do_Rio_Negro = [25156,2748,0,53,0]
Santo_Antônio_do_Içá = [21602,1861,0,45,0]
São_Gabriel_da_Cachoeira = [45564,8141,1,108,0]
São_Paulo_de_Olivença = [39299,5301,0,66,0]
São_Sebastião_do_Uatumã = [14020,1612,0,19,0]
Silves = [9171,1386,0,22,0]
Tabatinga = [65844,3341,0,126,0]
Tapauá = [17156,1972,0,24,0]
Tefé = [59849,9840,0,198,0]
Tonantins = [18755,1379,2,33,0]
Uarini = [13540,1970,0,26,0]
Urucá = [16256,2545,0,54,0]
Urucurituba = [23065,2728,0,36,0]

Obtosnovos = (Alvarães [4],  Amaturá  [4], Anamã  [4], Anori  [4], Apuí  [4], Atalaia_do_Norte  [4], Autazes  [4],
Barcelos  [4], Barreirinha  [4], Benjamin_Constant  [4], Beruri  [4], Boa_Vista_do_Ramos  [4], Boca_do_Acre  [4], Borba  [4], Caapiranga  [4], Canutama  [4],
Caruari  [4], Careiro  [4], Careiro_da_Várzea  [4], Coari  [4], Codajás  [4], Eirunepé  [4], Envira  [4], Fonte_Boa  [4], Guajará  [4],
Humaitá  [4], Ipixuna  [4], Iranduba  [4], Itacoatiara  [4], Itamarati  [4], Itapiranga  [4], Juruá  [4],
Jutaí  [4], Lábrea  [4], Manacapuru  [4], Manaquiri  [4], Manaus  [4], Manicoré  [4], Maraã  [4], Maués  [4], Nhamundá  [4],
Nova_Olinda_do_Norte  [4], Novo_Airão  [4], Novo_aripuanã  [4], Parintins  [4], Pauini  [4], Presidente_Figueiredo  [4], Rio_Preto_da_Eva  [4],
Santa_Isabel_do_Rio_Negro  [4], Santo_Antônio_do_Içá  [4], São_Gabriel_da_Cachoeira  [4], São_Paulo_de_Olivença  [4], São_Sebastião_do_Uatumã  [4],
Silves  [4], Tabatinga  [4], Tapauá  [4], Tefé  [4], Tonantins  [4], Uarini  [4], Urucá  [4], Urucurituba  [4])
print(max(Obtosnovos))
print(min(Obtosnovos))

# Questão L
Teresina_PI = [864845,105410,21,2544,0]
print(Teresina_PI [2])