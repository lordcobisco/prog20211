'''
----------------------------------
--Este é o meu primeiro programa--
----------------------------------
'''

print("hello world") # esta
# instrução faz aparecer o que está escrito nela 
# na tela preta do pc

issoEUmaString = "qq coisa aspas dupla"
naoENumeroESimString = "15"
istoEUmInteiro = 15
istoTambemEUmaString = 'Yago'
istoEUmNumeroReal = 15.3
istoEUmBooleano = True
print(issoEUmaString,naoENumeroESimString)
print(istoEUmInteiro,istoTambemEUmaString,istoEUmNumeroReal,istoEUmBooleano)
print()

print(type(issoEUmaString))
print(type(naoENumeroESimString))
print(type(istoEUmInteiro))
print(type(istoTambemEUmaString))
print(type(istoEUmNumeroReal))
print(type(istoEUmBooleano))

#import math 
from math import sqrt

#print('A raiz quadrade de 100 é: ',math.sqrt(100))
print('A raiz quadrade de 100 é: ',sqrt(100))
#print(math.sqrt(istoEUmNumeroReal))
print(sqrt(istoEUmNumeroReal))

resultadosoma=3+5 #soma
print(resultadosoma)
print(2-3,6*5,5/2,100/10)#subtração, multiplicação, divisão
print(7//2)#parte inteira da divisão
print(2**10)#exponencial
print(7%2)#resto da divisão

soma=0
soma += 3; print(soma); soma=soma+3; print(soma)
subtração=0
subtração -= 3; print(subtração); subtração=subtração-3; print(subtração)
multiplicação=1
multiplicação *= 3; print(multiplicação); multiplicação=multiplicação*3; print(multiplicação)

divisao=100
divisao /= 3; print(divisao); divisao=divisao/3; print(divisao)

a,b,c=1+5,2**8,3/3

print(a,b,c)

(a,b)=(10,20)
print(a,b,c)


parede="branca"
print(parede == "branca")
print(parede != "branca")
print(not(parede == "branca"))
print(not(parede == "branca") & (parede == "branca"))
print(not(parede == "branca") | (parede == "branca"))
print(not(parede == "branca") and (parede == "branca"))
print(not(parede == "branca") or (parede == "branca"))

print(2<3, 4>5, 2<=3, 2==3, 4!=5)

nome = input("Digite seu nome:")
peso = float(input("Digite o seu peso:"))

print(nome, "seu peso é:", peso)


    