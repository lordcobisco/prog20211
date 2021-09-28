#Atividade Contextualizada 4

#Requisito 1 = Habituação
#Animal Habituado? Sim ou Não

habituacaoAnimal = int(input('O animal está habituado? (sim = 1; não = 2) '))
if habituacaoAnimal == 1:
    print('O animal já está habituado, pular esta etapa')
if habituacaoAnimal == 2: 
    print('O animal não está habituado, iniciar habituação')

    #Requisito 2 = Regime de aproximação

    print('Posicione o animal a 30 cm de distância')
    varDistancia = 30
    varAprox = int(input('Insira a nova posição do animal: '))
    if varAprox >= 30:
        print('Animal não recebeu a recompensa')
    if varAprox < 30:
        print ('Animal se aproximou, liberar 0,5 ml da recompensa')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    varBarra = int(input('O animal tocou na barra? (sim = 1; não = 2)  '))
    if varBarra == 1:
        print ('vamos continuar')
    else:
        print ('vamos tentar novamente')
    
    varBarraFinal = int(input('Quantas vezes o animal tocou na barra? '))
    if varBarraFinal == 20:
        print('O experimento passou para a próxima fase!')
    else:
        print ('Vamos tentar novamente')

    #Nova Fase
    #Trill = direita e phee = esquerda

    Som1 = int(input('O animal ouivu o som Phee? (sim = 1; não = 2) '))
    varSom1 = int(input('O animal tocou na barra esquerda? (sim = 1; não = 2) '))
    Som2 = int(input('O animal ouivu o som Trill? (sim = 1; não = 2) '))
    varSom1 = int(input('O animal tocou na barra direita? (sim = 1; não = 2) '))
    if Som1 == 1 and varSom1 == 1:
        print('Liberar 0,5 ml de recompensa')
        print('Repita o processo 50 vezes')
    elif Som1 == 1 and varSom1 == 2:
        print('Não liberar recompensa')
    elif Som1 == 2 and varSom1 == 1:
        print('Não liberar recompensa')
    else:
        print('Não liberar recompensa')

    varTempo = int(input('Qual foi a duração do experimento em minutos?  '))
    if varTempo <= 30:
        print('Excelente! Podemos passar para a próxima etapa!')
    if varTempo >30:
        print('Tempo superior ao necessário, repetir experimento')
    
#Fim
    


    
    
    
        




