# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:11:00 2021

@author: driellevieira
"""

#Calculadora IMC com funções
#Exercícios aplicados aula 07

def imc(x,y):
    x = float(x)
    y = float(y)
    calculo = (x)/(y**2)
    
    return calculo

peso = float(input("Qual seu peso (em kg)?\n"))
altura = float(input("Qual sua altura (em metros)?\n"))

imc2 = imc(peso,altura)

if imc < 17:
    print ("Muito abaixo do peso normal")
elif imc > 17 and imc < 18.5:
    print("Abaixo do peso normal")
elif imc > 18.5 and imc < 25:
    print("Peso dentro do normal")
elif imc > 25 and imc < 30:
    print("Acima do peso normal")
elif imc > 30:
    print("Muito acima do peso normal")
else:
    print("Procure um médico!")
