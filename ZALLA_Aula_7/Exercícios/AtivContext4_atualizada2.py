aproximacao = 30
faseAproximacao = []
faseSons = []
verificacao = []

# Funções

def habituacaoDoAnimal(habituacao):
    while habituacao != "s":
        print("Então habitue o animal para que ele possa prosseguir para o treinamento.\n")
        habituacao = input("E agora, o animal já foi habituado? [s/n] ")
    else:
        faseAproximacao.append(True)
        print("Ok, o animal está pronto para o treinamento.\n")

def treinamentoAp3(toqueBarra):
    while toqueBarra < 20:
        print("O animal não tocou pelo menos 20 vezes na barra. Não seguir para a próxima fase. Repetir o procedimento.\n")
        toqueBarra = int(input("E agora, o animal tocou quantas vezes na barra? "))
    else:
        print("Seguir para a próxima fase.\n")
        faseSons.append(True)

def treinamentoAp2(apertarBarraQualquer):
    while apertarBarraQualquer != "s":
        print("O animal não apertou a barra. Não seguir para a próxima fase. Repetir o procedimento.\n")
        apertarBarraQualquer = input("E agora, o animal, além de se aproximar, apertou a barra? [s/n] ")
    else:
        treinamentoAp3(int(input("O animal tocou quantas vezes na barra? ")))

def treinamentoAp1(aproximacao):
    while aproximacao >= 30:
        print("O animal não se aproximou, então não liberar recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
        aproximacao = float(input("E agora, qual a distância atual entre o animal e a barra em cm? "))
    else:
        print("O animal se aproximou, então liberar 0,5 ml de recompensa.\n")
        treinamentoAp2(input("O animal, além de se aproximar, apertou a barra? [s/n] "))

def treinamentoSomPhee(apertarBarra):
    while apertarBarra != "esquerda":
        print("Não liberar a recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
        apertarBarra = input("E agora, qual barra o animal apertou? [esquerda/direita] ")
    else:
        print("Liberar 0,5 ml de recompensa.\n")
        verificacao.append(True)

def treinamentoSomTrill(apertarBarra):
    while apertarBarra != "direita":
        print("Não liberar a recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
        apertarBarra = input("E agora, qual barra o animal apertou? [esquerda/direita] ")
    else:
        print("Liberar 0,5 ml de recompensa.\n")
        verificacao.append(True)

def treinamentoVerificacao(proxFase):
    while proxFase != "s":
        print("Infelizmente, o animal não pode seguir para a próxima fase. Deixar o animal descansar e repetir o procedimento depois.\n")
        proxFase = input("E agora, os experimentos foram realizados com sucesso 50 vezes e dentro de 30 minutos? [s/n] ")
    else:
        print("Perfeito, o animal pode seguir para a próxima fase.")
        print("\nFim do programa de treinamento.")

# Habituação do animal (fase de habituação)

habituacaoDoAnimal(input("O animal já está habituado? [s/n] "))

# Treinamento do animal (fase de aproximação)

if faseAproximacao == [True]:
    print("O treinamento irá começar. Inicialmente, o animal se encontra a",aproximacao,"cm de distância da barra. Perceba se há mudança nessa distância nos próximos segundos.")
    print("...")
    print("...")
    print("...")
    treinamentoAp1(float(input("Agora, por favor, informe a distância atual entre o animal e a barra em cm: ")))

# Treinamento do animal (fase de sons)

if faseSons == [True]:
    print("A fase do treinamento em que sons 'Phee' ou 'Trill' são emitidos irá começar.")
    som = input("Deseja emitir qual som? [phee/trill] ")
    print("...")
    print("...")
    print("...")
    if som == "phee":
        treinamentoSomPhee(input("O som 'Phee' foi emitido. Qual barra o animal apertou? [esquerda/direita] "))
    elif som == "trill":
        treinamentoSomTrill(input("O som 'Trill' foi emitido. Qual barra o animal apertou? [esquerda/direita] "))
    else:
        print("Resposta inválida. Reinicie o trainamento.")

# Treinamento do animal (verificação)

if verificacao == [True]:
    treinamentoVerificacao(input("Os experimentos foram realizados com sucesso 50 vezes e dentro de 30 minutos? [s/n] "))
else:
   print("\nFim do programa de treinamento.")
