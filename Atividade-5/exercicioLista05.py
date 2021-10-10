
#print(' UF || cidade || coduf || nomeRegiaoSaude || codmun || codRegiaoSaude || data semanaEpi || populacaoTCU2019 || casosAcumulado || casosNovos || obitosAcumulado || obitosNovos || Recuperadosnovos || emAcompanhamentoNovos || interior/metropolitana')

#  Lista regioes de saúde do RN
from typing import KeysView


listRegioesRN = [[24,240010,24004,'4ÂªREGIAODESAUDE-CAICO','2020-08-03',32,11136,46,0,3,0,'','',0],
            [24,240680,24005,'5ÂªREGIAODESAUDE-SANTACRUZ','2020-12-23',52,4759,110,2,2,0,'','',0],
            [24,240020,24008,'8ÂªREGIAODESAUDE-ACU','2020-03-27',13,58017,0,0,0,0,'','',0],
            [24,240030,24003,'3ÂªREGIAODESAUDE-JOAOCAMARA','2020-03-27',13,11035,0,0,0,0,'','',0],
            [24,240690,24006,'6ÂªREGIAODESAUDE-PAUDOSFERROS','2020-08-01',31,3996,5,0,0,0,'','',0]]
# Tupla regioes de saúde do RN
tupleRegioesRN = ((24,240010,24004,'4ÂªREGIAODESAUDE-CAICO','2020-08-03',32,11136,46,0,3,0,'','',0),
                 (24,240680,24005,'5ÂªREGIAODESAUDE-SANTACRUZ','2020-12-23',52,4759,110,2,2,0,'','',0),
                 (24,240020,24008,'8ÂªREGIAODESAUDE-ACU','2020-03-27',13,58017,0,0,0,0,'','',0),
                 (24,240030,24003,'3ÂªREGIAODESAUDE-JOAOCAMARA','2020-03-27',13,11035,0,0,0,0,'','',0),
                 (24,240690,24006,'6ÂªREGIAODESAUDE-PAUDOSFERROS','2020-08-01',31,3996,5,0,0,0,'','',0))
# Lista regiões de saúde  da PB
listRegioesPB = [[25,250010,25011,'11ÂªREGIAO','2020-03-27',13,10234,0,0,0,0,'','',0],
            [25,250020,25007,'7ÂªREGIAO','2020-03-27',13,5640,0,0,0,0,'','',0],
            [25,250030,25003,'3ÂªREGIAO','2020-03-27',13,28496,0,0,0,0,'','',0],
            [25,250050,25002,'2ÂªREGIAO','2020-03-27',13,14489,0,0,0,0,'','',0],
            [25,250053,25015,'15ÂªREGIAO','2020-03-27',13,5492,0,0,0,0,'','',0]]
# Tupla regiões de saúde  da PB
tupleRegioesPB = ((25,250010,25011,'11ÂªREGIAO','2020-03-27',13,10234,0,0,0,0,'','',0),
                (25,250020,25007,'7ÂªREGIAO','2020-03-27',13,5640,0,0,0,0,'','',0),
                (25,250030,25003,'3ÂªREGIAO','2020-03-27',13,28496,0,0,0,0,'','',0),
                (25,250050,25002,'2ÂªREGIAO','2020-03-27',13,14489,0,0,0,0,'','',0),
                (25,250053,25015,'15ÂªREGIAO','2020-03-27',13,5492,0,0,0,0,'','',0))
# Lista regiões de saúde  do CE
listRegioesCE = [[23,230020,23012,'12ÂªREGIAOACARAU','2020-04-11',15,62641,0,0,0,0,'','',0],
            [23,230020,23012,'12ÂªREGIAOACARAU','2020-07-31',31,62641,2464,43,54,0,'','',0],
            [23,230010,23019,'19ÂªREGIAOBREJOSANTO','2020-08-02',32,11737,56,1,2,0,'','',0],
            [23,230015,23003,'3ÂªREGIAOMARACANAU','2020-08-03',32,14929,1162,1,14,0,'','',0],
            [23,230030,23018,'18ÂªREGIAOIGUATU','2020-08-03',32,54270,474,2,24,0,'','',0]]
# tupla regiões de saúde  do CE
tupleRegioesCE = ((23,230020,23012,'12ÂªREGIAOACARAU','2020-04-11',15,62641,0,0,0,0,'','',0),
                (23,230020,23012,'12ÂªREGIAOACARAU','2020-07-31',31,62641,2464,43,54,0,'','',0),
                (23,230010,23019,'19ÂªREGIAOBREJOSANTO','2020-08-02',32,11737,56,1,2,0,'','',0),
                (23,230015,23003,'3ÂªREGIAOMARACANAU','2020-08-03',32,14929,1162,1,14,0,'','',0),
                (23,230030,23018,'18ÂªREGIAOIGUATU','2020-08-03',32,54270,474,2,24,0,'','',0))
# Lista regiões de saúde  do PE
listRegioesPE = [[26,260005,26010,'RECIFE','2020-08-02',32,99990,656,10,86,1,'','',1],
            [26,260010,26001,'AFOGADOSDAINGAZEIRA','2020-08-01',31,37259,214,5,7,0,'','',0],
            [26,260020,26009,'PETROLINA','2020-08-01',31,19635,98,0,1,0,'','',0],
            [26,260030,26003,'CARUARU','2020-08-02',32,24885,469,4,24,0,'','',0],
            [26,260040,26008,'PALMARES','2020-08-01',31,36771,862,4,37,0,'','',0]]
# Tupla regiões de saúde  do PE
tupleRegioesPE = ((26,260005,26010,'RECIFE','2020-08-02',32,99990,656,10,86,1,'','',1),
                (26,260010,26001,'AFOGADOSDAINGAZEIRA','2020-08-01',31,37259,214,5,7,0,'','',0),
                (26,260020,26009,'PETROLINA','2020-08-01',31,19635,98,0,1,0,'','',0),
                (26,260030,26003,'CARUARU','2020-08-02',32,24885,469,4,24,0,'','',0),
                (26,260040,26008,'PALMARES','2020-08-01',31,36771,862,4,37,0,'','',0))
# Lista regiões de saúde da BA
listRegioesBA = [[29,290010,29023,'SEABRA','2020-08-01',31,8739,8,2,0,0,'','',0],
            [29,290020,29017,'PAULOAFONSO','2020-08-01',31,20086,39,0,0,0,'','',0],
            [29,290030,29001,'ALAGOINHAS','2020-08-01',31,15159,71,0,2,0,'','',0],
            [29,290035,29019,'RIBEIRADOPOMBAL','2020-08-01',31,17040,57,0,1,0,'','',0],
            [29,290040,29025,'SERRINHA','2020-08-01',31,16970,53,0,1,0,'','',0]]
# Tupla regiões de saúde da BA
tupleRegioesBA = ((29,290010,29023,'SEABRA','2020-08-01',31,8739,8,2,0,0,'','',0),
                (29,290020,29017,'PAULOAFONSO','2020-08-01',31,20086,39,0,0,0,'','',0),
                (29,290030,29001,'ALAGOINHAS','2020-08-01',31,15159,71,0,2,0,'','',0),
                (29,290035,29019,'RIBEIRADOPOMBAL','2020-08-01',31,17040,57,0,1,0,'','',0),
                (29,290040,29025,'SERRINHA','2020-08-01',31,16970,53,0,1,0,'','',0))
# Lista Regiões de saúde do MA
listRegioesMA = [[21,210193,21010,'PEDREIRAS','2020-09-04',36,6043,49,0,3,0,'','',0],
            [21,210197,21019,'ZEDOCA','2020-08-01',31,9287,13,0,2,0,'','',0],
            [21,210200,21014,'SANTAINES','2020-08-01',31,41630,757,2,18,0,'','',0],
            [21,210203,21001,'ACAILANDIA','2020-08-01',31,34028,1342,0,8,1,'','',0],
            [21,210207,21002,'BACABAL','2020-08-01',31,16294,174,0,0,0,'','',0]]
# Tupla Regiões de saúde do MA
tupleRegioesMA = ((21,210193,21010,'PEDREIRAS','2020-09-04',36,6043,49,0,3,0,'','',0),
                (21,210197,21019,'ZEDOCA','2020-08-01',31,9287,13,0,2,0,'','',0),
                (21,210200,21014,'SANTAINES','2020-08-01',31,41630,757,2,18,0,'','',0),
                (21,210203,21001,'ACAILANDIA','2020-08-01',31,34028,1342,0,8,1,'','',0),
                (21,210207,21002,'BACABAL','2020-08-01',31,16294,174,0,0,0,'','',0))
# Lista regioes de saúde do RJ
listRegioesRJ = [[33,330010,33001,'BAIADAILHAGRANDE','2020-08-01',31,203785,3822,5,115,0,'','',0],
            [33,330015,33007,'NOROESTE','2020-08-01',31,11759,143,2,5,0,'','',0],
            [33,330020,33002,'BAIXADALITORANEA','2020-08-01',31,132400,651,33,42,0,'','',0],
            [33,330022,33003,'CENTRO-SUL','2020-08-01',31,12572,123,4,3,0,'','',0],
            [33,330023,33002,'BAIXADALITORANEA','2020-08-01',31,33870,243,0,10,0,'','',0]]
# Tupla regiões de saúde do RJ
tupleRegioesRJ = ((33,330010,33001,'BAIADAILHAGRANDE','2020-08-01',31,203785,3822,5,115,0,'','',0),
                (33,330015,33007,'NOROESTE','2020-08-01',31,11759,143,2,5,0,'','',0),
                (33,330020,33002,'(BAIXADALITORANEA','2020-08-01',31,132400,651,33,42,0,'','',0),
                (33,330022,33003,'CENTRO-SUL','2020-08-01',31,12572,123,4,3,0,'','',0),
                (33,330023,33002,'BAIXADALITORANEA','2020-08-01',31,33870,243,0,10,0,'','',0))
# Lista Regiões de saúde de SP
listRegioesSP = [[35,350010,35091,'ADAMANTINA','2020-08-01',31,35068,150,6,6,0,'','',0],
            [35,350020,35156,'JOSEBONIFACIO','2020-08-01',31,3562,40,0,3,0,'','',0],
            [35,350030,35142,'MANTIQUEIRA','2020-08-01',31,36305,145,7,4,0,'','',0],
            [35,350040,35142,'MANTIQUEIRA','2020-08-01',31,8180,6,0,1,0,'','',0],
            [35,350050,35074,'CIRCUITODASAGUAS','2020-08-01',31,18705,73,2,5,0,'','',0]]
# Tupla Regiçoes de saúde de SP
tupleRegioesSP = ((35,350010,35091,'ADAMANTINA','2020-08-01',31,35068,150,6,6,0,'','',0),
                (35,350020,35156,'JOSEBONIFACIO','2020-08-01',31,3562,40,0,3,0,'','',0),
                (35,350030,35142,'MANTIQUEIRA','2020-08-01',31,36305,145,7,4,0,'','',0),
                (35,350040,35142,'MANTIQUEIRA','2020-08-01',31,8180,6,0,1,0,'','',0),
                (35,350050,35074,'CIRCUITODASAGUAS','2020-08-01',31,18705,73,2,5,0,'','',0))
# Lista por regioes do país
listNordeste=[]
listNordeste.insert(0,listRegioesRN)
listNordeste.insert(1,listRegioesCE)
listNordeste.insert(2,listRegioesPB)
listNordeste.insert(3,listRegioesBA)
listNordeste.insert(4,listRegioesPE)
listNordeste.insert(5,listRegioesMA)

listSudeste = []
listSudeste.insert(0,listRegioesRJ)
listSudeste.insert(1,listRegioesSP)

listBR = []
listBR.insert(0,listNordeste)
listBR.insert(1,listSudeste)

#tupla por regioes do país
tupleNordeste = (tupleRegioesRN,tupleRegioesCE,tupleRegioesPB,tupleRegioesBA,tupleRegioesPE,tupleRegioesMA)
tupleSudeste = (tupleRegioesRJ,tupleRegioesSP)
tupleBR = (tupleNordeste,tupleSudeste)
#faca o print dos casos acumulados para o estado do rio de janeiro (tupla/lista)
listRJ = listSudeste[0]
tupleRJ = tupleSudeste[0]
contListCasosAcumuladosRJ = 0
contTupleCasosAcumuladosRJ= 0

# Printando::::::::
for cont in listRJ:
    contListCasosAcumuladosRJ = contListCasosAcumuladosRJ + cont[7]
print('============================================================\n')
print('Casos Acumulados de Covid-19 para o Estado do RJ in Lista: ',contListCasosAcumuladosRJ)
print('============================================================\n')
for cont in tupleRJ:
    contTupleCasosAcumuladosRJ = contTupleCasosAcumuladosRJ + cont[7]
print('Casos Acumulados de Covid-19 para o Estado do RJ in Tupla: ',contTupleCasosAcumuladosRJ)
print('============================================================\n')

#Apresente todos os óbitos acumulados mostrando os casos apenas para caso do estados 
obAcumRN = 0
obAcumPB = 0
obAcumPE = 0
obAcumCE = 0
obAcumBA = 0
obAcumMA = 0
obAcumRJ = 0
obAcumSP = 0
for rg in listBR:
    for uf in rg:
        for info in uf:
            if 24==info[0]:
                #print('RN________________________________________')
                obAcumRN = obAcumRN + info[9]
                #print(info)
            if 25== info[0]:
                #print('PB________________________________________')
                obAcumPB = obAcumPB + info[9]
                #print(info)
            if 23==info[0]:
                #print('CE________________________________________')
                obAcumCE = obAcumCE + info[9]
                #print(info)
            if 26==info[0]:
                #print('PE________________________________________')
                obAcumPE = obAcumPE + info[9]
                #print(info)
            if 29==info[0]:
                #print('BA________________________________________')
                obAcumBA = obAcumBA + info[9]
                #print(info)
            if 21==info[0]:
                #print('MA________________________________________')
                obAcumMA = obAcumMA + info[9]
                #print(info)
            if 33==info[0]:
                #print('RJ________________________________________')
                obAcumRJ = obAcumRJ + info[9]
                #print(info)
            if 35==info[0]:
                #print('SP________________________________________')
                obAcumSP = obAcumSP + info[9]
                #print(info)

print('Óbitos Acumulados para o RN: ',obAcumRN)
print('Óbitos Acumulados para o CE: ',obAcumCE)
print('Óbitos Acumulados para o BA: ',obAcumBA)
print('Óbitos Acumulados para o PB: ',obAcumPB)
print('Óbitos Acumulados para o PE: ',obAcumPE)
print('Óbitos Acumulados para o SP: ',obAcumSP)
print('Óbitos Acumulados para o RJ: ',obAcumRJ)
print('Óbitos Acumulados para o MA: ',obAcumMA)

#Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10
#unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla,
#corrigindo os dados.
#info[8] = info[8] - 10
obtListNovosPB10 = 0
obtTupleNovosPB10 = 0
for RG in listBR:
    for UF in RG:
        for inf in UF:
            if inf[0]==25:
                inf[10] =- 2
                obtListNovosPB10 =  obtListNovosPB10 + inf[10]
                 
print('============================================================\n')
print('Somatório de Óbitos Novos para PB (Lista): ', obtListNovosPB10)
print('')
#Tupla
# for RG in tupleBR:
#     for UF in RG:
#         for inf in UF:
#             regPref = inf[0]
#             conRegPref = str(regPref)
#             if '25' in conRegPref:
#                 convInfo = int(inf[8])
#                 print(convInfo)
#                 inf[8] = inf[8] - 2 # não é possível realizar alterações em tuplas, por elas serem imutáveis 
#                 obtListNovosPB10 = obtListNovosPB10 + convInfo 
#As duas operações foram possíveis (lista e tupla)? Justifique.
#Apenas a operação de Lista. Tuplas não podem ser modificadas, por isso a operação de diminuição de 10 unidades para menos
#não foi possível realizar.

#Crie uma nova lista com apenas dados de 1 estado e todos os municípios e adicione essa
#lista nova a lista já existente (append ou insert).
novaListaPI = [[22,220480,22009,'VALEDORIOGUARIBAS','2020-10-16',42,9811,181,5,3,0,'','',0],
                [22,220110,22002,'CHAPADADASMANGABEIRAS','2020-10-27',44,11289,48,2,5,0,'','',0],
                [22,220117,22010,'VALEDOSAMBITO','2020-12-05',49,3951,32,0,1,0,'','',0],
                [22,220253,22005,'PLANICIELITORANEA','2020-12-20',52,5868,163,0,4,0,'','',0],
                [22,220160,22004,'ENTRERIOS','2020-09-17',38,10467,247,3,8,0,'','',1]]              

listNordeste.insert(6,novaListaPI)

# listBR.remove(listNordeste)
# listBR.append(listNordeste)
#listRegioesRN.append(novaListaRN)



# for info in listRegioesRN:
#     print(info)
#print(listRegioesRN)

#listNordeste.insert(novaListaRN) #adicionando a lista do RN na lista Nordeste 

# for reg in listNordeste:
#     print(reg)

# Remova da lista os dados das regiões de saúde. 
# listNordesteComRemove=[]
# listSudesteComRemove=[]
# for regioesPais in listBR:
#     for estados in regioesPais:
#         for info in estados:
#             if info[0] == 24:
#                 info.pop(2)
#                 listNordesteComRemove.append(info)
#             if info[0] == 25:
#                 info.pop(2)
#                 listNordesteComRemove.append(info)
#             if info[0] == 23:
#                 info.pop(2)
#                 listNordesteComRemove.append(info)
#             if info[0] == 26:
#                 info.pop(2)
#                 listNordesteComRemove.append(info)
#             if info[0] == 29:
#                 info.pop(2)
#                 listNordesteComRemove.append(info)
#             if info[0] == 21:
#                 info.pop(2)
#                 listNordesteComRemove.append(info)
#             if info[0] == 33:
#                 info.pop(2)
#                 listSudesteComRemove.append(info)
#             if info[0] == 35:
#                 info.pop(2)
#                 listSudesteComRemove.append(info)
# listBRComRemove = [listNordesteComRemove,listSudesteComRemove]

for rg in listBR:
    for uf in rg:
        for info in uf:
            info.pop(2)

       
for rg in listBR:
    for uf in rg:
        for dados in uf:
            dados.pop(2)
            
        
                        
#::::: Printando
# for RG in listBR:
#     for UF in RG:
#         for dados in UF:
#             print(dados)

tamanhoListaBR=0
qntIndexListaUF=0

for rg in listBR:
    for uf in rg:        
        for dados in uf:
            tamanhoListaBR=tamanhoListaBR + 1
            qntIndexListaUF = len(dados)
            
print('============================================================\n')
print('A lista /listBR/ contém %d elementos, são listas que refere-se as regiões Brasil'%len(listBR))
print('/listBR/listNordeste, em listNordete contém %d elementos, são listas que refere-se aos estados.'%len(listNordeste))
print('/listBR/listSudeste, em listSudeste contém %d elementos, são listas que refere-se aos estados.'%len(listSudeste))
print('/listBR/listNordeste/listRegioesUF,em listRegioesUF contém %d elementos, são listas que refere-se a regioes de saúde de um estado'%len(listRegioesBA))
print('A listBR contém %d listas armazenadas'%tamanhoListaBR)
print('Quantidade de elementos armazenada em uma lista de um dado do município é %d'%qntIndexListaUF)
print('')

#Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de
#óbitos novos.
obitosNovos=[]
for RG in listBR:
    for UF in RG:
        for dados in UF:
            obitosNovos.append(dados[8])
            
valMax=max(obitosNovos)
valMin=min(obitosNovos)            


print('===============================================')
print('O maior número de óbitos é: ',valMax)
print('O menor número de óbitos é: ',valMin)

print('================================================')     
listDictNordeste ={'RN':[
                        {240010:[24,24004,'4ÂªREGIAODESAUDE-CAICO','2020-08-03',32,11136,46,3,3,0,'','',0]},
                        {240030:[24,24003,'3ÂªREGIAODESAUDE-JOAOCAMARA','2020-03-27',13,11035,0,0,0,0,'','',0]},
                        {240690:[24,24006,'6ÂªREGIAODESAUDE-PAUDOSFERROS','2020-08-01',31,3996,5,0,0,0,'','',0]},
                        {240680:[24,24005,'5ÂªREGIAODESAUDE-SANTACRUZ','2020-12-23',52,4759,110,2,2,0,'','',0]}
                        ],
                    'PB':[
                        {250010:[25,25011,'11ÂªREGIAO','2020-03-27',13,10234,0,0,0,0,'','',0]},
                        {250020:[25,25007,'7ÂªREGIAO','2020-03-27',13,5640,0,0,0,0,'','',0]},
                        {250030:[25,25003,'3ÂªREGIAO','2020-03-27',13,28496,0,0,0,0,'','',0]},
                        {250050:[25,25002,'2ÂªREGIAO','2020-03-27',13,14489,0,0,0,0,'','',0]},
                        {250053:[25,25015,'15ÂªREGIAO','2020-03-27',13,5492,0,0,0,0,'','',0]}
                        ],
                    'PI':[
                        {220480:[22,22009,'VALEDORIOGUARIBAS','2020-10-16',42,9811,181,5,3,0,'','',0]},
                        {220110:[22,22002,'CHAPADADASMANGABEIRAS','2020-10-27',44,11289,48,2,5,0,'','',0]},
                        {220117:[22,22010,'VALEDOSAMBITO','2020-12-05',49,3951,32,0,1,0,'','',0]},
                        {220253:[22,22005,'PLANICIELITORANEA','2020-12-20',52,5868,163,0,4,0,'','',0]},
                        {220160:[22,22004,'ENTRERIOS','2020-09-17',38,10467,247,3,8,0,'','',1]}
                        ]
                        }
#Crie um dicionário de forma que seja possível encontrar os municípios associados a um
#estado específico e extrair os dados de casos novos em apenas um comando.
print("Dados de casos novos extraídos de municípios do RN")
print(listDictNordeste['RN'][0][240010][7])
print(listDictNordeste['RN'][1][240030][7])
print(listDictNordeste['RN'][2][240690][7])
print(listDictNordeste['RN'][3][240680][7])
print('================================================') 

# dicio ={}
# x=[]
# # print(dicio)
# x = listDictNordeste[0]
# # x['RN'][0]
# for y in x['RN']:
#     for i in y:
#         for k,j in i.items():
#             dicio[k] = j[7]
#     # for i in range(len(y)):
# print("Dados de casos novos extraídos de municípios do RN")
# print(dicio)
# print('================================================')  

# #Extraia os dados de Teresina/PI apresentando os casos novos com um print.

print('Dados extraídos de casos novos de municípios do estado PI')
for es in listDictNordeste['PI']:
    for k,y in es.items():
        print('Código Município: %d -- Casos Acumulados: %d'%(k,y[7]))
print('================================================')
