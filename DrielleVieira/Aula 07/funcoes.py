# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 08:56:04 2021

@author: driellevieira
"""

#Aula 07
#Funções e Classe

#Funções
#Sem parâmetros de entrada ou saída

def mensagemdeErro():
    """Não retorna nada, mas mostra na tela uma mensagem de erro clássica"""
    print("Tudo o que você colocou no programa está errado.\n")
    print("Comece do zero.")
    
mensagemdeErro()

#Com parâmetros de entrada e saída
def add(x,y):
    return x + y

parametro1 = int(input("Digite um número:\n"))
parametro2 = int(input("Digite outro número:\n"))

print(add(parametro1,parametro2))

#Não possível de determinar número de parâmetros
def arbitrary(x,y,*more):
    print("x = ",x,", y = ",y)
    print("arbitrary: ", more)
    
arbitrary(3, 4)
arbitrary(3, 4, "Olá", 3, 4)

#Escopo e tempo de vida das variáveis
def my_func():
    x = 10
    print("Valor da função: ",x)

x = 20
my_func()
print("O valor fora da função é: ",x)

#Parâmetros opcionais
def funcao(pais = "Brazil"):
    print("Olá, muito prazer. Eu venho do " + pais)

funcao("Suécia")
funcao("Finlâncida")
funcao()
funcao("Nova Zelândia")

#Listas como parâmetro
def minhafunc(comida):
    for x in comida:
        print(x)
        
saudaveis = ["Goiaba","Laranja Bahia","Frango Desfiado","Batata Doce"]
minhafunc(saudaveis)

#Recursão
def recursao(k):
    if (k > 0):
        result = k + recursao(k-1)
        print(result)
    else:
        result = 0
    return result

print ("\n\nEsse é um exemplo do uso da recursão.")
recursao(6)

