# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:52:42 2021

@author: driellevvieira
"""

peso = 80 #em quilogramas
altura = 1.67 #em metros
imc = peso/altura**2

print("O valor do seu IMC é: ", + imc)
print("Você está muito abaixo da faixa de peso considerada normal!", imc <= 17)
print("Você está abaixo da faixa de peso considerada normal!", imc > 17 and imc <= 18.5)
print("Você está dentro da faixa de peso considerada normal!", imc > 18.5 and imc < 25)
print("Você está acima da faixa de peso considerada normal!", imc > 25 and imc < 30)
print("Você está muito acima da faixa de peso considerada normal!", imc > 30)