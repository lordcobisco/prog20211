# Variáveis

limpeza = [False,False,False]
perfuracao = [False,False,False]
nomesPosicoes = ['AP','LL1','LL2','DV']
valoresPosicoes = {'AP': 6.42, 'LL1': 3.23, 'LL2': 3.23,'DV': 4.20}
hipocampoCA1 = (-0.42, -0.30, 0.30, -0.20)
mistura = []
finalizacao = [0,0,0]

# Inicialização

print("Olá, usuário, este é o programa de auxílio e automação da cirurgia estereotáxica em animais.\n")

# Etapa I

print("A primeira etapa consiste em administrar a anestesia no animal. Para este tipo de procedimento cirúrgico, é indicado o uso de ketamina mais xilazina ou de halotano gasoso.")

anestesiaEscolhida = input("Qual dos anéstesicos deve ser utilizado? [ketamina mais xilazina/halotano gasoso] ")
pesoAnimal = input("Qual o peso do animal em 'g'? ")
quantidadeAnestesia = input("Qual a quantidade do respectivo fármaco em 'ml'? ")

verifAnestesia = input("\nPor favor, verifique a dosagem: a quantidade de "+quantidadeAnestesia+" ml de "+anestesiaEscolhida+" está condizente com um animal de "+pesoAnimal+" g? [s/n] ")

while verifAnestesia != "s":
    print("Se a dosagem está incorreta, por favor, informe mais uma vez os parâmetros escolhidos:")
    anestesiaEscolhida = input("Qual fármaco deve ser utilizado? [ketamina mais xilazina/halotano gasoso] ")
    pesoAnimal = input("Por favor, informe o peso do animal em 'g': ")
    quantidadeAnestesia = input("Qual a quantidade do respectivo fármaco em 'ml'? ")

    verifAnestesia = input("\nPor favor, verifique a nova dosagem: a quantidade de "+quantidadeAnestesia+" ml de "+anestesiaEscolhida+" está condizente com um animal de "+pesoAnimal+" g? [s/n] ")
else:
    print("\nÓtimo, aplicar no animal o anestésico e vamos prosseguir...\n")

# Etapa II

print("A segunda etapa consiste em esperar o anestésico fazer efeito, posicionar o animal no estereotáxico e ajustar a angulação da cabeça do animal.\n")

anestesiaEfeito = input("A anestesia já fez efeito completo no animal? [s/n] ")

while anestesiaEfeito != "s":
    print("Vamos esperar o anestésico fazer efeito...")
    anestesiaEfeito = input("E agora, a anestesia já fez efeito completo no animal? [s/n] ")
else:
    print("\nOk, vamos prosseguir para o estereotáxico.\n")

print("As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal. Normalmente o animal dá uma pequena piscada, devido ao estímulo da musculatura responsável por este movimento.\n")

barras = input("As barras foram posicionadas? [s/n] ")
while barras != "s":
    print("Posicione as barras.")
    barras = input("E agora, as barras foram posicionadas? [s/n] ")
else:
    piscar = input("O animal piscou? [s/n] ")
    while piscar != "s":
        print("As barras ainda não estão corretamente posicionadas. Reposicione-as, por favor.")
        piscar = input("E agora, o animal piscou? [s/n] ")
    else:
        print("\nOk, vamos prosseguir para a angulação.\n")

print("Agora, vamos verificar a angulação da cabeça do animal, a qual deve estar sem diferenças de angulação entre os pontos 'Bregma' e 'Lambda'.")

angulacao = input("Há diferença de angulação na cabeça do animal entre os pontos 'Bregma' e 'Lambda'? [s/n] ")
while angulacao != "n":
    print("Por favor, ajuste a angulação para que não haja diferença.")
    angulacao = input("E agora, ainda há diferença de angulação na cabeça do animal entre os pontos 'Bregma' e 'Lambda'? [s/n] ")
else:
    print("\nÓtimo, vamos prosseguir...\n")

# Etapa III

print("A terceira etapa consiste em realizar a limpeza do campo de trabalho. Retire a pelagem que recobre a parte superior da calota craniana. Retire os tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana. Por último e não menos importante limpe a calota craniana de qualquer resto de 'pele' que esteja sobrando utilizando H²O² 10 volumes.\n")

while limpeza[0] == False:
    respostaLimpeza = input("Você retirou a pelagem? [s/n] ")
    if respostaLimpeza == "s":
        limpeza[0] = True
        continue
    print("Por favor, retire a pelagem.")
while limpeza[1] == False:
    respostaLimpeza = input("Você retirou os tecidos moles? [s/n] ")
    if respostaLimpeza == "s":
        limpeza[1] = True
        continue
    print("Por favor, retire os tecidos moles.")
while limpeza[2] == False:
    respostaLimpeza = input("Você limpou a calota craniana? [s/n] ")
    if respostaLimpeza == "s":
        limpeza[2] = True
        continue
    print("Por favor, limpe a calota craniana.")

if limpeza == [True,True,True]:
    print("\nÓtimo, a limpeza do campo de trabalho foi feita integralmente. Vamos prosseguir...\n")

# Etapa IV

print("A quarta etapa consiste em aplicar uma camada de poliacrilato em todo o perímetro externo para evitar sangramentos.\n")

poliacrilato = input("Você aplicou o poliacrilato em todo o perímetro externo? [s/n] ")

while poliacrilato != "s":
    print("Para prosseguir, é imprescindível aplicar o poliacrilato para evitar sangramentos.")
    poliacrilato = input("E agora, você já aplicou o poliacrilato em todo o perímetro externo? [s/n] ")
else:
    print("\nÓtimo, a aplicação de poliacrilato foi feita com sucesso. Vamos prosseguir...\n")

# Etapa V

print("A quinta etapa consiste em fixar os parafusos.\n")

parafusos = int(input("Qual a quantidade de parafusos que irá ser utilizada? "))

for i in range(parafusos):
    tamanhoParafuso = input("Qual o tamanho do parafuso "+str(i+1)+" de "+str(parafusos)+"? [pequeno/grande] ")
    if tamanhoParafuso == "grande":
        print("Como o parafuso "+str(i+1)+" é grande, dê no máximo 3 voltas.")
    else:
        print("Como o parafuso "+str(i+1)+" é pequeno, dê quantas voltas achar necessário mas tenha cuidado para não aprofundar muito.")

fixarParafusos = input("Você já fixou todos os parafusos? [s/n] ")

while fixarParafusos != "s":
    print("Fixe os parafusos para que possamos prosseguir.")
    fixarParafusos = input("E agora, todos os parafusos estão fixados? [s/n] ")
else:
    print("\nÓtimo, os parafusos foram fixados. Vamos prosseguir...\n")

# Etapa VI

print("A sexta etapa consiste em localizar os pontos de inserção das cânulas-guia.\n")

print("Os valores prévios das posições nas réguas do estereotáxico são os seguintes:",valoresPosicoes)

prosseguir = (input("Esses valores das posições não estão condizentes com a estrutura-alvo 'hipocampo (CA1)', mas não se preocupe, o próprio programa faz o cálculo de maneira automática. Para dar início ao cálculo, digite o número um (1): "))
while int(prosseguir) != 1:
    prosseguir = input("Você não digitou o número um (1). Estou no aguardo: ")
else:
    print("Certo, o cálculo para designar os valores corretos vai iniciar...")
    for i in range(len(valoresPosicoes)):
       valoresPosicoes[(nomesPosicoes[i])] += hipocampoCA1[i]

print("\nOs novos valores das posições são:",valoresPosicoes)

while 1 == 1:
    hemisferio1 = input("\nPor favor, escolha com qual hemisfério do eixo 'LateroLateral' devemos começar a inserção: [esquerdo/direito] ")
    if hemisferio1 == "esquerdo":
        print("Você escolheu começar com a cânula-guia da posição 'LateroLateral'",valoresPosicoes['LL1'],"cm.")
        lateroLateral1 = valoresPosicoes['LL1']
        lateroLateral2 = valoresPosicoes['LL2']
        hemisferio2 = "direito"
        break
    elif hemisferio1 == "direito":
        print("Você escolheu começar com a cânula-guia da posição 'LateroLateral'",valoresPosicoes['LL2'],"cm.")
        lateroLateral1 = valoresPosicoes['LL2']
        lateroLateral2 = valoresPosicoes['LL1']
        hemisferio2 = "esquerdo"
        break
    else:
        print("Você digitou alguma coisa diferente de 'esquerdo' ou 'direito'.")

print("\nÓtimo, os valores estão corretos e o primeiro hemisfério foi escolhido. Vamos prosseguir...\n")

# Etapa VII

print("A sétima etapa consiste em perfurar o crânio. Você deve ligar a broca, apoiar a mão firmemente contra o assoalho ou no esterotáxico e realizar a perfuração a aproximadamente 45 graus.\n")

while perfuracao[0] == False:
    respostaPerfuracao = input("Você ligou a broca? [s/n] ")
    if respostaPerfuracao == "s":
        perfuracao[0] = True
        continue
    print("Por favor, ligue a broca")
while perfuracao[1] == False:
    respostaPerfuracao = input("Você apoiou a mão de maneira firme? [s/n] ")
    if respostaPerfuracao == "s":
        perfuracao[1] = True
        continue
    print("Por favor, apoie a mão.")
while perfuracao[2] == False:
    respostaPerfuracao = input("Você ajustou o ângulo de perfuração para 45 graus? [s/n] ")
    if respostaPerfuracao == "s":
        perfuracao[2] = True
        continue
    print("Por favor, ajuste o ângulo.")

if perfuracao == [True,True,True]:
    print("\nÓtimo, pode perfurar o alvo. Após isso, vamos prosseguir...\n")

# Etapa VIII
    
print("A oitava etapa consiste em inserir a primeira cânula-guia no hemisfério escolhido: "+hemisferio1+" (eixo 'LateroLateral', posição "+str(lateroLateral1)+" cm). Insira-a até o valor exato de "+str(valoresPosicoes['DV'])+" cm, calculado previamente para o eixo 'DorsoVentral'.")

insercaoDV1 = input("Você inseriu a cânula-guia corretamente? [s/n] ")

while insercaoDV1 != "s":
    print("Por favor, insira a cânula-guia corretamente.")
    insercaoDV1 = input("Você já inseriu a cânula-guia corretamente? [s/n] ")
else:
    print("\nÓtimo, a primeira cânula-guia foi inserida com sucesso. Vamos prosseguir...\n")

# Etapa IX

print("A nona etapa consiste em drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso, utilize pequenos rolos de papel absorvente.\n")

sangue = input("Há sangue saindo pelo orifício craniano? [s/n] ")
liquido = input("Há líquido cefalorraquidiano saindo pelo orifício craniano? [s/n] ")

if sangue == "s" and liquido == "n":
    print("Por favor, drene o sangue.")
    drenar = 0
elif sangue == "s" and liquido == "s":
    print("Por favor, drene o sangue e o líquido cefalorraquidiano.")
    drenar = 0
elif sangue == "n" and liquido == "s":
    print("Por favor, drene o líquido cefalorraquidiano.")
    drenar = 0
elif sangue == "n" and liquido == "n":
    print("Ok, você não precisa drenar o local.")
    drenar = 1
else:
    print("Não entendi o que você disse. De qualquer modo, drene qualquer líquido do local.")
    drenar = 0

if drenar != 1:
    drenar = input("\nVocê drenou e deixou a superfície seca e limpa? [s/n] ")
    while drenar != "s":
        print("Por favor, faça a drenagem. Ela é imprescindível.")
        drenar = input("E agora, você drenou e deixou a superfície seca e limpa? [s/n] ")
    else:
        print("\nOk, agora vamos prosseguir...\n")
else:
    print("\nÓtimo, a drenagem foi realizada com sucesso. Vamos prosseguir...\n")

# Etapa X

print("A décima etapa consiste em criar uma mistura de acrílico polimerizante com o solvente e aplicá-la no local.\n")

while mistura == []:
    acrilicoSolvente = input("Você já misturou o acrílico polimerizante com o solvente? [s/n] ")
    if acrilicoSolvente == "s":
        mistura.append(True)
        continue
    print("Por favor, faça a mistura requisitada.")

while mistura == [True]:
    texturaMistura = input("A mistura está espessa e maleável ao mesmo tempo? [s/n] ")
    if texturaMistura == "s":
        mistura.append(True)
        continue
    print("Por favor, dilua ou concentre a mistura.")

if mistura == [True,True]:
    print("\nPode aplicar a mistura: abranja o crânio, a cânula-guia e os parafusos. Deixe um espaço entre o capacete e o início da área tecidual para evitar descolamentos futuros. Após isso, deixe-a secar. Atenção: o tempo pode variar de acordo com a temperatura e umidade da sala.\n")

while mistura == [True,True]:
    secarMistura = input("A mistura aplicada já secou? [s/n] ")
    if secarMistura == "s":
        mistura.append(True)
        continue
    print("Por favor, espere a mistura aplicada secar.")

if mistura == [True,True,True]:
    print("\nÓtimo, a aplicação e secagem da mistura aconteceu com sucesso. Vamos prosseguir...\n")

# Etapa XI

print("A décima-primeira etapa consiste em inserir uma segunda cânula-guia no hemisfério "+hemisferio2+" (eixo 'LateroLateral', posição "+str(lateroLateral2)+" cm). Antes, porém, é necessário gentilmente levantar o braço do equipamento estereotáxico, cuidando para não mexer a cânula-guia do hemisfério "+hemisferio1+".\n")

levantarEstereotaxico = input("Você levantou o braço do estereotáxico levemente? [s/n] ")

while levantarEstereotaxico != "s":
    print("Por favor, levante-o com cuidado.")
    levantarEstereotaxico = input("Você já levantou o estereotáxico levemente? [s/n] ")
else:
    print("Certo, pode inserir a segunda cânula-guia até o valor exato de "+str(valoresPosicoes['DV'])+" cm, calculado previamente para o eixo 'DorsoVentral'.")

insercaoDV2 = input("Você inseriu a cânula-guia corretamente? [s/n] ")

while insercaoDV2 != "s":
    print("Por favor, insira a cânula-guia corretamente.")
    insercaoDV2 = input("Você já inseriu a cânula-guia corretamente? [s/n] ")
else:
    print("\nÓtimo, a inserção da segunda cânula-guia foi realizada com sucesso. Vamos prosseguir...\n")

# Etapa XII

print("A décima-segunda etapa consiste em, mais uma vez, drenar qualquer sangue ou líquido cefalorraquidiano e, após isso, aplicar mais da mistura de acrílico polimerizante com solvente.\n")

sangue = input("Há sangue saindo pelo orifício craniano? [s/n] ")
liquido = input("Há líquido cefalorraquidiano saindo pelo orifício craniano? [s/n] ")

if sangue == "s" and liquido == "n":
    print("Por favor, drene o sangue.")
    drenar = 0
elif sangue == "s" and liquido == "s":
    print("Por favor, drene o sangue e o líquido cefalorraquidiano.")
    drenar = 0
elif sangue == "n" and liquido == "s":
    print("Por favor, drene o líquido cefalorraquidiano.")
    drenar = 0
elif sangue == "n" and liquido == "n":
    print("Ok, você não precisa drenar o local.")
    drenar = 1
else:
    print("Não entendi o que você disse. De qualquer modo, drene qualquer líquido do local.")
    drenar = 0

if drenar != 1:
    drenar = input("\nVocê drenou e deixou a superfície seca e limpa? [s/n] ")
    while drenar != "s":
        print("Por favor, faça a drenagem. Ela é imprescindível.")
        drenar = input("E agora, você drenou e deixou a superfície seca e limpa? [s/n] ")
    else:
        print("\nOk, agora você pode aplicar a mistura.\n")
else:
    print("\nOk, você pode aplicar a mistura. Lembre-se de deixar um espaço entre o capacete e o início da área tecidual para evitar descolamentos futuros.\n")

mistura.pop(2)

while mistura == [True,True]:
    secarMistura = input("A mistura aplicada já secou? [s/n] ")
    if secarMistura == "s":
        mistura.append(True)
        continue
    print("Por favor, espere a mistura aplicada secar.")

print("\nÓtimo, mais uma vez, a drenagem e a aplicação foram realizadas com sucesso. Vamos prosseguir...\n")

# Etapa XIII

print("A décima-terceira e última etapa consiste em gentilmente levantar todo o estereotáxico e acomodar o animal, primeiro em um ambiente separado, e depois em seu ambiente normal.")

while finalizacao == [0,0,0]:
    levantarEstereotaxico = input("Você já levantou cuidadosamente todo o estereotáxico? [s/n] ")
    if levantarEstereotaxico == "s":
        finalizacao[0] = 1
        print("Certo, pode retirar o animal.")
        continue
    else:
        print("Por favor, levante o equipamento conforme solicitado.")

while finalizacao == [1,0,0]:
    acomodarAnimal = input("Você já acomodou o animal em um ambiente aquecido, com uma lâmpada e sem a presença de outros animais? [s/n] ")
    if acomodarAnimal == "s":
        finalizacao[1] = 1
        print("Certo, esperar o animal acordar.")
        continue
    else:
        print("Por favor, acomode o animel conforme solicitado.")

while finalizacao == [1,1,0]:
    acordarAnimal = input("O animal que está no ambiente separado já acordou? [s/n] ")
    if acordarAnimal == "s":
        finalizacao[2] = 1
        print("Certo, pode levá-lo agora para seu ambiente normal, para o convívio com os outros animais.")
        continue
    else:
        print("Por favor, espere o animal acordar.")

if finalizacao == [1,1,1]:
    print("Todo o procedimento foi feito com sucesso. Parabéns, usuário.")
    print("O programa agora irá se encerrar...")
