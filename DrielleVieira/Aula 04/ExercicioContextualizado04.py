# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:09:01 2021

@author: driellevieira
"""

#Atividade Contextualizada 04
#Método de discriminação de estímulos auditivos para primatas através do condicionamento operante

#Som 1 = Som phee
#Som 2 = Som trill

#Requisitos:
    # 1) Habituação
    # 2) Regime de aproximações sucessivas
    
print ("Caixa comportamental para primatas com condicionamento operante por estímulos sonoros.")
print ("Habituação do animal - Passo 1")

hab = str(input("O animal já está habituado? Digite s ou n!\n")) #Perguntar ao usuário se o animal já está habituado
if (hab == 's'):
    print ("A sessão de treinamento está prestes a começar!") #início da sessão de treinamento
    dist = 30 #variavél inicial de distancia 30cm
    distancia = float(input("Qual é a distância entre o primata e a barra?\n")) #medição da distância do animal e da barra 20 vezes
    if (distancia < dist):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia0 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia0 < distancia):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia1 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia1 < distancia0):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia2 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia2 < distancia1):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia3 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia3 < distancia2):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia4 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia4 < distancia3):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia5 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia5 < distancia4):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia6 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia6 < distancia5):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia7 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia7 < distancia6):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia8 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia8 < distancia7):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia9 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia9 < distancia8):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia10 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia10 < distancia9):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia11 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia11 < distancia10):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia12 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia12 < distancia11):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia13 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia13 < distancia12):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia14 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia14 < distancia13):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia15 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia15 < distancia14):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia16 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia16 < distancia15):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia17 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia17 < distancia16):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    distancia18 = float(input("Qual é a distância entre o primata e a barra?\n"))
    if (distancia18 < distancia17):
        print ("Dê os 0,5ml de recompensa! =)")
    else:
        print ("O animal não cumpriu o objetivo. Não liberar nada =(")
    print("O animal já realizou as 20 tentativas.")
    print("Hora da próxima etapa de treinamento. Vem aí: ESTÍMULOS SONOROS!")
    
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
    
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
    
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
    
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
    
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
    
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
    
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    somphee = str(input("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite s ou n!\n"))
    somtrill = str(input("O animal tocou a barra da direita ao ouvir o Som Trill? Digite s ou n!\n "))
    
    if (somphee == 's' and somtrill == 's'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 'n' and somtrill == 's'):
        print ("Som Phee - Não liberar recompensa.")
        print ("Som Trill - Liberar 0,5ml de recompensa!")
    elif (somphee == 's' and somtrill == 'n'):
        print ("Som Phee - Liberar 0,5ml de recompensa!")
        print ("Som Trill - Não liberar recompensa.")
    else:
        print ("Não liberar recompensa, o objetivo do treinamento não foi atingido. =(")
        
    
    print ("Final das 50 repetições de estímulos sonoros.")
    
    treinamento = float(input("Qual foi o tempo, em minutos, que a sessão de treinamento durou?\n"))
    if (treinamento > 30):
        print ("O treinamento excedeu os 30 minutos e não será considerado para o estudo. Favor esperar 4 horas e realizar novamente o treinamento.")
    else:
        print ("O treinamento foi realizado em um tempo menor do que 30 minutos! Vamos para a próxima fase!")
else:
    print ("Espere um tempo e reabra o programa.")

print ("Fim do algoritmo.")
