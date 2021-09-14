# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:35:33 2021

@author: guilhermehenriqv
"""

# Atividade Contextualizada 03 - Exercício 02 - Microscopia Confocal
# Guilherme Henrique Viana da Silva

print ("Microscopia Confocal ISD / IIN-ELS")
print ("Bem vind@! Esse programa irá receber dados para que o microscópio possa realizar a captura das imagens")

tipodecelula = 3 #podendo variar de 1 a 100
filtro = 1 #podendo variar de 1 a 5
iluminacao = 2 #podendo variar de 1 a 150
profundidade = 100 #variação de 0 a 100
eixohorizontal= 200 #variação de 0 a 100
eixovertical = 300 #variação de 0 a 100
lentes1 = 4 #variação de 1 a 5
zoom1 = 50 #variação de 0 a 300
foco = 2 #variação de 1 a 10
intensidadelaser1 = 10 #variação de 1 a 10

tipodecelula = int(input("Qual célula você deseja encontrar (1 a 100)? "))
print ("Houve alteração de variável inserida? ", tipodecelula != tipodecelula)

filtro = int(input("Qual contraste você deseja utilizar (1 a 5)? "))
print ("Houve alteração de variável inserida? ", filtro != filtro)

iluminacao = int(input("Qual iluminação você deseja usar (1 a 150)? "))
print ("Houve alteração de variável inserida? ", iluminacao != iluminacao)

profundidade = int(input("Eixo z (0 a 100)? "))
print ("Houve alteração de variável inserida? ", profundidade != profundidade)

eixohorizontal = int(input("Eixo x (0 a 100)? "))
print ("Houve alteração de variável inserida? ", eixohorizontal != eixohorizontal)

eixovertical = int(input("Eixo y (0 a 100)? "))
print ("Houve alteração de variável inserida? ", eixovertical != eixovertical)

lentes = int(input("Qual lente você está utilizando (1 a 5)? "))
print ("Houve alteração de variável inserida? ", lentes != lentes1)

zoom = int(input("Qual o zoom da imagem (0 a 300)? "))
print ("Houve alteração de variável inserida? ", zoom != zoom1)

foco = int(input("Qual lâmina está sendo utilizada (1 a 10)? "))
print ("Houve alteração de variável inserida? ", foco != foco)

intensidadelaser = int(input("Qual intensidade de luz que você deseja (1 a 10)? "))
print ("Houve alteração de variável inserida? ", intensidadelaser != intensidadelaser1)

print ("O usuário escolheu as seguintes especificações para o uso do equipamento.")
print ("Tipo de célula: ", tipodecelula)
print ("Contraste: ", filtro)
print ("Iluminação: ", iluminacao)
print ("Eixo Z: ", profundidade)
print ("Eixo x: ", eixohorizontal)
print ("Eixo y: ", eixovertical)
print ("Lente utilizada: ", lentes)
print ("Zoom escolhido: ", zoom)
print ("Lâmina escolhida: ", foco)
print ("Intensidade do Laser: ", intensidadelaser)

#Calibração do Equipamento

#Calibração Horizontal 

usuario = (input("Digite seu nome: "))
print (usuario.lower())

#Insira aqui o seu nome 10x

print (usuario,", insira aqui o seu nome para calibração horizontal do equipamento.")
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite o seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite o seu nome: ")
print(x2 == usuario[-1].lower())

#Calibração vertical

#Segunda e penúltima letra do nome 

print (usuario,", por favor, insira 10 vezes a segunda e a penúltima letra do seu nome para calibração vertical do equipamento.")
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())
y1 = input("Digite a segunda letra do seu nome: ")
print(y1 == usuario[1].lower())
y2 = input ("Digite a penúltima letra do seu nome: ")
print(y2 == usuario[-2].lower())

print ("Chegamos ao término da calibração.")
print (usuario,"! O equipamento está pronto para uso! Tenha um bom dia")