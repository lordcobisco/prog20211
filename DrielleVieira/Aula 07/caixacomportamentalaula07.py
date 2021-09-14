# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:11:00 2021

@author: driellevieira
"""

#Inclua no exercício de Método de discriminação de estímulos auditivos para primatas através do condicionamento operante uma atualização.
#Requisito:
    #Adaptar o problema utilizando funções.
    
def habituacao():
    dist = 30
    for i in range(20):
        distancia = float(input("Qual é a distância entre o primata e a barra?\n"))
        if(distancia < dist):
            print("Dê os 0,5ml de recompensa! =)")
        else:
            print("O animal não cumpriu o objetivo. Não liberar nada! =(")
            
    return print("O animal já realizou as 20 tentativos.")
    return print("Hora da próxima etapa do treinamento. Vem aí: ESTÍMULOS SONOROS.")

def treinocomestimulo():
    for i in range(50):
        somphee = str("O animal tocou a barra da esquerda ao ouvir o Som Phee? Digite 's' para Sim e 'n' para Não.\n")
        somtrill = str("O animal tocou a barra da direita ao ouvir o Som Trill? Digite 's' para Sim e 'n' para Não.\n")
        
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
        
    return print("Final das 50 repetições de estímulos sonoros.")

def tempo():
    treinamento = float(input("Qual foi o tempo, em minutos, que a sessão de treinamento durou?\n"))
    if (treinamento > 30):
        print("O treinamento excedeu os 30 minutos e não será considerado para estudo. Favor esperar 4 horas e realizar novamente o treinamento.")
    else:
        print("O treinamento foi realizado em um  tempo menor do que 30 mintuos! Vamos para a próxima fase.")
    return print("Fim do treinamento.")

def primatas():
    print("Caixa comportamental para primetas com condicionamento operante por estímulos sonoros.")
    print("")
    print("Habituação do animal - Passo 1")
    hab = str(input("O animal já está habituado? Digite 's' para Sim e 'n' para Não.\n"))
    if (hab == "s"):
        print("A sessão de treinamento está prestes a começar!!!")
        print("")
        habituacao()
        treinocomestimulo()
        tempo()
    else:
        print("Após o animal habituado, reabra o programa para o treinamento.")
        
primatas()