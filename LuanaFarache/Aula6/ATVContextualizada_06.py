'''
Rotina criada para atender aos requisitos da atividade contextualizada 6 - Disciplina de introdução à programação.

Desenvolva um programa em Python que automatize o procedimento cirúrgico estereotáxico apresentado, assumindo que:

a.	As entradas (seja informações de máquina, posicionamentos a serem medidos etc.) serão traduzidas em inputs no programa.
b.	O detalhamento das etapas é informado na tela para o usuário a cada passo do procedimento.
c.	O programa deve conter estruturas de tomada de decisão (if-elif-else).
d.	O programa deve conter estruturas de repetição (while-for).
e.	O programa deve conter pelo menos 1 variável de cada tipo (lista, tupla e dicionário)

'''

# Automatização de cirurgia estereotáxia em animais para fins de pesquisa:

#QUESTÃO A)
OpAnimal=('Rato','Camudongo','Coelho')
Animal=0
while Animal==0:
    Animal = int(input('Insira uma valor de 1 a 3 para informar a espécie de animal: \n 1-Rato \n 2-Camudongo \n 3-Coelho \n'))
    if Animal == 1 or Animal == 2 or Animal == 3:
        print('Você escolheu a opção:',OpAnimal[Animal-1],'\n')
    else:
        print('Digite uma informação válida!!')
        Animal=0

OpAnestesia=('Cetamina + Xilazina','Cetamina + Midazolan','Halotano(Gasoso)')
Anestesia=0
while Anestesia==0:
    Anestesia = int(input('Insira uma valor de 1 a 3 para informar os fármacos anestésicos: \n 1-Cetamina + Xilazina \n 2-Cetamina + Midazolan \n 3-Halotano(Gasoso) \n'))
    if Anestesia == 1 or Anestesia == 2 or Anestesia == 3:
        print('Você escolheu a opção:',OpAnestesia[Anestesia-1],'\n')
    else:
        print('Digite uma informação válida!! \n')
        Anestesia=0

Peso = int(input('Insira o valor do peso do animal em kg: \n'))

if Anestesia == 1:
    if Animal == 1 or Animal == 2:
        Cetamina=80*Peso
        Xilazina=15*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Xilazina,' mg de Xilazina \n')
    else: 
        Cetamina=50*Peso
        Xilazina=10*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Xilazina,' mg de Xilazina \n')
elif Anestesia == 2:
    if Animal == 1 or Animal == 2:
        Cetamina=80*Peso
        Midazolan=5*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Midazolan,' mg de Midazolan \n')
    else:
        Cetamina=50*Peso
        Midazolan=2*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Midazolan,' mg de Midazolan \n')   
else:
    print('Para anestesiar o animal, realize a indução com agente inalatório Halotano em até 5% e Manutenção entre 1 a 3% \n')

print('Realize o POSICIONAMENTO do animal no estereotáxico. Verifique a angulação da cabeça do animal, a qual deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana. \n')
Posicionamento=0
while Posicionamento==0:
    Posicionamento = int(input('O posicionamento do Animal foi realizado adequadamente? Insira 0 ou 1 para: \n 0 - Animal BEM Posicionado \n 1 - Animal MAL Posicionado \n'))
    if Posicionamento == 1:
        print('Você escolheu realizou o posicionamento do animal adequadamente! \n')
    elif Posicionamento == 0:
        print('Ajuste o posicionamento do Animal... \n')
    else:
        print('Digite uma informação válida!! \n')
        Posicionamento=0

print('Realize a LIMPEZA do campo de trabalho. \n')
Limpeza=0
while Limpeza==0:
    Limpeza = int(input('A LIMPEZA do campo de trabalho foi realiza? Insira 0 ou 1 para: \n 0 - Não \n 1 - Sim \n'))
    if Limpeza == 1:
        print('Você escolheu realizou a LIMPEZA! \n')
    elif Limpeza == 0:
        print('Faça a LIMPEZA do campo de trabalho... \n')
    else:
        print('Digite uma informação válida!! \n')
        Limpeza=0

# I.	Procedimento de anestesia: Pode-se utilizar uma diversidade de fármacos para anestesia os animais, dentre eles Ketamina e xilazina utilizados em conjunto, halotano (gasoso). Verificar a dosagem correta de acordo com o peso dos animais.
# II.	Depois do anestésico ter feito efeito, deve-se posicionar o animal no estereotáxico. As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal. Normalmente o animal dá uma pequena piscada, devido ao estímulo da musculatura responsável por este movimento. Em seguida verificar a angulação da cabeça do animal, a qual deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana.
# III.	Limpeza do campo de trabalho: Este procedimento requer o cumprimento de algumas etapas: Retirada da pelagem que recobre a parte superior da calota craniana, Retirada dos tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana. Por último e não menos importante deve-se limpar a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H2O2 10 volumes.
# IV.	Com o animal em posição e com o campo cirúrgico devidamente limpo, utiliza-se uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.
# V.	Após este procedimento deve-se escolher um ponto para a fixação de parafusos, de preferência na parte posterior da calota craniana, pois a camada óssea é mais espessa e suporta uma maior profundidade do parafuso. 
# Obs: Cuidar para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.
# Posicionar a agulha (devidamente preparada para o tamanho da cânula e que servirá de suporte para a fixação das cânulas) sobre o bregma (ver figura acima). Fazer os cálculos de posicionamento AnteroPosterior (AP), LateroLateral (LL) e DorsoVentral (DV). Os valores utilizados para os cálculos são os valores encontrados nas réguas a partir do posicionamento da agulha.
# E. G.: Hipocampo (CA1): Valores hipotéticos para fins de cálculo.
# AP: 6,42 cm 
# LL: 3,23 cm
# DV: 4,2 cm
# Isso significa que estes foram os valores encontrados em cada régua do estereotáxico e se subtrai ou soma a estes, os valores de cada estrutura ou núcleo. CA1: AP - 0,42 cm LL +/- 0,30 cm DV - 0,20 cm.
# AP: 6,42 cm – 0,42 = 6,00
# LL: 3,33 cm + 0,30 = 3,63 / - 0,30 = 3,03  (BILATERAL)
# DV: 4,20 cm – 0,20 = 4,00

# VI.	Após estes cálculos feitos é hora de localizar os pontos de inserção das cânulas-guia. Assim que estes pontos forem localizados é necessário fazer furos para a introdução das cânulas-guia. A localização destes pontos deve ser definida pelos valores encontrados nos cálculos AnteroPosterior (6,00) e LateroLateral (3,63 e 3,03). Deve-se escolher qual dos hemisférios vai ser colocada a primeira cânula, daí os dois valores para as medidas LL.
# VII.	Depois de posicionar a agulha, fazer um furo com a broca até alcançar as meninges. A não perfuração das meninges é o procedimento ideal, e para conseguir isso apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +- 450 de angulação.
# VIII.	Após ter atingido este objetivo, introduza a cânula-guia previamente confeccionada até o valor DorsoVentral (4,00) que foi calculado anteriormente.
# IX.	Logo após drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.
# X.	Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável (o ideal é que a mistura seja capaz de cobrir a parte desejada sem escorrer por todo o crânio). Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido. O tempo de secagem varia de acordo com a temperatura e umidade da sala. 
# XI.	O próximo passo é a fixação da outra cânula-guia. Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia previamente fixada não se movimente. Logo após, posicionar a agulha sobre o outro ponto de inserção da cânula-guia. Introduzir a cânula-guia até o valor DV (4,00) calculado previamente.
# XII.	Seguir novamente a descrição do item 9 e após fixar a cânula conforme item 10. De preferência espalhar o cimento sobre a maior área do crânio, sempre deixando um espaço entre o capacete e o início da área tecidual. Este cuidado previne de um futuro descolamento do capacete devido a entrada de sangue u outro líquido entre o capacete e o crânio.
# XIII.	Levantar bem devagar seguindo as instruções do item contida no item 11. Acomodar o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados. Assim que o animal despertar colocá-lo de volta a sua caixa-moradia.




























