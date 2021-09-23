# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:18:05 2021

@author: driellevieira
"""

#Atividade Contextualizada 06
#Automatização do procedimento de cirurgias esterotáxicas em animais
#Drielle Viana Vieira - 2021.2

import math

print ("Cirurgia Esterotáxica Em Roedores")

agenteanalgesico_ratos = (("Codeína","250mg/kg"),("Butorfanol","0,05 a 2mg/kg"),("Meloxicam","1 a 4mg/kg"))
agenteanalgesico_camundongos = (("Codeína","250mg/kg"),("Butorfanol","5mg/kg"),("Meloxicam","1 a 10mg/kg"))

roedor = int(input("Qual roedor será operado? Digite 0 para ratos e 1 para camundongos.\n"))
lista = ["Rato","Camundongo"]

if roedor == 0:
    print("O roedor é: ", lista[0])
    print("Os agentes analgésicos recomendados para este roedor são: ", agenteanalgesico_ratos)
elif roedor == 1:
    print("O roedor é: ", lista[1])
    print("Os agentes analgésicos recomendados para este roedor são: ", agenteanalgesico_camundongos)
    
agenteanestesico = {"Ketamina","90 a 120mg/kg","Xilazina","5 a 16mg/kg"}
anestesico = input("A dosagem do anestésico é de acordo com o peso do roedor. Para mais informações digite 'Ketamina' ou 'Xilazina': \n")

if anestesico == "Ketamina":
    agenteanestesico = {"Ketamina":"90 a 120mg/kg"}
    print(agenteanestesico)
else:
    agenteanestesico = {"Xilazina":"5 a 16mg/kg"}
    print(agenteanestesico)
    
peso = float(input("Qual o peso do animal (em kg)?"))

ketamina = peso*90
xilazina = peso*10

print ("Para esse roedor, a dose de Ketamina a ser administrada é:", ketamina)
print ("Para esse roedor, a dose de Xilazina a ser administrada é:", xilazina)

roedoranestesiado = input("O roedor encontra-se anestesiado e pronto pra começar a ser operado? Digite 0 para 'Sim' e 1 para 'Não'")

if roedoranestesiado == 0:
    print("O roedor já pode ser posicionado no Estereotoráxico.")
    angulo_bregma = input("Qual o valor da angulação Bregma?\n")
    angulo_lambda = input("Qual o valor do angulação lambda?\n")
    
    while angulo_bregma != angulo_lambda:
        print("O roedor não está posicionado corretamente. Ambas angulações devem ser iguais!")
        angulo_bregma = input("Qual o valor da angulação Bregma?\n")
        angulo_lambda = input("Qual o valor do angulação lambda?\n")
        
    print ("Agora o roedor está posicionado corretamente! A superfície está plana.")
    
    print("Agora vamos começar a limpeza do campo para depois iniciar com segurança a cirurgia.")
    print("Siga os seguintes passos:")
    print("1 - Retire a pelagem que cobre a parte superior da calota craniana.")
    print("2 - Retire a epiderme, a derme e o tecido conjuntivo.")
    
    resp = int(input("A caixa craniana já foi alcaçada? Digite 0 para 'Sim' e 1 para 'Não'"))
    
    while resp != 0:
        print("Ainda existe tecido mole para ser retirado!")
        resp = input("A caixa craniana já foi alcaçada? Digite 0 para 'Sim' e 1 para 'Não'")
        
    print("3 - Para limpar a calota craniana, incluindo qualquer resto de pelagem, utilize H2O2 de 10 volumes.")
    print("Agora que você fez os três passos de limpeza, o campo de trabalho está limpo.")
    
    print("Para evitar sangramentos utilize uma pequena camada de poliacrilato em todo o perímetro externo.")
    
    parafusos = int(input("Escolha os pontos de fixação dos parafusos. Dê preferência para a parte posterior da calota craniana."))
    voltas = 1
    
    for i in range(1,4):
        print("Já foram dadas", i, "voltas no parafuso.")
    
    agulha_ap = 0
    agulha_ll = 0
    agulha_dv = 0

    ap = 6
    ll = 3.63
    dv = 4
    
    print("Todos os parâmetros foram definidos.")
    
    print("Agora é hora de fazer os furos com a broca até alcançar a meninge.")
    print("Para isso apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +/- 45º de angulação.")
    print("Agora é hora de introduzir as cânulas.")
    
    canula1 = 0
    
    while (canula1 != dv):
        canula1 += 1
        print("Introdução da cânula 1.")
    
    if canula1 == dv:
        print("A cânula 1 foi inserida.")
        
    print("Agora, drene qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio.")
    print("Faça uma mistura de acrílico polimerizante com o solvente para fazer um capacete.")
    
    canula2 = 0
    
    while (canula2 != dv):
        canula2 += 1
        print("Introdução da cânula 2.")
    
    if canula2 == dv:
        print("A cânula 2 foi inserida.")
        
    print ("Acomode o roedor em uma caixa aquecida por uma lâmpada sem outros animais acordados.")
    print ("Assim que o roedor despertar, coloque-o de volta a sua caixa-moradia.")
    print ("O procedimento chegou ao fim!")
    
else:
    print("É necessário mais anestésico!")
    print("Aplique:", ketamina*0.1, "de ketamina e", xilazina*0.1, "de xilazina.")
    print("Roedor anestesiado.")
    
    print("O roedor já pode ser posicionado no Estereotoráxico.")
    angulo_bregma = input("Qual o valor da angulação Bregma?\n")
    angulo_lambda = input("Qual o valor do angulação lambda?\n")
    
    while angulo_bregma != angulo_lambda:
        print("O roedor não está posicionado corretamente. Ambas angulações devem ser iguais!")
        angulo_bregma = input("Qual o valor da angulação Bregma?\n")
        angulo_lambda = input("Qual o valor do angulação lambda?\n")
        
    print ("Agora o roedor está posicionado corretamente! A superfície está plana.")
    
    print("Agora vamos começar a limpeza do campo para depois iniciar com segurança a cirurgia.")
    print("Siga os seguintes passos:")
    print("1 - Retire a pelagem que cobre a parte superior da calota craniana.")
    print("2 - Retire a epiderme, a derme e o tecido conjuntivo.")
    
    resp = int(input("A caixa craniana já foi alcaçada? Digite 0 para 'Sim' e 1 para 'Não'"))
    
    while resp != 0:
        print("Ainda existe tecido mole para ser retirado!")
        resp = input("A caixa craniana já foi alcaçada? Digite 0 para 'Sim' e 1 para 'Não'")
        
    print("3 - Para limpar a calota craniana, incluindo qualquer resto de pelagem, utilize H2O2 de 10 volumes.")
    print("Agora que você fez os três passos de limpeza, o campo de trabalho está limpo.")
    
    print("Para evitar sangramentos utilize uma pequena camada de poliacrilato em todo o perímetro externo.")
    
    parafusos = int(input("Escolha os pontos de fixação dos parafusos. Dê preferência para a parte posterior da calota craniana."))
    voltas = 1
    
    for i in range(1,4):
        print("Já foram dadas", i, "voltas no parafuso.")
    
    agulha_ap = 0
    agulha_ll = 0
    agulha_dv = 0

    ap = 6
    ll = 3.63
    dv = 4
    
    print("Todos os parâmetros foram definidos.")
    
    print("Agora é hora de fazer os furos com a broca até alcançar a meninge.")
    print("Para isso apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +/- 45º de angulação.")
    print("Agora é hora de introduzir as cânulas.")
    
    canula1 = 0
    
    while (canula1 != dv):
        canula1 += 1
        print("Introdução da cânula 1.")
    
    if canula1 == dv:
        print("A cânula 1 foi inserida.")
        
    print("Agora, drene qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio.")
    print("Faça uma mistura de acrílico polimerizante com o solvente para fazer um capacete.")
    
    canula2 = 0
    
    while (canula2 != dv):
        canula2 += 1
        print("Introdução da cânula 2.")
    
    if canula2 == dv:
        print("A cânula 2 foi inserida.")
        
    print ("Acomode o roedor em uma caixa aquecida por uma lâmpada sem outros animais acordados.")
    print ("Assim que o roedor despertar, coloque-o de volta a sua caixa-moradia.")
    print ("O procedimento chegou ao fim!")