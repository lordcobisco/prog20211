#INSTITUTO INTERNACIONAL DE NEUROCIÊNCIAS EDMOND E LILY SAFRA, IIN-ELS
#INSTITUTO SANTOS DUMONT
#PROGRAMA DE PÓS-GRADUAÇÃO EM NEUROENGENHARIA
#COMPONENENTE CURRICULAR: FUND. DE PROGRAMAÇÃO E DESENVOLVIMENTO DE PROJETOS APLICADOS À NEUROENGENHARIA
#DOCENTE: PROF. Dr. ANDRÉ FELIPE OLIVEIRA DE AZEVEDO DANTAS
#DISCENTE: YAGO DANIEL SOUTO
#ESTA ATVIDADE TEM COMO OBJETIVO A ELABORAÇÃO DE UM PROGRAMA EM PYTHON QUE SIMULE DADOS DE ENTRADA E SAÍDA DE UM 
#MICROSCÓPIO CONFOCAL DE VARREDUDA A LASER.

# Variáveis necessárias para que o programa funcione corretamente;
# variáveis com valores padrão adequados;
# item (a) e (b)

ResolImagem = 1.7
FaixaIlumin = 0.5
TipoCelula = 4
Abertura = 2
Tipolente = 'media'
FiltroLuz = 'azul'
Densidade = 5
Desfoque = 1.2
CalibrHorizontal = 3.5
CalibrVertical = 4.5

# Mensagem de apresentação do programa para realizar uma interface com o usuário
#item (c)

print("Esse programa tem como objetivo receber dados para a configuração de um microscópio confocal. Seja muito bem-vindo, caro usuário!") 


#Solicitação de algumas informações necessárias para a configuração de um microscópio dessa natureza.
#item (d) e (e)
nome = input('Insira seu nome\n')
v1 = float(input('Insira a resolução da imagem necessária\n'))
print('Houve alteração na variável inserida?', v1 != ResolImagem)

v2 = float(input('Insira a faixa de iluminacao desejada\n'))
print('Houve alteração na variável inserida?', v2 != FaixaIlumin)

v3 = float(input('Insira o tipo de célula desejada\n'))
print('Houve alteração na variável inserida?', v3 != TipoCelula)

v4 = float(input('Insira a abertura desejada\n'))
print('Houve alteração na variável inserida?', v4 != Abertura)

v5 = float(input('Insira o tipo de lente desejada\n'))
print('Houve alteração na variável inserida?', v5 != Tipolente)

v6 = float(input('Insira o filtro de luz desejado\n'))
print('Houve alteração na variável inserida?', v6 != FiltroLuz)

v7 = input('Insira a densidade desejada\n')
print('Houve alteração na variável inserida?', v7 != Densidade)

v8 = input('Insira o desfoque desejado\n')
print('Houve alteração na variável inserida?', v8 != Desfoque)

v9 = float(input('Insira a calibração horizontal da imagem desejada\n'))
print('Houve alteração na variável inserida?', v9 != CalibrHorizontal)

v10 = float(input('Insira a calibração vertical da imagem desejada\n'))
print('Houve alteração na variável inserida?', v10 != CalibrVertical)

#Retorno ao usuário das informações que foram digitadas
#item (f)
print('As informações de configurações setadas pelo usuário são: \n', v1, 'ResolImagem\n',
                               v2, 'FaixaIlumin\n',
                               v3, 'TipoCelula\n',
                               v4, 'Abertura\n',
                               v5, 'Tipolente\n',
                               v6, 'FiltroLuz\n',
                               v7, 'Densidade\n',
                               v8, 'Desfoque\n',
                               v9, 'CalibrHorizontal\n',
                               v10,'CalibrVertical\n'     
     )

#Utilização de dois caracteres para a calibração do equipamento no sentido horizontal. Apertar a tecla correspondente 
# à primeira letra do seu nome 10x e à última letra do seu nome 10x.
#item (g)
print ('Calibração do equipamento no sentido horizontal.\n Para isso pressione a primeira letra correspondente ao seu nome 10x')

PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)
PrimeiraLetradoNome = input()
print (PrimeiraLetradoNome)

print ('Calibração do equipamento no sentido horizontal.\n Para isso pressione a última letra correspondente ao seu nome 10x')

ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)
ÚltimaLetradoNome = input()
print (ÚltimaLetradoNome)

#Apresentação na tela que a informação foi corretamente digitada e o caractere pressionado.
#item (h)

print ('A letra:', PrimeiraLetradoNome,'\ne a letra:', ÚltimaLetradoNome, '\n foram colocadas corretamente?', PrimeiraLetradoNome == nome[0] and ÚltimaLetradoNome == nome [-1])
print ('As letras foram corretamente inseridas e o seu equipamento foi calibrado horizontalmente com sucesso!')


#Utilização de dois caracteres para a calibração do equipamento no sentido vertical. Apertar a tecla correspondente 
# à segunda letra do seu nome 10x e à penúltima letra do seu nome 10x.
#item (i)
print ('Calibração do equipamento no sentido vertical.\n Para isso pressione a segunda letra correspondente ao seu nome 10x')

SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)
SegundaLetradoNome = input()
print (SegundaLetradoNome)

print ('Calibração do equipamento no sentido vertical.\n Para isso pressione a penúltima letra correspondente ao seu nome 10x')

PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)
PenúltimaLetradoNome = input()
print (PenúltimaLetradoNome)

#Apresentação na tela que a informação foi corretamente digitada e o caractere pressionado.
#item (j)

print ('A letra:', SegundaLetradoNome,'\ne a letra:', PenúltimaLetradoNome, '\n foram colocadas corretamente?', SegundaLetradoNome == nome[1] and PenúltimaLetradoNome == nome [-2])
print ('As letras foram corretamente inseridas e o seu equipamento foi calibrado verticalmente com sucesso!')

#Apresentação na tela que houve o término da calibração do sistema.

print ('A calibração do equipamento foi concluída com sucesso!')
