'''
-------------------------------------
----Este é o meu primeiro programa---
-------------------------------------
'''
print('André Felipe dizendo hello world') # esta 
# instrução faz aparecer o que está escrito nela
# na tela preta do pc

issoEUmaString = "qq coisa entre aspas dupla"
naoENumeroESimString = "15"
istoEUmInteiro = 15
istoTambemEUmaString = 'andre'
istoEUmNumeroReal = 15.3
istoEUmBooleano = True 
print(issoEUmaString,naoENumeroESimString)
print(istoEUmInteiro,istoTambemEUmaString,istoEUmNumeroReal,istoEUmBooleano)

print()

print(type(issoEUmaString))
print(type(istoEUmInteiro))
print(type(istoEUmNumeroReal))
print(type(istoEUmBooleano))

# import math
from math import sqrt

# print('A raiz quadrade de 100 é: ',math.sqrt(100))
print('A raiz quadrade de 100 é: ',sqrt(100))
# print(math.sqrt(istoEUmNumeroReal))
print(sqrt(istoEUmNumeroReal))

resultadosoma = 3+5 #coma
print(resultadosoma)
print(2-3,6*5,8/2)#subtração,multiplicação,divisão
print(7//2,2**10,7%2)#parte inteira, potenciação, resto da divisão

soma = 0
soma += 3; print(soma); soma = soma+3; print(soma)

subtração = 0
subtração -= 3; print(subtração); subtração = subtração-3; print(subtração)

multiplicacao = 1
multiplicacao *= 3; print(multiplicacao); multiplicacao = multiplicacao*3; print(multiplicacao)

divisao = 100
divisao /= 3; print(divisao); divisao = divisao/3; print(divisao)

a,b,c = 1+5,2**12,3

print(a,b,c)

(a,b) = (10,20)
print(a,b,c)

parede = "branca"
print(parede == "branca")
print(parede != "branca")
print(not(parede == "branca"))
print(not(parede == "branca") & (parede == "branca"))
print(not(parede == "branca") | (parede == "branca"))
print(not(parede == "branca") and (parede == "branca"))
print(not(parede == "branca") or (parede == "branca"))

print(2<3, 4>5, 2<=3, 4>=5, 2==3, 4!=5)

nome = input("Digite seu nome: ")
peso = float(input("Digite o seu peso: "))

print(nome, ", seu peso é: ", peso)

