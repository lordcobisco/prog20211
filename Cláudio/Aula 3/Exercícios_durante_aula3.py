#Este é o meu primeiro programa

print("Salve rapaziada, aqui é Júnior") #isso aqui aparece logo quando abrir o programa mas nao aparece no programa
a = 1
b = 1
print (a + b)
print ("Lucas está com saudade")
'''
aqui é que também não amostra
'''
issoeumastring = "qq coisa entre aspas dupla"
naoenumeroesimstring = "15"
istoeuminteiro = 15
istotbmeumastring = 'jubileu'
#tudo que está em azul está guardado na minha memória
#então tudo que está depois = significa que a info está dentro da memória
istoeumnumeroreal = 15.3
intoeumbooleano = True #esse azul mais escuro é uma palavra reservada do python
print (istoeuminteiro, istotbmeumastring, istoeumnumeroreal)
for i in range (10):
    print (istoeumnumeroreal)
print(type(istotbmeumastring))
print (type(intoeumbooleano))
if (a+b) == 2:
    print ("very nice")
# import math
from math import sqrt
import math
print (math.sqrt (9))
print (math.sqrt (istoeuminteiro))

resultadosoma = 3+5
print(resultadosoma)
print(7//2,2**10,7%2) #parte inteira, potenciação, resto da divisão

soma = 0
soma += 3; print(soma); soma = soma+3; print (soma) #isso aqui é uma operação acumulada

parede = "branca"
print (parede == "branca") 
print (parede != "branca") 
#duas iguals é uma pergunta lógica, um igual é uma atribuição, !é perguntando se é diferente
print (not(parede == "branca"))
print (not(parede == "branca") & (parede == "branca"))
print (not(parede == "branca") | (parede == "branca"))
# & ambas tem que ser verdadeira, | é o msemo que ou (uma ou outra pode ser verdadeira)
print (not(parede == "branca") and (parede == "branca"))
print (not(parede == "branca") or (parede == "branca"))

print (2<3, 4>5, 2<=3, 4>=5, 2==3, 4!=5)

nome = input ("digite seu nome")
peso = float(input("digite o seu peso")) #input sempre vem como string

print(nome, "seu peso é:", peso)
