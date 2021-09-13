# Dados baixados no dia 06/09/2021
# Utilizado os dados covid coletados entre 25/02/20 até 31/07/20 

casosAcumuladosRO = [38992]
casosAcumuladosAC = [19625]
casosAcumuladosAM = [100940]
casosAcumuladosRR = [32016]
casosAcumuladosPA = [154685]
casosAcumuladosAP = [36468]
casosAcumuladosTO = [24824]

casosAcumuladosNorte = [casosAcumuladosRO, casosAcumuladosAC, casosAcumuladosAM, casosAcumuladosRR, casosAcumuladosPA, casosAcumuladosAP, casosAcumuladosTO]
casosAcumuladosNorteTupla = (casosAcumuladosNorte)



casosAcumuladosMA = [120661]
casosAcumuladosPI = [51477]
casosAcumuladosCE = [173882]
casosAcumuladosRN = [50416]
casosAcumuladosPB = [82794]
casosAcumuladosPE = [95005]
casosAcumuladosAL = [59725]
casosAcumuladosSE = [58713]
casosAcumuladosBA = [166154]

casosAcumuladosNordeste = [casosAcumuladosMA, casosAcumuladosPI, casosAcumuladosCE, casosAcumuladosRN, casosAcumuladosPB, casosAcumuladosPE, casosAcumuladosAL, casosAcumuladosSE, casosAcumuladosBA]
casosAcumuladosNordesteTupla = (casosAcumuladosNordeste)



casosAcumuladosMG = [127106]
casosAcumuladosES = [83292]
casosAcumuladosRJ = [165495]
casosAcumuladosSP = [542304]

casosAcumuladosSudeste = [casosAcumuladosMG, casosAcumuladosES, casosAcumuladosRJ, casosAcumuladosSP]
casosAcumuladosSudesteTupla = (casosAcumuladosSudeste)



casosAcumuladosPR = [76112]
casosAcumuladosSC = [84073]
casosAcumuladosRS = [66692]

casosAcumuladosSul = [casosAcumuladosPR, casosAcumuladosSC, casosAcumuladosRS]
casosAcumuladosSulTupla = (casosAcumuladosSul)



casosAcumuladosMS = [24936]
casosAcumuladosMT = [51865]
casosAcumuladosGO = [67941]
casosAcumuladosDF = [106292]

casosAcumuladosCentroOeste = [casosAcumuladosMS, casosAcumuladosMT, casosAcumuladosGO, casosAcumuladosDF]
casosAcumuladosCentroOesteTupla = (casosAcumuladosCentroOeste)


print('O número de casos acumulados no RJ é', casosAcumuladosRJ)
print('O número de casos acumulados no RJ é', casosAcumuladosSudesteTupla[2])

# Apresente na tela o número de óbitos acumulados por cada estado

obitosAcumuladosRO = [872]
obitosAcumuladosAC = [531]
obitosAcumuladosAM = [3268]
obitosAcumuladosRR = [505]
obitosAcumuladosPA = [5728]
obitosAcumuladosAP = [565]
obitosAcumuladosTO = [381]

obitosAcumuladosMA = [3013]
obitosAcumuladosPI = [1329]
obitosAcumuladosCE = [7668]
obitosAcumuladosRN = [1777]
obitosAcumuladosPB = [1811]
obitosAcumuladosPE = [6557]
obitosAcumuladosAL = [1567]
obitosAcumuladosSE = [1434]
obitosAcumuladosBA = [3463]

obitosAcumuladosMG = [2769]
obitosAcumuladosES = [2545]
obitosAcumuladosRJ = [13477]
obitosAcumuladosSP = [22997]

obitosAcumuladosPR = [1920]
obitosAcumuladosSC = [1102]
obitosAcumuladosRS = [1876]

obitosAcumuladosMS = [376]
obitosAcumuladosMT = [1819]
obitosAcumuladosGO = [1656]
obitosAcumuladosDF = [1469]

# Lista e Tupla com dado de novos óbitos para o dia 31/07/20:

print('Os dados abaixo são referentes a óbitos novos computados no dia 31/07/20.')
obitosNovosNordeste = ['MA:', 17, 'PI:', 25, 'CE:', 7, 'RN:', 26, 'PB:', 26, 'PE:', 31, 'AL:', 13, 'SE:', 26, 'BA:', 72]
print(obitosNovosNordeste)

obitosNovosNordesteTupla = ('MA:', 17, 'PI:', 25, 'CE:', 7, 'RN:', 26, 'PB:', 26, 'PE:', 31, 'AL:', 13, 'SE:', 26, 'BA:', 72)
print(obitosNovosNordesteTupla)

obitosNovosNordeste.remove('PB:')
print(obitosNovosNordeste)
obitosNovosNordeste.remove(26)
print(obitosNovosNordeste)

print('Houve um erro e a contagem da PB irá diminuir em 10')
print('Abaixo segue a nova contagem:')
obitosNovosNordesteCorrigido = [obitosNovosNordeste, ['PB:', 16]]
print(obitosNovosNordesteCorrigido)

# Uma Tupla não pode ser modificada, logo, a alteração acima só pode ser feita na lista.


# Criando lista com dados de todos os municípios de Roraima. Nessa lista inclui: Nome do município, região de saúde, casos acumulados e óbitos acumulados.

roraima = ['Amajari:', ['Centro Norte', 244, 6], 
         'Alto Alegre:', ['Centro Norte', 389, 9],
         'Boa Vista:', ['Centro Norte', 23932, 405],
         'Bomfim:', ['Centro Norte', 381, 6],
         'Cantai:', ['Centro Norte', 725, 7],
         'Caracara:', ['Sul', 561, 6],
         'Caroebe:', ['Sul', 691, 2],
         'Iracema:', ['Sul', 188, 4],
         'Mucaja:', ['Centro Norte', 0, 0],
         'Normandia:', ['Centro Norte', 247, 9],
         'Pacaraima:', ['Centro Norte', 1127, 20],
         'Rorainópolis:', ['Sul', 1198, 16],
         'São João da Baliza:', ['Sul', 656, 3],
         'São Luiz:', ['Sul', 162, 2],
         'Uiramuta:', ['Centro Norte', 496, 2]] 

print(roraima)

casosAcumuladosNorte.append(roraima)

print(casosAcumuladosNorte)

# A lista abaixo refere-se aos dados de Casos acuulados, Óbitos acumulados do dia 18/08/20 no estado de RR:

dadosRR18Ago20 = [40183, 574]
 
dadosRR2020 = [30997, 497]

print('A soma dos dados para RR no primeiro semestre de 2020 é:')
print(sum(dadosRR2020))

print('A soma dos dados de RR na data de 18/08/2020 é:')
print(sum(dadosRR18Ago20))

if sum(dadosRR18Ago20) == sum(dadosRR2020):
    print('A soma dos dados é igual\n')
else:
    print('A soma dos dados não é igual')   

# lista de novos óbitos no estado de RR em Agosto de 2020:

NovosObitosRR = [8,0,0,15,4,6,6,3,0,0,4,4,6,4,3,0,0,6,1,1,0,3,0,0,3,0,4,1,0,0,0]
print('O maior valor numérico de novos óbitos em RR no mês de Agosto 2020 é', max(NovosObitosRR))     
print('O menor valor numérico de novos óbitos em RR no mês de Agosto 2020 é', min(NovosObitosRR))