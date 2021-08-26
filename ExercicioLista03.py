
#resImagemAlt
#resImagemLar

# Para públicação em periódicos Isto significa que é mais seguro
#coletar imagens para publicação com formatos de 1024 x 1024 ou até 2048 x 2048

resImagemAlt = 768 
resImagemLar = 1366
tipoCelulaAmostra = "osteoblastos"
#40 vezes
posicaoObjetivaCima = 40
posicaoObjetivaBaixo = 40
# Choose “speed” or “slow” buttons to switch between coarse and fine focus 
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

### 1 = cinza
#2 = blue e.g. DAPI
#3 = green e.g. FITC/SYTO 9
#4 = red e.g. TRITC/RHOD/Texas Red
#5 = to use as a ‘normal’ microscope with a halogen light source

# Para Lamparada Halogen use the knob
#to increase the light intensity. You can view your sample using the VIS button and filter set 5. 
labelFiltro = 1

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
print ("\n" * 5)
print('            INFORMAÇÕES SETADAS PELO USUÁRIO         ')
print(' ______________________________________________________________')
print('| Imagem Altura  |  Imagem Largura  |  Nome da Amostra   ')
print('|   %d                %d              %s                '%(resImagemAltIn,resImagemLarIn,tipoCelulaAmostraIn))
print('|________________|__________________|_____________________ ')
print('| Tipo Lâmpada   |  Ajuste do Foco  |  Filtro            ')
print('|   %s                %s               %d                '%(tipoLampadaIn,ajusteFocoIn,labelFiltroIn))
print('|________________|__________________|_____________________ ')
print('| Bloq Lâmpada   | Nome Pesquisador |                      ')
print('|   %d             %s                                     ' % (bloquearLampadaIn,nomePesquisador))
print('|________________|__________________|____________________________')
print('\n'*4)
print('            CALIBRAÇÃO DO EQUIPAMENTO         ')
print(' ______________________________________________________________')
print('\n'*2) 
print('[!] Para calibrar o equipamento você precisa digitar')
print('[!] a primeira letra do seu nome 10X e a ')
print('[!] última letra do seu nome 10X também')
print('\n'*2)
print('[!] Toque por 10X na tecla da primeira letra do seu primeiro nome')
letraIni =nomePesquisador[0] #pega a letra incial
comprimento = len(nomePesquisador) #comprimento do nome
print(comprimento)
letraFim = nomePesquisador[comprimento-1]
print(letraFim)
contador1=0
contador2=0

while (contador1 < 10):
       entradaLetraIni = (input('Digite a letra | %s | = ' % letraIni))
       print('Digitou correto ? ', entradaLetraIni == letraIni)
       contador1   = contador1 + int(entradaLetraIni == letraIni)
print('[!] Toque por 10X na tecla da última letra do seu primeiro nome')
while (contador2 < 10):
       entradaLetraFim = (input('Digite a letra | %s | = ' % letraFim))
       print('Digitou correto ? ', entradaLetraFim == letraFim)
       contador2   = contador2 + int(entradaLetraFim == letraFim)






# posicaoObjetivaCimaIn  = int (input("| posicaoObjetivaCima  | -*- Informe o valor que deseja \
# subir a objetiva: "))
# print ('Houve alteração na variável posicaoObjetivaCimaIn? ', posicaoObjetivaCima != posicaoObjetivaCimaIn)
# print("-----------------------------------------------------")
# posicaoObjetivaBaixoIn  = int (input("| posicaoObjetivaBaixo  | -*- Informe o valor que deseja \
# descer a objetiva: "))
# print ('Houve alteração na variável posicaoObjetivaBaixo? ', posicaoObjetivaBaixo != posicaoObjetivaBaixoIn)
# print("-----------------------------------------------------")
