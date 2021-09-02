
# Fase 1 - Escolhas e Habituacao 

fase1 = 0
fase2 = 0
fase3 = 0
contadorE = 0
contadorD = 0

barraE = input('Pressione 1 e emita o som phee\n')
barraD = input('Pressione 2 e emita o som trill\n')


if barraE == 1 and barraD == 2:

    print('O rato pressionou a barra esquerda e recebeu sua recompensa')

    contadorE = contadorE + 1 # acerto contabilizado
    contadorD = contadorD + 1 #  acerto contabilizado  

elif barraE != 1 and barraD == 2:

    print('O rato errou a barra. A luz sera apagada por 5 segundos')

elif barraE == 1 and barraD != 2:
    
    print('O rato errou a barra. A luz sera apagada por 5 segundos')

fase1 = fase1 + 1

if fase1 < 60:
    
    # este bloco deve ser repetido por 60x, apos 60% de acerto, o experimento segue para o proximo bloco

    if fase1/60 == 0.62:
        
        #inicia-se a fase 2


# Fase 2 - Regime de aproximacoes sucessivas

        distancia = 30.0
        fase2 = 0

        if contadorE == 20 and contadorD == 20:
            print('O experimento seguira para proxima fase')

            if distancia < 30:
                print('O rato nao se aproximou, portanto nao recebera recompensa')
            else:
                print(' Liberado 0.5ml de recompensa')

                fase2 = fase2 + 1
                    
            if fase2 >= 20.0:
                print('O experimento passou para proxima etapa')

        # este bloco deve ser repetido por 20x ate que possa seguir para proxima fase

fase2 = fase2 + 1

if fase2 > 20:

# Fase 3

    fase3 = 0
    som1 = input('Digite P para emitir o som phee')
    som2 = input('Digite T para emitir o som trill')

    if som1 == 'P' and barraE == True:
        print('O rato recebeu 0.5ml de recompensa')
    elif som1 != 'P' and barraE == True:
        print('O rato nao recebeu recompensa')
    elif som2 == 'T'and barraD == True:
        print('O rato recebeu 0.5ml de recompensa')
    elif som2 != 'T' and barraD == True:
        print('O rato nao recebeu recompensa')

fase3 = fase3 + 1

if fase3 < 50:

    # repete-se o bloco de cima

# este bloco deve ser repetido por 50x ate que o contador chegue em 50 e o codigo siga para proxima etapa

    if fase3 == 50:
        
        print('O experimento seguira para proxima fase')

