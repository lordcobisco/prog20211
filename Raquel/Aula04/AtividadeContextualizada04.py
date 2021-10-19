# Ativida contextualizada 04
# habituação animal

from typing import overload


print("programa para habituação para treinar os saguis")

print('Etapa 1- habituação do animal')

habituado = str(input('O animal está habituado? "1" para SIM e "0" para NÃO.\n'))
if habituado:
 print("legal agora vamos para a proxima etapa")
 print('Fase 2 - Aproximaçao')
else:
    print ('Habitue o animal e então retorne.')
    print ('Fim do programa!')

print ('Início da etapa 2')
distanciaPadrao = 30

distanciaAtual = int (input ('Qual a distância entre o animal e a barra em centímetros?\n'))

if 1<distanciaAtual<distanciaPadrao:
    print (' O animal se aproximou!\nFoi liberado 0,5ml de rec.')
elif distanciaAtual==distanciaPadrao:
    print ('O animal não se aproximou nem se afastou!\nAguarde até o tempo final estimado.')
elif distanciaAtual==0:
    print ('O animal chegou a barra!\nContinuar para próxima etapa!')
else: 
    print ('O animal se afastou ou não se aproximou!\nEncerre o experimento.')

print('Você precisará registrar quantas vezes o animal tocou na barra.\nPara isso, será perguntado se o animal tocou na barra.\n Quando chegar a 20 vezes, você será direcionado para a próxima etapa.')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('1 vez')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('2 vezes')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('3 vezes')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('4 vezes')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('5 vezes')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('6 vezes')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('7 vezes')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('8 vezes')
else:
    print ('Aguardar!')

toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('9 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('10 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('11 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('12 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('13 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('14 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('15 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('16 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('17 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('18 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('19 vezes')
else:
    print ('Aguardar!')
toquenabarra = int (input ('O animal tocou na barra?\nPressione 1 para sim e 0 para não.\n'))

if toquenabarra:
    print ('20 vezes')
    print ('Muito bem!\nO animal tocou na barra 20 vezes.\nVamos para a próxima etapa.')
else:
    print ('Aguardar!')

print ('Nessa etapa, você irá verificar se a barra pressionada pelo animal\nestá de acordo com o som emitido.')
print ('A barra da esquerda será corretamente pressionada\nquando o animal pressioná-la quando for tocado o som 1. ')
print ('A barra da direita será corretamente pressionada\nquando o animal pressioná-la quando for tocado o som 2. ')
print ('Esse experimento durará até o animal apertar 50 vezes a barra ou até durar 30 minutos.')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('1º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('2º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('3º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('4º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('5º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('6º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('7º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('8º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('9º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('10º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('11º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('12º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('13º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('14º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('15º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('16º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('17º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('18º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('19º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('20º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('21º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('22º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('23º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('24º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('25º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('26º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('27º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('28º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('29º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('30º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('31º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('32º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('33º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('34º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('35º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('36º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('37º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('38º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('39º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('40º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('41º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('42º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('43º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('44º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('45º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('46º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('47º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('48º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('49º vez')

botaoEsquerdo = int (input ('O animal apertou o botão esquerdo?\n'))
botaoDireito =  int (input ('O animal apertou o botão direito?\n'))
som1 = int (input ('O som 1 foi acionado?\n'))
som2 = int (input ('O som 2 foi acionado?\n'))
suco = 'Liberar 0,5ml de rec'

if botaoEsquerdo and som1:
    print (suco)
elif botaoEsquerdo and som2:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som1:
    print ('Botão apertado errado, continuar experimento!')
elif botaoDireito and som2:
    print (suco)
else:
    print ('Aguardar o fim do tempo!')

print ('50º vez')

print (input ('Se o experimento foi realizado 50 vezes ou se o tempo de 30 min esgotou\npasse para a próxima fase.'))