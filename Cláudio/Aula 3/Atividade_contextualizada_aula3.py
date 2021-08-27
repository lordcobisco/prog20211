print ('Olá, Usuári@!\n Este programa tem como objetivo automatizar seu procedimento de histologia utilizando o microscópio confocal.\n Seja bem-vind@.\n')

aberturadalente = 5 #1 a 10
iluminacao = 8 #1 a 10
resolucao = 9 #1 a 10
tipodecelula = 'neuronio' #hemacia, neuronio, espermatozoide, enterocitos, neutrofilos
filtrodeluz = 'azul' #azul, vermelho, verde
densidadedaimagem = 5 #1 a 10
desfoqueambiente = 0.5 #0.1 a 1.0
focoprincipal = 7 #1 a 10
tipodelente = 'media' #baixa, media, alta
corambiente = 'preto' #preto, branco

nome = input ('Qual o seu nome?\n')

aberturadalenteUsuario = int (input ('Qual a abertura da lente desejada? Entre 1 e 10\n'))
iluminacaoUsuario = int (input ('Qual a iluminação desejada? Entre 1 e 10\n'))
resolucaoUsuario = int (input ('Qual a resolução desejada? Entre 1 e 10\n'))
tipodecelulaUsuario = str (input ('Qual o tipo de célula desejado? hemacia, neuronio, espermatozoide, enterocitos ou neutrofilos\n'))
filtrodeluzUsuario = str (input ('Qual o tipo filtro de luz desejado? azul, vermelho ou verde\n'))
densidadedaimagemUsuario = int (input ('Qual o desfoque da imagem desejado? 1 a 10\n'))
desfoqueambienteUsuario = float (input ('Qual o desfoque do ambiente desejado? 0.1 a 1.0\n'))
focoprincipalUsuario = int (input ('Qual o tipo do foco principal desejado? 1 a 10\n'))
tipodelenteUsuario = str (input ('Qual o tipo de lente desejado? baixa, media ou alta\n'))
corambienteUsuario = str (input ('Qual a cor do ambiente desejado? preto ou branco\n'))

print ('Houve alteração na variável "abertura da lente" inserida?', aberturadalenteUsuario == aberturadalente)
print ('Houve alteração na variável "iluminação" inserida?', iluminacaoUsuario == iluminacao)
print ('Houve alteração na variável "resolução" inserida?', resolucaoUsuario == resolucao)
print ('Houve alteração na variável "tipo de célula" inserida?', tipodecelulaUsuario == tipodecelula)
print ('Houve alteração na variável "filtro de luz" inserida?', filtrodeluzUsuario == filtrodeluz)
print ('Houve alteração na variável "densidade da imagem" inserida?', densidadedaimagemUsuario == densidadedaimagem)
print ('Houve alteração na variável "desfoque ambiente" inserida?', desfoqueambienteUsuario == desfoqueambiente)
print ('Houve alteração na variável "foco principal inserida?', focoprincipalUsuario == focoprincipal)
print ('Houve alteração na variável "tipo de lente" inserida?', tipodelenteUsuario == tipodelente)
print ('Houve alteração na variável "cor ambiente" inserida?', corambienteUsuario == corambiente)

print ('Suas escolhas de configuração foram:')
print ('abertura da lente:', aberturadalenteUsuario)
print ('iluminação:', iluminacaoUsuario)
print ('resolução:', resolucaoUsuario)
print ('tipo de célula:', tipodecelulaUsuario)
print ('filtro de luz:', filtrodeluzUsuario)
print ('densidade da imagem:', densidadedaimagemUsuario)
print ('desfoque ambiente:', desfoqueambienteUsuario)
print ('foco principal:', focoprincipalUsuario)
print ('tipo de lente:', tipodelenteUsuario)
print ('cor ambiente:', corambienteUsuario)

print ('Muito bem, agora vamos calibrar o equipamento no sentido horizontal.\nPara isso é necessário que você aperte a primeira letra do seu nome 10 vezes')

calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])
calibrarhorizontal1 = input(nome[0])

print ('Muito bem, agora vamos calibrar o equipamento no sentido horizontal.\nPara isso é necessário que você aperte a última letra do seu nome 10 vezes')

calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])
calibrarhorizonta2 = input(nome[-1])


print ('a letra:', calibrarhorizontal1,'\ne a letra:', calibrarhorizonta2, '\nforam colocadas corretamente?', calibrarhorizontal1 == nome[0] and calibrarhorizonta2 == nome [-1])
print ('Obrigad@! a calibração do eixo horizontal foi realizada corretamente')

print ('Agora vamos calibrar o equipamento no sentido vertical.\nPara isso é necessário que você aperte a segunda letra do seu nome 10 vezes')

calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])
calibrarhorizontal3 = input(nome[1])

print ('Muito bem, agora vamos calibrar o equipamento no sentido vertical.\nPara isso é necessário que você aperte a penúltima letra do seu nome 10 vezes')

calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])
calibrarhorizonta4 = input(nome[-2])

print ('a letra:', calibrarhorizontal3,'\ne a letra:', calibrarhorizonta4, '\nforam colocadas corretamente?', calibrarhorizontal3 == nome[1] and calibrarhorizonta4 == nome [-2])
print ('Obrigad@!\nA calibração do eixo vertical foi realizada corretamente')

print ('Parabéns!\nO microscópio confocal está calibrado e configurado de acordo com seu objetivo.')