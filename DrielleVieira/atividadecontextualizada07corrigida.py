# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 08:27:36 2021

@author: driellevieira
"""

#Atividade Contextualizada 07
#Drielle Viana Vieira
#Optogenética

import time
import random
import sys

print ("A optogenética é uma das técnicas que tem revolucionado a neurociência moderna, permitindo a modulação da atividade de populações neuronais específicas com grande precisão espacial e temporal.")
print ("Seja bem vind@!")

inicio = input("Você deseja iniciar o procedimento? Digite 's' para Sim e 'n' para Não.\n")
tempo = time.time()

if inicio == "s":
    led = (("Red",5),("Green",3.5),("Blue",3.3))
    eletrodos = []
    canal = int(input("Qual canal do eletrodo você deseja utilizar? Digite um valor entre 1 e 32.\n"))
    
    for i in range (1,33):
        canalutilizado = ("canal: ", i)
        eletrodos.insert(i, canalutilizado)
    
    def acender(voltagem):
        tensao = float(voltagem)
        if (voltagem == 5):
            cor = led[0][0]
        elif (voltagem == 3.5):
            cor = led[1][0]
        else:
            cor = led[2][0]
        return cor
    
    ligar = input("Você deseja ligar o canal? Digite 's' para Sim e 'n' para Não.\n")
    
    while (ligar == "s"):
        for i in range (0,33):
            if (i == canal-1):
                voltagem = input("Qual é a tensão que está passando pelo canal? 5V, 3.5V ou 3.3V?\n")
                corled = acender(voltagem)
                print ("O led que está aceso é o: ",corled,"do",eletrodos[i])
                
        desligar = input("Você deseja parar o procedimento? Digite 's' para Sim e 'n' para Não.\n")
            
        if (desligar == "s"):
            break
        ligar = input("Você deseja ligar algum outro canal? Digite 's' para Sim e 'n' para Não.\n")
            
tempodeexecucao = time.time() - tempo
print("O tempo de execução do experimento foi de: ", tempodeexecucao)
