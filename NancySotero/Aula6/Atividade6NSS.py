#Atividade Contextualizada 6
#Automatização de cirurgia estereotáxica


# I. Procedimento de anestesia

print('1. Procedimento de Anestesia')

listaFarmacos = ('ketamina', 'xilazina', 'halotano')
listaAnimais = ('camundongo', 'rato')
animal = str(input('Qual animal será operado (rato ou camundongo)? '))
peso = float(input('Qual o peso do animal que será operado? '))

if animal == listaAnimais[1]:
    print('Deve ser administrado o fármaco ', listaFarmacos[0], 'e', listaFarmacos[1], 'com cálculo para ', peso, 'em gramas')
elif animal == listaAnimais[0]:
    print('Deve ser administrado o fármado ', listaFarmacos[2], 'com cálculo para ', peso, 'em mg')

# II. Posicionamento do Animal no estereotáxico

print('2. Posicionamento do Animal no estereotáxico')
print('Posicionar barras de ferro no meato acúsctico do animal')
piscadaOlho = str(input('O animal piscou os olhos (sim ou não)? '))

while(piscadaOlho != 'sim'):
    print('Coloque novamente as barras') 
    piscadaOlho = str(input('O animal piscou os olhos (sim ou não)? '))
print('Prosseguir')


bregAngulo = input('Insira o valor da angulação bregma: ')
lambAngulo = input('Insira o valor do angulação lambda: ')

while(bregAngulo != lambAngulo):
    print('A angulação deve ter valores iguais')
    bregAngulo = input('Insira o valor da angulação bregma: ')
    lambAngulo = input('Insira o valor da angulação lambda: ')
        
    print ("Posição correta")

# III. Limpeza do campo de trabalho

print('3. Limpeza do campo de trabalho')
#Retirada da pelagem que recobre a parte superior da calota craniana
#Retirada dos tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana. 
#Limpar a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H2O2 10 volumes.

etapasLimpeza = ['Pelagem', 'Tecidos Moles', 'Calota']
Limpeza = str(input('Qual envoltório do tecido cerebral foi higienizado? '))
while(Limpeza != etapasLimpeza[0]):
    print('Retire a Pelagem')
    Limpeza = str(input('Qual envoltório do tecido cerebral foi higienizado? '))
print('Prosseguir')

Limpeza2 = str(input('Qual envoltório do tecido cerebral foi higienizado em seguida? '))
while(Limpeza2 != etapasLimpeza[1]):
    print('Retire os Tecidos Moles')
    Limpeza2 = str(input('Qual envoltório do tecido cerebral foi higienizado? '))
print('Prosseguir')

Limpeza3 = str(input('Qual envoltório do tecido cerebral foi higienizado por último? '))
while(Limpeza3 != etapasLimpeza[2]):
    print('Higienize a calota')
    Limpeza3 = str(input('Qual envoltório do tecido cerebral foi higienizado? '))

perox=float(input('Quantos volumes de H2O2 foram utilizados? '))
if perox != 10:
    print('Incorreto, utilize 10 volumes')
else:
    print('Limpeza Finalizada')

# IV. Utilizar poliacrilato

print('4. Utilizar poliacrilato')
poliac = float(input('O poliacrilato foi colocado no perímetro externo(0=sim/1=não)?   '))
while(poliac != 0):
    print('Por favor, faça a colocação')
    poliac = float(input('O poliacrilato foi colocado no perímetro externo?   '))
print('Nenhum sangramento detectado')

# V. Fixação de parafusos

print('5. Fixação de parafusos')
print('Posicione a agulha em cima do bregma')

AP = 6.0
LL = 3.3
DV = 4.0

coordAP = float(input('Insira a coordenada para posição AP: '))
while(coordAP != AP):
    print('Coordenada incorreta, tente novamente: ')
    coordAP = float(input('Insira a coordenada para posição AP: '))

coordLL = float(input('Insira a coordenada para posição LL: '))
while(coordLL != LL):
    print('Coordenada incorreta, tente novamente: ')
    coordLL = float(input('Insira a coordenada para posição LL: '))

coordDV = float(input('Insira a coordenada para posição DV: '))
while(coordDV != DV):
    print('Coordenada incorreta, tente novamente: ')
    coordDV = float(input('Insira a coordenada para posição DV: '))
print('Parafusos posicionados')

# VI. Inserção de cânulas

print('6. Inserção de cânulas')
hemisf = str(input('Selecione um hemisfério cerebral (1=direito/2=esquerdo): '))
if hemisf == 1:
    print ('Iniciar pelo hemisfério direito')
else:
    print ('Iniciar pelo hemisfério esquerdo')

canula1 = float(input('Insira a posição da primeira cânula: '))
if canula1 == coordAP:
    print('Valor correto')

canula2 = float(input('Insira a posição da segunda cânula: '))
if canula2 == 2*coordLL:
    print('Valor correto')

#VII. Fazer furo com a broca

print('7. Fazer furo com broca')
grau = float(input('Verifique o grau de angulação de sua mão: '))
while(grau != 45):
    print('O posicionamento não está correto')
    grau = float(input('Verifique o grau de angulação de sua mão: '))

print('Posicionamento correto, realizar furo')

#VIII. Introdução de cânula-guia
print('8. Introdução de cânula-guia')

canGuia = float(input('Insira o valor de inserção da cânula-guia: '))
while(canGuia != coordDV):
    print('Posicionamento incorreto')
    canGuia = float(input('Insira o valor de inserção da cânula-guia: '))
print('Correto, inserir cânula-guia')

#IX. Absorver LCR
print('9. Absorver LCR')

absLCR = str(input('Há escape de LCR (sim ou não)? '))
if absLCR == 'sim':
    print('Retire LCR com toalhas de papel')
else:
    print('Prosseguir')

#X. Confecção de capacete
print('10. Confecção de capacete')

listaCapacete = ['crânio', 'cânula-guia', 'parafuso']
capacete = str(input('Onde o capacete está localizado? '))
while(capacete != listaCapacete[0] and capacete != listaCapacete[1] and capacete != listaCapacete[2]):
    print('Posicionamento incorreto, repita')
    capacete = str(input('Onde o capacete está localizado? '))

print('Aguarde a secagem do acrílico')

#XI. Inserção de segunda cânula-guia
print('11. Inserção de segunda cânula-guia')
print('Levante o braço do estereotáxico')

canGuia2 = float(input('Insira o valor de inserção da segunda cânula-guia: '))
while(canGuia2 != coordDV):
    print('Posicionamento incorreto')
    canGuia2 = float(input('Insira o valor de inserção da segunda cânula-guia: '))
print('Correto, inserir a segunda cânula-guia')

#XII. Espalhar cimento
print('12. Espalhar cimento')

print('Repita as etapas 9 e 10 do procedimento')
print('Espalhe cimento sobre o crânio')

#XIII. FInalização
print('13. Finalização')

print('Levante o braço do estereotáxico')
caixa = str(input('Levar animal para caixa. O animal está acomodado? '))
if caixa == 'não':
    print('Acomode o animal')
else:
    print('Fim do protocolo cirúrgico')


