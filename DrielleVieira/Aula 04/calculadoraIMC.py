# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:34:35 2021

@author: cinvi
"""

#Cálculo do IMC

import os

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = peso/altura**2

print("Seu IMC é: %.4f" % imc)

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
    
os.system("pause")
