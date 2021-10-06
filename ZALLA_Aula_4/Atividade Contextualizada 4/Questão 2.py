aproximacao = 30
faseAproximacao = False
faseSons = False
verificacao = False

# Habituação do animal (fase de habituação)

habituação = input("O animal já está habituado? [s/n] ")

if habituação == "s":
    faseAproximacao = True
    print("Ok, o animal está pronto para o treinamento.")
elif habituação == "n":
    print("Habitue o animal antes de seguir para o treinamento.")
else:
    print("Resposta inválida. Reinicie o programa.")

# Treinamento do animal (fase de aproximação)

if faseAproximacao == True:
    print("O treinamento irá começar. Inicialmente, o animal se encontra a",aproximacao,"cm de distância da barra. Perceba se há mudança nessa distância nos próximos segundos.")
    print("...")
    print("...")
    print("...")
    aproximacao = float(input("Agora, por favor, informe a distância atual entre o animal e a barra em cm: "))
    if aproximacao < 30:
        print("O animal se aproximou, então liberar 0,5 ml de recompensa.")
        apertarBarraQualquer = input("O animal, além de se aproximar, apertou a barra? [s/n] ")
        if apertarBarraQualquer == "s":
            toqueBarra = int(input("O animal tocou quantas vezes na barra? "))
            if toqueBarra >= 20:
                print("Seguir para a próxima fase.")
                faseSons = True
            elif toqueBarra <20:
                print("Não seguir para a próxima fase. Reiniciar o treinamento, repetir habituação ou testar novo indivíduo.")
            else:
                print("Resposta inválida. Reinicie o treinamento.")
        elif apertarBarraQualquer == "n":
                print("Não seguir para a próxima fase. Reiniciar o treinamento, repetir habituação ou testar novo indivíduo.")
        else:
            print("Resposta inválida. Reinicie o treinamento.")
    elif aproximacao >= 30:
        print("O animal não se aproximou, então não liberar recompensa. Não seguir para a próxima fase. Reiniciar o treinamento, repetir habituação ou testar novo indivíduo.")
    else:
        print("Resposta inválida. Reinicie o treinamento.")

# Treinamento do animal (fase de sons)

if faseSons == True:
    print("A fase do treinamento em que sons 'Phee' ou 'Trill' são emitidos irá começar.")
    som = input("Deseja emitir qual som? [phee/trill] ")
    print("...")
    print("...")
    print("...")
    apertarBarra = input("Qual barra o animal apertou? [esquerda/direita] ")
    if (som == "phee") and (apertarBarra == "esquerda"):
        print("Liberar 0,5 ml de recompensa.")
        verificacao = True
    elif (som == "phee") and (apertarBarra == "direita"):
        print("Não liberar a recompensa. Não seguir para a próxima fase. Reiniciar o treinamento, repetir habituação ou testar novo indivíduo.")
    elif (som == "trill") and (apertarBarra == "direita"):
        print("Liberar 0,5 ml de recompensa.")
        verificacao = True
    elif (som == "trill") and (apertarBarra == "esquerda"):
        print("Não liberar a recompensa. Não seguir para a próxima fase. Reiniciar o treinamento, repetir habituação ou testar novo indivíduo.")
    else:
        print("Respostas inválidas. Reinicie o treinamento.")

# Treinamento do animal (verificação)

if verificacao == True:
    proxFase = input("Os experimentos foram realizados com sucesso 50 vezes e dentro de 30 minutos? [s/n] ")
    if proxFase == "s":
        print("Perfeito, o animal pode seguir para a próxima fase.")
    elif proxFase == "n":
        print("Infelizmente, o animal não pode seguir para a próxima fase. Deixar o animal descansar ou testar novo indivíduo.")
    else:
        print("Resposta inválida. Reinicie o treinamento.")
else:
    print("Fim do programa de treinamento.")
