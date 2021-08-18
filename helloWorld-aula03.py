#Este é o meu primeiro programa
'''---------------comentando também da para comentar adicionando três aspas simples---------------'''


print("hello world")

issoEUmaString = "Disciplina fundamentos de programação" #variável do tipo String

NumeroInteiro = 1 #isso é um Int

NumeroReal = 1.2 #isso é um Float

Decisao = True #isso é uma variável do tipo Bool

print(issoEUmaString, NumeroInteiro, NumeroReal)
print(Decisao)
print(NumeroInteiro * NumeroReal)
print(type(NumeroReal))
print(type(Decisao))

import math

print('A raíz quadrada de um é: ', math.sqrt(NumeroInteiro))

print(3+4, 5*8, 3/15)

soma = 1
soma += 5 #equivalente a soma=soma+3
print(soma); soma = soma+3; print(soma)

parede = "preta"
print(parede == "preta")
print(parede != "branca")

nome = input("Digite seu nome: ")
peso = float(input("digite o seu peso: ")