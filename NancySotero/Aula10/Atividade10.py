import random
from audiomath import Sound, Player, Concatenate, StretchAndShift

def duplicarCanais (som):
    som *= [1.0,1.0]
    return som

def limitarCanais (som):
    som = som[:,:2]
    return som

#Defina os parametros

paramTempo = float(input("Tempo do estimulo em ms: "))
paramISI = float(input("ISI (Tempo entre estimulos) em ms: "))
paramQuant = float(input("Quantidade de estimulos: "))
paramProp = float(input("Digite a proporcao do estimulo raro. Ex: 0.2 (20%): "))
paramFreq = float(input("Digite a frequencia da aquisição em Hz: "))

#Importar os Estimulos

estimulo01 = Sound('Ba.wav')
estimulo02 = Sound('DaHigh.wav')

#Informaçoes dos audios pré-Manipulação
print("Informações dos estimulos pré manipulação: ", estimulo01, estimulo02)

#Caso haja apenas 1 canal, criação de novos canais.

if estimulo01.nChannels == 1:
    estimulo01 = duplicarCanais(estimulo01)
if estimulo02.nChannels == 1:
    estimulo02 = duplicarCanais(estimulo02)

#Limitação da quantidade de canais.

estimulo01 = limitarCanais(estimulo01)
estimulo02 = limitarCanais(estimulo02)

#Alterar a Frequencia

estimulo01.fs = paramFreq
estimulo02.fs = paramFreq

#Alterar a Duração dos Estimulos

estimulo01.TimeStretch(speed=((estimulo01.duration*1000)/paramTempo))
estimulo02.TimeStretch(speed=((estimulo02.duration*1000)/paramTempo))

#Acrescimo de ISI

estimulo01 = (paramISI/1000) % estimulo01
estimulo02 = (paramISI/1000) % estimulo02

#RiseDecay - A Implementar

#Informaçoes dos audios pós-Manipulação

print("Informações dos estimulos pós manipulação: ", estimulo01, estimulo02)

#Criação de lista completa

faixafinal = []

for i in range (int(paramQuant*paramProp)):
    faixafinal.append(estimulo01)

for i in range (int(paramQuant*(1-paramProp))):
    faixafinal.append(estimulo02)

random.shuffle(faixafinal)

for i in range (int(paramQuant)):
    faixafinal[i].Play()

#Criação de faixa final

AmostraSalva = Sound(fs=paramFreq)

for i in range (int(paramQuant)):
    AmostraSalva = AmostraSalva % faixafinal[i]

AmostraSalva.Write('arquivo_teste_01.wav')
