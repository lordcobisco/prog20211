aproximacao = 30
faseAproximacao = []
faseSons = []
verificacao = []
informacoesAnimal = {'Habituação': [], 'Aproximação 1': [], 'Aproximação 2': [], 'Aproximação 3': [], 'Sons': [], 'Verificação': []}

# Funções

def habituacaoDoAnimal(habituacao):
    while habituacao != "s":
        print("Então habitue o animal para que ele possa prosseguir para o treinamento.\n")
        informacoesAnimal['Habituação'].append('O animal não está habituado.')
        habituacao = input("E agora, o animal já foi habituado? [s/n] ")
    else:
        faseAproximacao.append(True)
        informacoesAnimal['Habituação'].append('O animal está habituado.')
        print("Ok, o animal está pronto para o treinamento.\n")

def treinamentoAp3(toqueBarra):
    while toqueBarra < 20:
        print("O animal não tocou pelo menos 20 vezes na barra. Não seguir para a próxima fase. Repetir o procedimento.\n")
        informacoesAnimal['Aproximação 3'].append('O animal apertou alguma barra somente '+str(toqueBarra)+' vezes.')
        toqueBarra = int(input("E agora, o animal tocou quantas vezes na barra? "))
    else:
        informacoesAnimal['Aproximação 3'].append('O animal apertou alguma barra pelo menos 20 vezes. Foram '+str(toqueBarra)+' vezes.')
        print("Seguir para a próxima fase.\n")
        faseSons.append(True)

def treinamentoAp2(apertarBarraQualquer):
    while apertarBarraQualquer != "s":
        print("O animal não apertou a barra. Não seguir para a próxima fase. Repetir o procedimento.\n")
        informacoesAnimal['Aproximação 2'].append('O animal não apertou qualquer barra.')
        apertarBarraQualquer = input("E agora, o animal, além de se aproximar, apertou a barra? [s/n] ")
    else:
        informacoesAnimal['Aproximação 2'].append('O animal apertou alguma barra.')
        treinamentoAp3(int(input("O animal tocou quantas vezes na barra? ")))

def treinamentoAp1(aproximacao):
    while aproximacao >= 30:
        print("O animal não se aproximou, então não liberar recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
        informacoesAnimal['Aproximação 1'].append('O animal não se aproximou. Ele ficou a '+str(aproximacao)+' cm da barra.')
        aproximacao = float(input("E agora, qual a distância atual entre o animal e a barra em cm? "))
    else:
        print("O animal se aproximou, então liberar 0,5 ml de recompensa.\n")
        informacoesAnimal['Aproximação 1'].append('O animal se aproximou. Ele ficou a '+str(aproximacao)+' cm da barra.')
        treinamentoAp2(input("O animal, além de se aproximar, apertou a barra? [s/n] "))

def treinamentoSomPhee(apertarBarra):
    while apertarBarra != "esquerda":
        print("Não liberar a recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
        informacoesAnimal['Sons'].append('O animal não apertou a barra correta (som "phee"): '+apertarBarra+'.')
        apertarBarra = input("E agora, qual barra o animal apertou? [esquerda/direita] ")
    else:
        print("Liberar 0,5 ml de recompensa.\n")
        informacoesAnimal['Sons'].append('O animal apertou a barra correta (som "phee"): '+apertarBarra+'.')
        verificacao.append(True)

def treinamentoSomTrill(apertarBarra):
    while apertarBarra != "direita":
        print("Não liberar a recompensa. Não seguir para a próxima fase. Repetir o procedimento.\n")
        informacoesAnimal['Sons'].append('O animal não apertou a barra correta (som "trill"): '+apertarBarra+'.')
        apertarBarra = input("E agora, qual barra o animal apertou? [esquerda/direita] ")
    else:
        print("Liberar 0,5 ml de recompensa.\n")
        informacoesAnimal['Sons'].append('O animal apertou a barra correta (som "trill"): '+apertarBarra+'.')
        verificacao.append(True)

def treinamentoVerificacao(proxFase):
    while proxFase != "s":
        print("Infelizmente, o animal não pode seguir para a próxima fase. Deixar o animal descansar e repetir o procedimento depois.\n")
        informacoesAnimal['Verificação'].append('O experimento não foi feito com sucesso 50 vezes e dentro de 30 min.')
        proxFase = input("E agora, os experimentos foram realizados com sucesso 50 vezes e dentro de 30 minutos? [s/n] ")
    else:
        print("Perfeito, o animal pode seguir para a próxima fase.")
        informacoesAnimal['Verificação'].append('O experimento foi feito com sucesso 50 vezes e dentro de 30 min.')
        print("\nFim do programa de treinamento.\n")

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
   print("\nFim do programa de treinamento.\n")

# Salvar as informações geradas:

modo_salvar = input("Você deseja salvar as informações do treinamento do animal em que formato? [csv/txt] ")
nome_arquivo = input("Qual o nome que deseja dar para o referido arquivo? ")

while modo_salvar != 'csv' and modo_salvar != 'txt':
    modo_salvar = input('Desculpe, não entendi o formato que você deseja. Digite um formato adequado: [csv/txt] ')

else:
    if modo_salvar == 'csv':
        import csv

        with open((nome_arquivo+'.csv'),'w',newline='') as arquivo_csv:
            arquivo_escrita = csv.writer(arquivo_csv,delimiter=',')

            arquivo_escrita.writerow(['Habituação'] + ['Aproximação 1'] + ['Aproximação 2'] + ['Aproximação 3'] + ['Sons'] + ['Verificação'])
            arquivo_escrita.writerow([informacoesAnimal['Habituação']] + [informacoesAnimal['Aproximação 1']] + [informacoesAnimal['Aproximação 2']]
            + [informacoesAnimal['Aproximação 3']] + [informacoesAnimal['Sons']] + [informacoesAnimal['Verificação']])

        print('Os dados já foram salvos no formato .csv.')

    elif modo_salvar == 'txt':

        arquivo_txt = open((nome_arquivo+'.txt'),'w')

        arquivo_txt.write('Habituação: '+str(informacoesAnimal['Habituação'])+'\n')
        arquivo_txt.write('\nAproximação 1: '+str(informacoesAnimal['Aproximação 1'])+'\n')
        arquivo_txt.write('\nAproximação 2: '+str(informacoesAnimal['Aproximação 2'])+'\n')
        arquivo_txt.write('\nAproximação 3: '+str(informacoesAnimal['Aproximação 3'])+'\n')
        arquivo_txt.write('\nSons: '+str(informacoesAnimal['Sons'])+'\n')
        arquivo_txt.write('\nVerificação: '+str(informacoesAnimal['Verificação'])+'\n')

        arquivo_txt.close()

        print('Os dados já foram salvos no formato .txt.')
