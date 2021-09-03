proxEtapa = False
print('Vamos Começar -- \n')
habituacao = int(input('Informe o valor [ 0 - Animal não Habituado ] ou [ 1 - Animal Habituado ] \n'))
if ((habituacao >=  0) and (habituacao<=1)):
    if (habituacao == 1):
        proxEtapa = True
        print('[!] Ok, seguimos para próximas etapas \n')
    else:
        print('[!] Para anvançar no seu experimento, você precisa habituar o seu animal \n')
else:
    print('[!] -- Digite um valor válido \n')
if(proxEtapa == True):
    print('[Medidor de Aproximação] - O sangui está a menos de 30cm do experimento? \n')
    opAprox = int(input('Digite 0 - [Não] ou Digite 1 [Sim]: \n'))
    if ((opAprox >=  0) and (opAprox<=1)):
        if(opAprox==1):
            print('Liberar recompensa de 0,5 ml \n')
        else:
            print('Não liberar recompensa de 0,5 ml \n')
    else:
        print('[!] -- Digite um valor válido \n')
    print('[Tocar na Barra 20x] - O sangui tocou na barra por 20x? \n')
    opBarra20 = int(input('Digite 0 pra [Não] ou Digite 1 pra [Sim]: '))
    if((opBarra20 >=  0) and (opBarra20<=1)):
        if(opBarra20 == 1):
            print('[!] O experimento pode seguir para próxima Etapa \n')
            proxEtapaSom = True
        else:
            print('[!] Aguarde o animal tocar 20x para seguir para próxima etapa \n')
            proxEtapaSom = False
    else:
        print('Por favor, digite um valor válido')
        proxEtapaSom = False
    if(proxEtapaSom==True):
        print('[!] Observe o tipo do som e o toque do animal nas barras \n')
        tipoSom= int(input('Phee - [ 1 ] ou Trill [ 2 ]'))
        toqueBarras = int(input('Barra Direita [ 1 ] ou Barra Esquerda [ 2 ]'))
        if((tipoSom == 1) and (toqueBarras == 2)) or ((tipoSom == 2) and (toqueBarras == 1)):
            print('Liberar recompensa de 0,5 ml')
        else:
            print('Não liberar nada para o animal \n')
    if(proxEtapaSom==True):
        print('O experimento foi realizado por 50x em 30 minutos? \n')
        outraFase = int(input('[1] - Sim ou [0] Não \n'))
        if(outraFase == 1):
            print('Você deverá seguir para a próxima fase, até logo. \n')
        else:
            print('Treine mais um pouco... \n')
else:
    print('[ Aplicação Terminou ] -- \n')
