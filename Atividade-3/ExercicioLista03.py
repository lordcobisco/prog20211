
#Kelisson Lima
# Para públicação em periódicos Isto significa que é mais seguro
#coletar imagens para publicação com formatos de 1024 x 1024 ou até 2048 x 2048

resImagemAlt = 768 
resImagemLar = 1366
tipoCelulaAmostra = "osteoblastos"
# Escolha “speed” or “slow” que irá ajustar o foco fino ou grosso 
ajusteFoco = "speed"
#Argon ou Halogen
#Argon é um laser que mostra a fluorecencia da amostra
#Halogen é uma lâmpada de mércurio que não mostra a fluorecencia da amostra
tipoLampada = "argon"
laserArgonLigado = False
lampadaHalogenLigado = False
#Bloqueador de lâmpada de mercúrio, pois a longa exposição à luz pode 
# branquear suas amostras e mudar o filtro para 1
bloquearLampada = False
#1 = cinza
#2 = blue 
#3 = green 
#4 = red 
#5 = para usar como microscopio como ‘normal’  com a fonte de luz halogen 
labelFiltro = 1
# para aumentar a intensidade da luz .
luzIntensidade = 5

print('\n'*2)
print('Esse programa tem como objetivo receber dados para o Software LSM usado em um microscópio confocal')
print('\n' * 2)
nomePesquisador = str (input("| nomePesquisador | Informe o primeiro nome do pesquisador: ").lower())
print("-----------------------------------------------------")
resImagemAltIn = int (input("| resImagemAlt | Informe a altura da imagem: "))
infImagemAlt = (resImagemAlt  != resImagemAltIn)
print ('Houve alteração na variável resImagemAlt? ', infImagemAlt)
print("-----------------------------------------------------")
resImagemLarIn = int (input("| resImagemLar | Informe a largura da imagem: "))
infImagemLar = (resImagemLar  != resImagemLarIn)
print ('Houve alteração na variável resImagemLar? ', infImagemLar)
print("-----------------------------------------------------")
tipoCelulaAmostraIn = input("| tipoCelulaAmostra | Informe  o nome da celula a ser \
scaneada: ")
infCelulaAmostra = (tipoCelulaAmostra  != tipoCelulaAmostraIn)
print ('Houve alteração na variável de tipoCelulaAmostra ? ', infCelulaAmostra)
print("-----------------------------------------------------")
tipoLampadaIn  =  str (input("| tipoLampada | -*- [Argon/Halogen] Informe a Lâmpada: "))
infTipoLampada = (tipoLampada != (tipoLampadaIn).lower())
print ('Houve alteração na variável tipoLampada? ', infTipoLampada)
print("-----------------------------------------------------")
ajusteFocoIn  =  (input("| ajusteFoco  | [Speed/Slow] Informe o valor: "))
infAjusteFoco = (ajusteFoco != (ajusteFocoIn).lower())
print ('Houve alteração na variável ajusteFoco? ', infAjusteFoco)
print("-----------------------------------------------------")
labelFiltroIn = int (input("| labelFiltro | filtro [Blue] = 2 : filtro [Green] = 3 : filtro [Red] = 4 \
: filtro [Normal] = 5  ¨|¨ Informe: \n"))
infLabelFiltro = (labelFiltro != labelFiltroIn)
print ('Houve alteração na variável labelFiltro? ', infLabelFiltro)
print("-----------------------------------------------------")
bloquearLampadaIn = int (input("| bloquearLampada | -*- [Sim-1/Não-0] Informe em números: "))
infBloquearLampada = (bloquearLampada != bloquearLampadaIn)
print ('Houve alteração na variável labelFiltro? ', infBloquearLampada)
print("-----------------------------------------------------")
luzIntensidadeIn = int (input("| luzIntensidade | [1/100] Informe em números: "))
influzIntensidade = (luzIntensidade != luzIntensidadeIn)
print ('Houve alteração na variável labelFiltro? ', influzIntensidade)
print("-----------------------------------------------------")
print ("\n" * 5)
print('            INFORMAÇÕES SETADAS PELO USUÁRIO         ')
print(' ______________________________________________________________')
print('| Imagem Altura  |  Imagem Largura  |  Nome da Amostra   ')
print('|   %d                %d              %s                '%(resImagemAltIn,resImagemLarIn,tipoCelulaAmostraIn))
print('|________________|__________________|_____________________ ')
print('| Tipo Lâmpada   |  Ajuste do Foco  |  Filtro            ')
print('|   %s                %s               %d                '%(tipoLampadaIn,ajusteFocoIn,labelFiltroIn))
print('|________________|__________________|_____________________ ')
print('| Bloq Lâmpada   | Nome Pesquisador | Luz Intensidade      ')
print('|   %d             %s                 %d                    ' % (bloquearLampadaIn,nomePesquisador,luzIntensidadeIn))
print('|________________|__________________|____________________________')
print('\n'*4)
print('            CALIBRAÇÃO DO EQUIPAMENTO         ')
print(' ______________________________________________________________')
print('\n'*2) 
print('[!] Para calibrar o equipamento você precisa executar os seguintes passos:')
print('[ SENTIDO HORIZONTAL ]')
print('[!] a PRIMEIRA letra do seu nome 10X e a ')
print('[!] ÚLTIMA letra do seu nome 10X também')
print('\n'*2)
print('[ SENTIDO VERTICAL ]')
print('[!] a SEGUNDA letra do seu nome 10X e a ')
print('[!] PENÚLTIMA letra do seu nome 10X também')
print('\n'*2)
letraIni =nomePesquisador[0] #pega a letra incial
comprimento = len(nomePesquisador) #comprimento do nome
letraFim = nomePesquisador[comprimento-1]
print(letraFim)
contador=0
letraSeg = nomePesquisador[1]
letraPen = nomePesquisador[comprimento-2]


print('[HORIZONTAL] Toque por 10X na tecla da primeira letra do seu primeiro nome')
while (contador < 10):
       entradaLetraIni = (input('Digite a letra | %s | = ' % letraIni))
       print('Digitou correto ? ', entradaLetraIni == letraIni)
       print('O que você digitou? ', entradaLetraIni)
       contador   = contador + int(entradaLetraIni == letraIni)
print('[HORIZONTAL] Toque por 10X na tecla da última letra do seu primeiro nome')
contador = 0
while (contador < 10):
       entradaLetraFim = (input('Digite a letra | %s | = ' % letraFim))
       print('Digitou correto ? ', entradaLetraFim == letraFim)
       print('O que você digitou? ', entradaLetraFim)
       contador   = contador + int(entradaLetraFim == letraFim)
print('[VERTICAL] Toque por 10X na tecla da segunda letra do seu primeiro nome')
contador = 0
while (contador < 10):
       entradaLetraIni = (input('Digite a letra | %s | = ' % letraSeg))
       print('Digitou correto ? ', entradaLetraIni == letraSeg)
       print('O que você digitou? ', entradaLetraIni)
       contador   = contador + int(entradaLetraIni == letraSeg)
print('[VERTICAL] Toque por 10X na tecla da penúltima letra do seu primeiro nome')
contador=0
while (contador < 10):
       entradaLetraFim = (input('Digite a letra | %s | = ' % letraPen))
       print('Digitou correto ? ', entradaLetraFim == letraPen)
       print('O que você digitou? ', entradaLetraFim)
       contador   = contador + int(entradaLetraFim == letraPen)

print('[<|>] ** EQUIPAMENTO CALIBRADO **')





























































































































































#Kelisson Lima