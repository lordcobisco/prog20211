# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:35:33 2021

@author: driellevieira
"""

# Atividade Contextualizada 03 - Exercício 02 - Microscopia Confocal
# Drielle Viana Vieira

print ("Microscopia Confocal")
print ("Bem vind@! Esse programa irá receber dados para que o microscópio possa realizar a captura das imagens")

tipodecelula = 3 #podendo variar de 1 a 10
contraste1 = 150 #podendo variar de 0 a 1000
iluminacao1 = 2 #podendo variar de 1 a 10
profundidade1 = 100 #variação de 0 a 100
eixox1 = 200 #variação de 0 a 100
eixoy1 = 300 #variação de 0 a 100
lentes1 = 4 #variação de 1 a 5
zoom1 = 50 #variação de 0 a 200
lamina1 = 2 #variação de 1 a 10
intensidadelaser1 = 10 #variação de 1 a 15

celula = int(input("Qual célula você deseja encontrar (1 a 10)? "))
print ("Houve alteração de variável inserida? ", celula != tipodecelula)

contraste = int(input("Qual contraste você deseja utilizar (0 a 1000)? "))
print ("Houve alteração de variável inserida? ", contraste != contraste1)

iluminacao = int(input("Qual iluminação você deseja usar (1 a 10)? "))
print ("Houve alteração de variável inserida? ", iluminacao != iluminacao1)

profundidade = int(input("Eixo z (0 a 100)? "))
print ("Houve alteração de variável inserida? ", profundidade != profundidade1)

eixox = int(input("Eixo x (0 a 100)? "))
print ("Houve alteração de variável inserida? ", eixox != eixox1)

eixoy = int(input("Eixo y (0 a 100)? "))
print ("Houve alteração de variável inserida? ", eixoy != eixoy1)

lentes = int(input("Qual lente você está utilizando (1 a 5)? "))
print ("Houve alteração de variável inserida? ", lentes != lentes1)

zoom = int(input("Qual o zoom da imagem (0 a 200)? "))
print ("Houve alteração de variável inserida? ", zoom != zoom1)

lamina = int(input("Qual lâmina está sendo utilizada (1 a 10)? "))
print ("Houve alteração de variável inserida? ", lamina != lamina1)

intensidadelaser = int(input("Qual intensidade de luz que você deseja (1 a 15)? "))
print ("Houve alteração de variável inserida? ", intensidadelaser != intensidadelaser1)

print ("O usuário escolheu as seguintes especificações para o uso do equipamento.")
print ("Tipo de célula: ", celula)
print ("Contraste: ", contraste)
print ("Iluminação: ", iluminacao)
print ("Eixo Z: ", profundidade)
print ("Eixo x: ", eixox)
print ("Eixo y: ", eixoy)
print ("Lente utilizada: ", lentes)
print ("Zoom escolhido: ", zoom)
print ("Lâmina escolhida: ", lamina)
print ("Intensidade do Laser: ", intensidadelaser)

#Calibração do Equipamento

#Calibração Horizontal 

usuario = (input("Digite seu nome: "))
print (usuario.lower())

#Primeira e última letra do nome 10x

print (usuario,", por favor, insira 10 vezes a primeira e a última letra do seu nome para calibração horizontal do equipamento.")
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
print(x2 == usuario[-1].lower())
x1 = input("Digite a primeira letra do seu nome: ")
print(x1 == usuario[0].lower())
x2 = input ("Digite a última letra do seu nome: ")
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

print ("Chegamos ao fim da calibração.")
print (usuario,"! O equipamento já está pronto para uso!")