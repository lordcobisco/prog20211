toqueBarra = 0
aproximacao = 30
faseAproximacao = False
faseSons = False
verificacao = False

# Habituação do animal (fase de habituação)

habituação = input("O animal já está habituado? [s/n] ")

while habituação != "s":
    print("Então habitue o animal para que ele possa prosseguir para o treinamento.\n")
    habituação = input("E agora, o animal já foi habituado? [s/n] ")
else:
    faseAproximacao = True
    print("Ok, o animal está pronto para o treinamento.")

# Treinamento do animal (fase de aproximação)

if faseAproximacao == True:
    print("O treinamento irá começar. Inicialmente, o animal se encontra a",aproximacao,"cm de distância da barra. Perceba se há mudança nessa distância nos próximos segundos.")
    print("...")
    print("...")
    print("...")
    aproximacao = float(input("Agora, por favor, informe a distância atual entre o animal e a barra em cm: "))
    while aproximacao >= 30:
        print("O animal não se aproximou, então não liberar recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
        aproximacao = float(input("E agora, qual a distância atual entre o animal e a barra em cm? "))
    else:
        print("O animal se aproximou, então liberar 0,5 ml de recompensa\n.")
        apertarBarraQualquer = input("O animal, além de se aproximar, apertou a barra? [s/n] ")
        while apertarBarraQualquer != "s":
            print("O animal não apertou a barra. Não seguir para a próxima fase. Repetir o procedimento.\n")
            apertarBarraQualquer = input("E agora, o animal, além de se aproximar, apertou a barra? [s/n] ")
        else:
            toqueBarra = int(input("O animal tocou quantas vezes na barra? "))
            while toqueBarra < 20:
                print("O animal não tocou pelo menos 20 vezes na barra. Não seguir para a próxima fase. Repetir o procedimento.\n")
                toqueBarra = int(input("E agora, o animal tocou quantas vezes na barra? "))
            else:
                print("Seguir para a próxima fase.\n")
                faseSons = True

# Treinamento do animal (fase de sons)

if faseSons == True:
    print("A fase do treinamento em que sons 'Phee' ou 'Trill' são emitidos irá começar.")
    som = input("Deseja emitir qual som? [phee/trill] ")
    print("...")
    print("...")
    print("...")
    if som == "phee":
        apertarBarra = input("O som 'phee' foi emitido. Qual barra o animal apertou? [esquerda/direita] ")
        while apertarBarra != "esquerda":
            print("Não liberar a recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
            apertarBarra = input("E agora, qual barra o animal apertou? [esquerda/direita] ")
        else:
            print("Liberar 0,5 ml de recompensa.\n")
            verificacao = True
    elif som == "trill":
        apertarBarra = input("O som 'trill' foi emitido. Qual barra o animal apertou? [esquerda/direita] ")
        while apertarBarra != "direita":
            print("Não liberar a recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
            apertarBarra = input("E agora, qual barra o animal apertou? [esquerda/direita] ")
        else:
            print("Liberar 0,5 ml de recompensa.")
            verificacao = True
    else:
        print("Resposta inválida. Reinicie o trainamento.")

# Treinamento do animal (verificação)

if verificacao == True:
    proxFase = input("Os experimentos foram realizados com sucesso 50 vezes e dentro de 30 minutos? [s/n] ")
    while proxFase != "s":
        print("Infelizmente, o animal não pode seguir para a próxima fase. Deixar o animal descansar e repetir o procedimento depois.")
        proxFase = input("E agora, os experimentos foram realizados com sucesso 50 vezes e dentro de 30 minutos? [s/n] ")
    else:
        print("Perfeito, o animal pode seguir para a próxima fase.")
        print("Fim do programa de treinamento.")
else:
   print("Fim do programa de treinamento.")