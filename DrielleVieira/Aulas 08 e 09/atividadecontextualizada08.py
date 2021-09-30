# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:11:01 2021

@author: driellevieira
"""

#Atividade Contextualizada 08
#Motion Capture
#Tratar dados obtidos a partir de sensores IMU

import csv
import math

with open('C:\\Users\\cinvi\\OneDrive\\Documentos\\Drielle\\Mestrado\\Projeto\\Python\\Visualização de dados\\Fundamentos da programação\\Aula 08\\coletaFlexJoelho.csv','r') as arquivo:
    angreader = csv.reader(arquivo,delimiter="'", quotechar='|')

sensores = []

for linha in arquivo:
    valor = linha.split('],""[')
    sensor1 = valor[0].split('[')[1]
    sensor2 = valor[1].split(']"""')[0]
    
    for sensor01 in sensor1.split(","):
        snsores.append(float(sensor01))
    for sensor02 in sensor2.split(","):
        sensores.append(float(sensor02))

print (sensores)                             
    
def calculo():
    angulo = 0
    valores = []
    
    for i in range(4,len(sensores),4):
        angulo = 0.98(angulo+sensores[i]*0.05)+(1-0.98)*sensores[i-3]
        valores.append(angulo)
    return valores