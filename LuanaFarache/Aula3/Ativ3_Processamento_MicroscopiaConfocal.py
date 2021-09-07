# Mensagem inicial para interação com o usuário:
print ('Bem vindo ao processador de Microscopia Confocal MiCo_LuFa')
nome = input("Digite seu nome: ")
print ('Olá!',nome,', esse programa foi criado para receber os dados de microscopia confocal coletados em sua pesquisa')

# Iniciando o programa:
print('Para prosseguir, vamos precisar de algumas informações!')
inicio = input('Digite OK para prosseguir: ')
print('Para confirgurar o microscópio, preencha os campos a seguir:',
"Coloque apenas os valores absolutos, sem unidade de medida")

# Variáveis sobre a Microsocpia confocal necessárias para calibração do programa e seus respectivos valores de referência. 

TipoCelular = "Neurônio"
ResoluçãoLateral = 200
VelocidadeVarredura = 2
ÁreaVarrida = 10
ComprimentoOnda = 405
FaixaLuminosa = "violeta-azul"
PotênciaSaídaDiodo = 85
DiâmetroFeixe = "1,5 x 5,25"
CorrenteOperação = 3000
TemperaturaOperação = "0 a 40"

# As variáveis serão registradas pelo usuário e comparadas com os valores estabelecidos anteriormente.

TipoCelular = input("Qual tipo de célula será analisada? ") #Resposta modelo: Neurônio
print("Houve alteração na variável inserida?") # Checagem de alteração da variável
print(TipoCelular != TipoCelular) # Operação lógica para indicar ao usuário alteração no valor da variável

ResoluçãoLateral = float(input("Digite a resolução que você deseja para as imagens: ")) #Resposta modelo: 200nm
print("Houve alteração na variável inserida?")
print(ResoluçãoLateral != ResoluçãoLateral)

VelocidadeVarredura = float(input("Qual a velocidade de varredura almejada? ")) #Resposta modelo: 2mm²/s
print("Houve alteração na variável inserida?")
print(VelocidadeVarredura != VelocidadeVarredura)

ÁreaVarrida = float(input("Qual a área que deseja realizar varredura? ")) #Resposta modelo: Ex:10³ mm²
print("Houve alteração na variável inserida?")
print(ÁreaVarrida != ÁreaVarrida)

ComprimentoOnda = float(input("Qual será o comprimento de onda do Laser utilizado? ")) #Resposta modelo: 405 nm
print("Houve alteração na variável inserida?")
print(ComprimentoOnda != ComprimentoOnda)

FaixaLuminosa = input("Qual será a faixa espectral do laser? ") #Resposta modelo: Faixa do violeta-azul
print("Houve alteração na variável inserida?")
print(FaixaLuminosa != FaixaLuminosa)

PotênciaSaídaDiodo = float(input("Qual a potência de saída do Diodo laser utilizado? ")) #Resposta modelo: 85mW
print("Houve alteração na variável inserida?")
print(PotênciaSaídaDiodo != PotênciaSaídaDiodo)

DiâmetroFeixe = input("Qual o diâmetro do feixe do laser? ") #Resposta modelo: 1,5 x 5,25 mm
print("Houve alteração na variável inserida?")
print(DiâmetroFeixe != DiâmetroFeixe)

CorrenteOperação = float(input("Qual a corrente máxima de operação do diodo laser? ")) #Resposta modelo: 3000 mA
print("Houve alteração na variável inserida?")
print(CorrenteOperação != CorrenteOperação)

TemperaturaOperação = input("Qual a faixa de temperatura de funiconamento do diodo laser? ") #Resposta modelo: 0 a 40 Cº 
print("Houve alteração na variável inserida?")
print(TemperaturaOperação != TemperaturaOperação)

#Fim da etapa de registro dos valores das variáveis.

print("Obrigada por registrar as informações solicitadas",
"Você cadastrou os seguintes parâmetros:")

# Retorno do programa ao usuário sobre os valores registrados.
print(TipoCelular, ResoluçãoLateral,"nm", VelocidadeVarredura,"mm²/s", ÁreaVarrida,"³ mm²", ComprimentoOnda,"nm", 
FaixaLuminosa, PotênciaSaídaDiodo,"mW", DiâmetroFeixe,"nm", CorrenteOperação,"mA",TemperaturaOperação,"C°")

#Início da etapa de calibração:
Etapa2 = input("Deseja prosseguir? ")
print(Etapa2)

print("Agora precisamos calibrar o microscópio nas duas dimensões da imagem",
"A primeira dimensão será a LARGURA da imagem, no sentido horizontal",
"Para isso utilizaremos dois caracteres de entrada no programa!",
"O primero caracter será a primeira letra do seu nome",
"O segundo carcater será a última letra do seu nome",
"ATENÇÃO! Você deve digitar cada um dos caracteres 10 vezes, conforme solicitado pelo programa")

Largura1 = input("Digite a primeira letra do seu nome: ")
Largura1_2 = input("Digite a primeira letra do seu nome: ")
Largura1_3 = input("Digite a primeira letra do seu nome: ")
Largura1_4 = input("Digite a primeira letra do seu nome: ")
Largura1_5 = input("Digite a primeira letra do seu nome: ")
Largura1_6 = input("Digite a primeira letra do seu nome: ")
Largura1_7 = input("Digite a primeira letra do seu nome: ")
Largura1_8 = input("Digite a primeira letra do seu nome: ")
Largura1_9 = input("Digite a primeira letra do seu nome: ")
Largura1_10 = input("Digite a primeira letra do seu nome: ")

Largura2 = input("Digite a última letra do seu nome: ")
Largura2_2 = input("Digite a última letra do seu nome: ")
Largura2_3 = input("Digite a última letra do seu nome: ")
Largura2_4 = input("Digite a última letra do seu nome: ")
Largura2_5 = input("Digite a última letra do seu nome: ")
Largura2_6 = input("Digite a última letra do seu nome: ")
Largura2_7 = input("Digite a última letra do seu nome: ")
Largura2_8 = input("Digite a última letra do seu nome: ")
Largura2_9 = input("Digite a última letra do seu nome: ")
Largura2_10 = input("Digite a última letra do seu nome: ")

# Retorno so usuário sobre os caracteres inseridos por ele na estapa de calibração da largura.
print("As informações foram corretamente inseridas")
print(Largura1, Largura1_2, Largura1_3, Largura1_4, Largura1_5, Largura1_6, Largura1_7, Largura1_8, Largura1_9, Largura1_10)
print(Largura2, Largura2_2, Largura2_3, Largura2_4, Largura2_5, Largura2_6, Largura2_7, Largura2_8, Largura2_9, Largura2_10)

Etapa3 = input("Deseja prosseguir? ")
print(Etapa3)

print("Agora precisamos calibrar a ALTURA, segunda dimensão da imagem, no sentido vertical.",
"Para isso utilizaremos, novamente, dois caracteres de entrada no programa!",
"O primero caracter será a segunda letra do seu nome",
"O segundo carcater será a penúltima letra do seu nome",
"ATENÇÃO! Você deve digitar cada um dos caracteres 10 vezes, conforme solicitado pelo programa")

Altura1 = input("Digite a segunda letra do seu nome: ")
Altura1_2 = input("Digite a segunda letra do seu nome: ")
Altura1_3 = input("Digite a segunda letra do seu nome: ")
Altura1_4 = input("Digite a segunda letra do seu nome: ")
Altura1_5 = input("Digite a segunda letra do seu nome: ")
Altura1_6 = input("Digite a segunda letra do seu nome: ")
Altura1_7 = input("Digite a segunda letra do seu nome: ")
Altura1_8 = input("Digite a segunda letra do seu nome: ")
Altura1_9 = input("Digite a segunda letra do seu nome: ")
Altura1_10 = input("Digite a segunda letra do seu nome: ")

Altura2 = input("Digite a penúltima letra do seu nome: ")
Altura2_2 = input("Digite a penúltima letra do seu nome: ")
Altura2_3 = input("Digite a penúltima letra do seu nome: ")
Altura2_4 = input("Digite a penúltima letra do seu nome: ")
Altura2_5 = input("Digite a penúltima letra do seu nome: ")
Altura2_6 = input("Digite a penúltima letra do seu nome: ")
Altura2_7 = input("Digite a penúltima letra do seu nome: ")
Altura2_8 = input("Digite a penúltima letra do seu nome: ")
Altura2_9 = input("Digite a penúltima letra do seu nome: ")
Altura2_10 = input("Digite a penúltima letra do seu nome: ")

print("As informações foram corretamente inseridas")

# Retorno so usuário sobre os caracteres inseridos por ele na estapa de calibração da largura.
print(Altura1, Altura1_2, Altura1_3, Altura1_4, Altura1_5, Altura1_6, Altura1_7, Altura1_8, Altura1_9, Altura1_10)
print(Altura2, Altura2_2, Altura2_3, Altura2_4, Altura2_5, Altura2_6, Altura2_7, Altura2_8, Altura2_9, Altura2_10)

print("Obrigada! Você concluiu com êxito a calibração do equipamento")

# Fim do programa!
