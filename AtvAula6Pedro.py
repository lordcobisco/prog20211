# Automatização de um programa para cirurgia estereotáxica em roedores

print('Vamos iniciar a cirurgia estereotáxica')

doseAnalgésico = [['codeína', '250mg/kg'], ['dipirona', '600mg/kg'], ['morfina', '10mg/kg']]
doseAnestésico = [['propofol', '10mg/kg'], ['ketamina', '90mg/kg'], ['xilazina', '10mg/kg']]

print('A primeira etapa é anestesiar o animal')

analgésico = int(input('Escolha o analgésico, digite 0 para codeína, 1 para dipirona, 2 para morfina\n')) 
if analgésico == 0:
    print('A dose de codeína é', doseAnalgésico[0])
if analgésico == 1:
    print('A dose de dipirona é', doseAnalgésico[1])
if analgésico == 2:
    print('A dose de morfina é', doseAnalgésico[2]) 

anestésico = int(input('Escolha o anestésico, digite 0 para propofol, 1 para ketamina e 2 para xilazina\n')) 
if anestésico == 0:
    print('A dose de proprofol é', doseAnestésico[0])
if anestésico == 1:
    print('A dose de ketamina é', doseAnestésico[1])
if anestésico == 2:
    print('A dose de xilazina é', doseAnestésico[2])

print('Agora, posicione o animal no estereotáxico')

animalanestesiado = int(input('O animal está anestesiado? 0 para sim, 1 para não\n'))
if animalanestesiado == 0:
    print('Posicione o animal no esterotáxico')
if animalanestesiado == 1:
    print('Aguarde a anestesia fazer efeito')

bregma = int(input('Qual a angulação do ponto bregma?\n'))
lanbda = int(input('Qual a angulação do ponto lanbda?\n'))
if bregma != lanbda:
    print('Ajuste as agulações até estarem no mesmo eixo')
else:
    print('Vamos para a próxima etapa') 

print('Retire a pelagem que recorbe a calota craniana')
print('Retire os tecidos moles, até expor a superfície óssea')
print('Remova restos de tecido mole com solução de H2O2 10 volumes')       
print('Aplica uma pequena camada de poliacrilato no perímetro externo')    
print('Escolha os pontos de fixação dos parafusos na parte posterior da calota craniana, dê no máximo 3 voltas no parafuso')

print('Agora vamos escolher a área do encéfalo que iremos atingir, para isso, acesse o dicionário abaixo com as coordenadas dos eixos AP, LL e DV')

hipocampoCA1 = ('AP 6,1cm, LL 3,23cm, DV 4,2cm')
globoPálidoInterno = ('AP 8,3cm, LL 5,5cm, DV 2,3cm')
NúcleoAccumbens = ('AP 9,1cm, LL 4,5cm, DV 3,9cm')
áreasCerebrais = {hipocampoCA1, globoPálidoInterno, NúcleoAccumbens}

áreaescolhida = int(input('Escolha a área cerebral de interesse: 0 para CA1, 1 para GPI, 2 para NAcc\n'))

if áreaescolhida == 0:
    print('Vc escolheu hipocampoCA1, estas são as coordenadas:', hipocampoCA1)
elif áreaescolhida == 1:
    print('Vc escolheu globo pálido interno, estas são as coordenadas:', globoPálidoInterno)
if áreaescolhida == 2:
    print('Vc escolheu núcleo accumbens, estas são as coordenadas:', NúcleoAccumbens)

print('Posicione a agulha sobre o ponto bregma e mova para os pontos AP e LL')
print('Agora que vc escolheu o ponto de inserção da cânula, vamos perfurar o crânio')    
print('Posicione a broca no ponto escolhido e perfure o crânio numa angulação de 45º')
print('Agora introduza a cânula até o ponto DV')
print('Aspire restos de sangue e líquido cefalorraquidiano')


cânula1posicionada = int(input('A cânula 1 está bem posicionada? Digite 0 para CA1, 1 para GPI e 2 para NAcc, 3 para não posicionada\n'))
if cânula1posicionada == 3:
    print('Introduza até os pontos calculados')
else:
    print('Vamos fixar a cânula')

print('Faça uma mistura de acrílico com solvente para criar um capacete envolvendo a cânula, o crânio e os parafusos')
print('Aguarde secar')
print('Retire o animal e o acomode em uma caixa com lâmpada aquecida, sem a presença de outros animais, quando ele acordar, colocar em sua caixa-moradia')
print ('Fim do procedimento')        