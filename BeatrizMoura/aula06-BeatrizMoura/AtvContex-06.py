
# I - Anestesia do ratinho

peso = float(input('Digite o peso do animal em quilogramas: \n'))
dose_aplicada = float(input(' Digite o valor em ml do farmaco aplicado: \n'))
dosagem = 0.2*peso # exemplo de que a dosagem em ml eh 20% do peso do rato

if dose_aplicada == dosagem:
    print('O animal estara pronto para cirurgia dentro de alguns segundos')
    
    # II - Posicionando as hastes no ouvido externo
    
    olho_piscou = input('Encaixe das hastes no ouvido externo. Digite S, caso o olho do rato tenha piscado, ou N caso o olho nao tenha piscado \n')
    inclinacao = input('Digite S caso a inclinacao esteja em 5 graus\n')

    if olho_piscou == 'S' and inclinacao == 'S':
        print('Procedimento autorizado para proxima etapa')

            # III - Limpeza do campo de trabalho

        print("De acordo com as intrucoes cirurgicas, certifique-se de que apos a retirada dos tecidos moles, o local foi devidamente higienizado")

        higienizacao = input(' Digite S caso o local tenha sido higienizado \n')

        if higienizacao == 'S':
            print('Retire os tecidos moles ate alcancar a parte ossea da caixa craniana')

            osso = bool(input('Digite 1, caso tenha acessado a caixa ossea e 0, caso nao tenha acessado a caixa ossea\n'))

            if osso == True:
                print('Deve ser aplicado 10 volumes de H202')

                # IV - Posicionamento e campo cirurgico higienizado

                posicionamento = bool(input('Digite 1 caso o animal esteja devidamente posicionado, digite 0, caso o animal nao esteja posicionado corretamente\n'))

                if posicionamento == True:
                    
                    print('Aplique uma pequena camada de poliacrilato no perimetro externo para evitar sangramentos')

                    # V - Escolha dos pontos de fixacao de parafusos

                    parafusos = int(input('Determine o ponto de fixacao dos implantes!\n'))
                    giros = 1

                    for i in range(1,4):
                        print('Foram realizados ', i, 'giros para fixacao do implante.')
                    
                    ap = 6.42
                    ll = 3.63
                    dv = 4.20

                    anteroPosterior = float(input('Digite o valor encontrado na regua da localizacao Antero-Posterior'))
                    lateroLateral = float(input('Digite o valor encontrado na regua da localizacao Latero-Lateral'))
                    dorsoVentral = float(input('Digite o valor encontrado na regua da localizacao Dorso-Ventral'))
                    
                    ca1 = anteroPosterior - ap
                    ca2 = lateroLateral - ll
                    ca3 = dorsoVentral - dv 
                                        
                    print('Realize o procedimendo de perfuracao.\n')
                    print('Apoie a mao que segura a broca contra o assoalho e perfure o cranio em uma angulacao de aproximadamente 45 graus.\n')
                    print('Introduza a canula no hemisferio desejado.\n')

                    canula1 = 0
    
                    while (canula1 != dv):
                        canula1 += 1
                        print("Introducao da canula 1.")
                    
                    if canula1 == dv:
                        print("A canula 1 foi inserida.")
                        
                    print("Atencao! Drene qualquer sangue ou líquido que extravase pelo orifício criado no crânio.")
                    print("Misture de acrílico polimerizante com o solvente para fazer um capacete.")
                    
                    canula2 = 0
                    
                    while (canula2 != dv):
                        canula2 += 1
                        print("Introducao da canula 2.")
                    
                    if canula2 == dv:
                        print("A canula 2 foi inserida.")
                        
                    print ("O procedimento chegou ao fim!")




                else:
                    print('Posicione o animal corretamente para aplicacao do poliacrilato')
            else:
                print('Realize o procedimento para acessar a caixa ossea')
        else:
            print('Realize a higienizacao do campo de trabalho! ')
    else:
        print('Atencao: reajuste a angulacao e as hastes!\n')
else:
    print('A dose informada nao pode ser aplicada. Procedimento nao autorizado! ')
    
