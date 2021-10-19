#Aparelho desligado:
aparelho = False
anestesias = {'Ketamina': 90, 'Xilazina': 10}

# Aparelho ligado:
aparelho = True
# Verificar a dosagem correta de acordo com o peso dos animais.


# Verificar se anestésico ter feito efeito
while aparelho is True:
    iniciar = input('Deseja iniciar o procedimento cirúrgico?\n(s/n): ')
    if iniciar == 's':
        peso_animal = float(input('Informe o peso do animal(Kg):\n'))
        dosagemKetamina = peso_animal * anestesias['Ketamina']
        dosagemXilazina = peso_animal * anestesias['Xilazina']
        print('-'*60)
        print('[+] Devem ser utilizadas as seguintes dosagens de anestésicos:')
        print(f'- Dosagem Ketamina: {dosagemKetamina} mg ')
        print(f'- Dosagem Xilazina: {dosagemXilazina} mg')
        print('-'*60)
        anestesicosAplicados = input(
            'Os anestésicos foram injetados?\n(s/n): ')
        if anestesicosAplicados == 's':
            # Posicionar o animal no estereotáxico
            print('-'*60)
            angulacao = input(
                'A angulação da cabeça do animal está correta?\n(s/n): ')
            if angulacao == 's':
                print('-'*60)
                retirarPelagem = input(
                    'Foi feita a limpeza do campo cirúrgico?\n(s/n): ')
                if retirarPelagem == 's':
                    print('-'*60)
                    poliacrilatoAplicado = input(
                        'Foi aplicado o Poliacrilato por todo o perímetro externo?\n(s/n): ')
                    if poliacrilatoAplicado == 's':
                        print('-'*60)
                        pontosFixacao = input(
                            'Os pontos de fixação foram definidos?\n(s/n): ')
                        if pontosFixacao == 's':
                            print('-'*60)
                            posicionamentoAgulhas = [
                                ('AP', 6.42), ('LL', 3.23), ('DV', 4.2)]
                            valores = []
                            for x in range(3):
                                print('-'*60)
                                valor = float(input(
                                    f"Digite a coordenada de procedimento para a\nlocalização {posicionamentoAgulhas[x][0]} com '.' (ex: 5.3): \n"))
                                valores.append(valor)
                            posAP = posicionamentoAgulhas[0][1] + valores[0]
                            posLL1 = posicionamentoAgulhas[1][1] + valores[1]
                            posLL2 = posicionamentoAgulhas[1][1] - valores[1]
                            posDV = posicionamentoAgulhas[2][1] + valores[2]
                            print('-'*60)
                            print(
                                f'AP Final: {posAP:.2f}\nLL1 Final: {posLL1:.2f}\nLL2 Final: {posLL2:.2f}\nDV Final: {posDV:.2f}')
                            print('-'*60)
                            print('Inserção das canulas guias: ')
                            print('-'*60)
                            lista2 = ['LL1', 'LL2']
                            L1L2 = input(
                                f'Informe qual ponto escolhido inicialmente:\n1 - {lista2[0]}\n2 - {lista2[1]}\n')
                            if L1L2 == '1':
                                print('-'*60)
                                print('Os pontos que devem ser utilizados serão:')
                                print(f'LL1 : {posLL1:.2f}')
                                print(f'AP: {posAP:.2f}')
                                print('-'*60)
                                iniciarPerfuracao = input(
                                    'Iniciar perfuração do crânio?\n(s/n): ')
                                print('-'*60)
                                if iniciarPerfuracao == 's':
                                    introduzirCanulaGuia = input(
                                        'Introduzir a cânula guia?\n(s/n): ')
                                    print('-'*60)
                                    if introduzirCanulaGuia == 's':
                                        print(
                                            f'A canula guia deve ser introduzida até {posDV:.2f} do Dorso Ventral(DV)')
                                        posCG = input(
                                            f'A canula guia foi introduzida até {posDV:.2f} do Dorso Ventral?\n(s/n): ')
                                        print('-'*60)
                                        if posCG == 's':
                                            print(
                                                'A canula guia foi introduzida corretamente')
                                            drenagem = input(
                                                'A drenagem de liquidos que estejam saindo pelo orifício criado no crânio foi realizada?\n(s/n): ')
                                            print('-'*60)
                                            if drenagem == 's':
                                                mistura = input(
                                                    'A mistura do acrílico polimerizante com o solvente foi realizada?(s/n): ')
                                                print('-'*60)
                                                if mistura == 's':
                                                    print(
                                                        'Com essa mistura, faça um capacete abrangendo o crânio, a cânula guia e o parafuso.')
                                                    capacete = input(
                                                        'O capacete foi feito?\n(s/n): ')
                                                    print('-'*60)
                                                    if capacete == 's':
                                                        secar = input(
                                                            'A mistura feita para o capacete já secou?\n(s/n): ')
                                                        print('-'*60)
                                                        if secar == 's':
                                                            print('\n'*10)
                                                            print(
                                                                'Os pontos que devem ser utilizados para a inserção da proxima Cânula Guia são:')
                                                            print(
                                                                f'LL2 : {posLL2:.2f}')
                                                            print(
                                                                f'AP: {posAP:.2f}')
                                                            print('-'*60)
                                                            iniciarPerfuracao = input(
                                                                'Iniciar perfuração do crânio?\n(s/n): ')
                                                            if iniciarPerfuracao == 's':
                                                                introduzirCanulaGuia = input(
                                                                    'Introduzir a cânula guia?\n(s/n): ')
                                                                print('-'*60)
                                                                if introduzirCanulaGuia == 's':
                                                                    print(
                                                                        f'A canula guia deve ser introduzida até {posDV:.2f} do Dorso Ventral(DV)')
                                                                    print(
                                                                        '-'*60)
                                                                    posCG = input(
                                                                        f'A canula guia foi introduzida até {posDV:.2f} do Dorso Ventral?\n(s/n): ')
                                                                    print(
                                                                        '-'*60)
                                                                    if posCG == 's':
                                                                        print(
                                                                            'A canula guia foi introduzida corretamente')
                                                                        drenagem = input(
                                                                            'A drenagem de liquidos que estejam saindo pelo orifício criado no crânio foi realizada?\n(s/n): ')
                                                                        print(
                                                                            '-'*60)
                                                                        if drenagem == 's':
                                                                            mistura = input(
                                                                                'A mistura do acrílico polimerizante com o solvente foi realizada?(s/n): ')
                                                                            print(
                                                                                '-'*60)
                                                                            if mistura == 's':
                                                                                print(
                                                                                    'Com essa mistura, faça um capacete abrangendo o crânio, a cânula guia e o parafuso.')
                                                                                capacete = input(
                                                                                    'O capacete foi feito?\n(s/n): ')
                                                                                print(
                                                                                    '-'*60)
                                                                                if capacete == 's':
                                                                                    secar = input(
                                                                                        'A mistura feita para o capacete já secou?\n(s/n): ')
                                                                                    print(
                                                                                        '-'*60)
                                                                                    if secar == 's':
                                                                                        print('\n'*10)
                                                                                        print(
                                                                                            'Procedimento realizado com sucesso!')
                                                                                        aparelho = False
                                                                                    elif secar == 'n':
                                                                                        print(
                                                                                            'Aguardar a mistura secar')
                                                                                    else:
                                                                                        print(
                                                                                            "Digite apenas 's' ou 'n'")
                                                                                elif capacete == 'n':
                                                                                    print(
                                                                                        'Realize a construção do capacete')
                                                                                else:
                                                                                    print(
                                                                                        "Digite apenas 's' ou 'n'")

                                                                        elif drenagem == 'n':
                                                                            print(
                                                                                'Realizar a drenagem de liquidos que estejam saindo pelo orifício criado no crânio')
                                                                        else:
                                                                            print(
                                                                                "Digite apenas 's' ou 'n'")
                                                                    elif posCG == 'n':
                                                                        print(
                                                                            f'A canula guia deve ser introduzida até {posDV}')

                                                                elif introduzirCanulaGuia == 'n':
                                                                    print(
                                                                        'Introduzir a canula guia')

                                                                else:
                                                                    print(
                                                                        "Digite apenas 's' ou 'n'")

                                                            elif iniciarPerfuracao == 'n':
                                                                print(
                                                                    'Inicie a perfuração')

                                                            else:
                                                                print(
                                                                    "Digite apenas 's' ou 'n'")
                                                            aparelho = False
                                                        elif secar == 'n':
                                                            print(
                                                                'Aguardar a mistura secar')
                                                        else:
                                                            print(
                                                                "Digite apenas 's' ou 'n'")
                                                    elif capacete == 'n':
                                                        print(
                                                            'Realize a construção do capacete')
                                                    else:
                                                        print(
                                                            "Digite apenas 's' ou 'n'")

                                            elif drenagem == 'n':
                                                print(
                                                    'Realizar a drenagem de liquidos que estejam saindo pelo orifício criado no crânio')
                                            else:
                                                print(
                                                    "Digite apenas 's' ou 'n'")
                                        elif posCG == 'n':
                                            print(
                                                f'A canula guia deve ser introduzida até {posDV}')

                                    elif introduzirCanulaGuia == 'n':
                                        print('Introduzir a canula guia')

                                    else:
                                        print("Digite apenas 's' ou 'n'")

                                elif iniciarPerfuracao == 'n':
                                    print('Inicie a perfuração')

                                else:
                                    print("Digite apenas 's' ou 'n'")
                            elif L1L2 == '2':
                                print('-'*60)
                                print('Os pontos que devem ser utilizados serão:')
                                print(f'LL2 : {posLL2:.2f}')
                                print(f'AP: {posAP:.2f}')
                                print('-'*60)
                                iniciarPerfuracao = input(
                                    'Iniciar perfuração do crânio?\n(s/n): ')
                                print('-'*60)
                                if iniciarPerfuracao == 's':
                                    introduzirCanulaGuia = input(
                                        'Introduzir a cânula guia?\n(s/n): ')
                                    print('-'*60)
                                    if introduzirCanulaGuia == 's':
                                        print(
                                            f'A canula guia deve ser introduzida até {posDV:.2f} do Dorso Ventral(DV)')
                                        posCG = input(
                                            f'A canula guia foi introduzida até {posDV:.2f} do Dorso Ventral?\n(s/n): ')
                                        print('-'*60)
                                        if posCG == 's':
                                            print(
                                                'A canula guia foi introduzida corretamente')
                                            drenagem = input(
                                                'A drenagem de liquidos que estejam saindo pelo orifício criado no crânio foi realizada?\n(s/n): ')
                                            print('-'*60)
                                            if drenagem == 's':
                                                mistura = input(
                                                    'A mistura do acrílico polimerizante com o solvente foi realizada?(s/n): ')
                                                print('-'*60)
                                                if mistura == 's':
                                                    print(
                                                        'Com essa mistura, faça um capacete abrangendo o crânio, a cânula guia e o parafuso.')
                                                    capacete = input(
                                                        'O capacete foi feito?\n(s/n): ')
                                                    print('-'*60)
                                                    if capacete == 's':
                                                        secar = input(
                                                            'A mistura feita para o capacete já secou?\n(s/n): ')
                                                        print('-'*60)
                                                        if secar == 's':
                                                            print('\n'*10)
                                                            print(
                                                                'Os pontos que devem ser utilizados para a inserção da proxima Cânula Guia são:')
                                                            print(
                                                                f'LL1 : {posLL1:.2f}')
                                                            print(
                                                                f'AP: {posAP:.2f}')
                                                            print('-'*60)
                                                            iniciarPerfuracao = input(
                                                                'Iniciar perfuração do crânio?\n(s/n): ')
                                                            if iniciarPerfuracao == 's':
                                                                introduzirCanulaGuia = input(
                                                                    'Introduzir a cânula guia?\n(s/n): ')
                                                                print('-'*60)
                                                                if introduzirCanulaGuia == 's':
                                                                    print(
                                                                        f'A canula guia deve ser introduzida até {posDV:.2f} do Dorso Ventral(DV)')
                                                                    print(
                                                                        '-'*60)
                                                                    posCG = input(
                                                                        f'A canula guia foi introduzida até {posDV:.2f} do Dorso Ventral?\n(s/n): ')
                                                                    print(
                                                                        '-'*60)
                                                                    if posCG == 's':
                                                                        print(
                                                                            'A canula guia foi introduzida corretamente')
                                                                        drenagem = input(
                                                                            'A drenagem de liquidos que estejam saindo pelo orifício criado no crânio foi realizada?\n(s/n): ')
                                                                        print(
                                                                            '-'*60)
                                                                        if drenagem == 's':
                                                                            mistura = input(
                                                                                'A mistura do acrílico polimerizante com o solvente foi realizada?(s/n): ')
                                                                            print(
                                                                                '-'*60)
                                                                            if mistura == 's':
                                                                                print(
                                                                                    'Com essa mistura, faça um capacete abrangendo o crânio, a cânula guia e o parafuso.')
                                                                                capacete = input(
                                                                                    'O capacete foi feito?\n(s/n): ')
                                                                                print(
                                                                                    '-'*60)
                                                                                if capacete == 's':
                                                                                    secar = input(
                                                                                        'A mistura feita para o capacete já secou?\n(s/n): ')
                                                                                    print(
                                                                                        '-'*60)
                                                                                    if secar == 's':
                                                                                        print('\n'*10)
                                                                                        print(
                                                                                            'Procedimento realizado com sucesso!')
                                                                                        aparelho = False
                                                                                    elif secar == 'n':
                                                                                        print(
                                                                                            'Aguardar a mistura secar')
                                                                                    else:
                                                                                        print(
                                                                                            "Digite apenas 's' ou 'n'")
                                                                                elif capacete == 'n':
                                                                                    print(
                                                                                        'Realize a construção do capacete')
                                                                                else:
                                                                                    print(
                                                                                        "Digite apenas 's' ou 'n'")

                                                                        elif drenagem == 'n':
                                                                            print(
                                                                                'Realizar a drenagem de liquidos que estejam saindo pelo orifício criado no crânio')
                                                                        else:
                                                                            print(
                                                                                "Digite apenas 's' ou 'n'")
                                                                    elif posCG == 'n':
                                                                        print(
                                                                            f'A canula guia deve ser introduzida até {posDV}')

                                                                elif introduzirCanulaGuia == 'n':
                                                                    print(
                                                                        'Introduzir a canula guia')

                                                                else:
                                                                    print(
                                                                        "Digite apenas 's' ou 'n'")

                                                            elif iniciarPerfuracao == 'n':
                                                                print(
                                                                    'Inicie a perfuração')

                                                            else:
                                                                print(
                                                                    "Digite apenas 's' ou 'n'")
                                                            aparelho = False
                                                        elif secar == 'n':
                                                            print(
                                                                'Aguardar a mistura secar')
                                                        else:
                                                            print(
                                                                "Digite apenas 's' ou 'n'")
                                                    elif capacete == 'n':
                                                        print(
                                                            'Realize a construção do capacete')
                                                    else:
                                                        print(
                                                            "Digite apenas 's' ou 'n'")

                                            elif drenagem == 'n':
                                                print(
                                                    'Realizar a drenagem de liquidos que estejam saindo pelo orifício criado no crânio')
                                            else:
                                                print(
                                                    "Digite apenas 's' ou 'n'")
                                        elif posCG == 'n':
                                            print(
                                                f'A canula guia deve ser introduzida até {posDV}')

                                    elif introduzirCanulaGuia == 'n':
                                        print('Introduzir a canula guia')

                                    else:
                                        print("Digite apenas 's' ou 'n'")

                                elif iniciarPerfuracao == 'n':
                                    print('Inicie a perfuração')

                                else:
                                    print("Digite apenas 's' ou 'n'")
                        elif pontosFixacao == 'n':
                            print('-'*60)
                            print('Definir pontos de fixação')
                            print('-'*60)
                            print('REPETINDO PROCEDIMENTO')
                            print('-'*60)
                        else:
                            print("Digite apenas 's' ou 'n'")
                    elif poliacrilatoAplicado == 'n':
                        print('-'*60)
                        print('Aplicar Poliacrilato no perímetro externo')
                        print('-'*60)
                        print('REPETINDO PROCEDIMENTO')
                        print('-'*60)
                    else:
                        print("Digite apenas 's' ou 'n'")

                elif retirarPelagem == 'n':
                    print('-'*60)
                    print('Limpar o campo cirúrgico')
                    print('-'*60)
                    print('REPETINDO PROCEDIMENTO')
                    print('-'*60)
                else:
                    print("Digite apenas 's' ou 'n'")

            elif angulacao == 'n':
                print('-'*60)
                print('Verificar angulação da cabeça do animal')
                print('-'*60)
                print('REPETINDO PROCEDIMENTO')
                print('-'*60)
            else:
                print("Digite apenas 's' ou 'n'")

        elif anestesicosAplicados == 'n':
            print('-'*60)
            print('Aplicar anestésicos')
            print('-'*60)
            print('REPETINDO PROCEDIMENTO')
            print('-'*60)

        else:
            print('-'*60)
            print('Digite um comando válido')
            print('-'*60)
            print('REPETINDO PROCEDIMENTO')
            print('-'*60)
    else:
        print('Procedimento cirurgico não iniciado')

