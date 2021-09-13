# Atividade contextualizada 03

print ('esse programa tem como Esse programa tem como objetivo receber dados e passar informações para o usuário e simular a interface do microscopio confocal')

#Variaves 
tipoDeCelula = 5 #variar de 1 a 10
iluminação = 6 #variar 1 a 15
foco = 500 # variar de 50 a 5000
tipoDeLuz = 'azul' #variar de Azul , vermelho ou verde
brilho = 70 #variar 0 a 100
contraste = 50 # variar de 0 a 100
resolucao = 1000 #variar 1000 a 5000
densidade =5 #variar 1 a 10
desfoque = 0.5 #variar 0.1 a 1.0 
lente = 'media' #variar baixo , media e alta

nome = input ('Qual é o seu nome?\n')

tipoDecelulaUsuario = int (input ('Qual o tipo de célula desejado? Entre 1 e 10 \n'))
iluminacaoUsuario = int (input ('Qual a iluminação desejada? Entre 1 e 15\n'))
focoUsuario = int (input ('Qual o tipo do foco  desejado? 50 a 5000\n'))
tipodeluzUsuario =  str (input ('Qual o tipo  de luz desejado? azul, vermelho ou verde\n'))
brilhoUsuario = int (input (' Qual tipo de brilho desejado? 0 e 100\n'))
contrasteUsuario = int (input ('Qual contraste desejado? 0 e 100\n'))
resolucaoUsuario =  int (input ('Qual a resolução desejada? entre 1000 e 5000\n'))
densidadeUsuario = int (input ('Qual o densidade desejada? 1 e 10\n'))
desfoqueUsuario = float (input ('Qual o desfoque  desejado? 0.1 a 1.0\n'))
lenteUsuario =  str (input ('Qual o tipo de lente desejado? baixa, media ou alta\n'))


print ('Houve alteração na variável "tipo de célula" inserida?', tipoDecelulaUsuario == tipoDeCelula)
print ('Houve alteração na variável "iluminação" inserida?', iluminacaoUsuario == iluminação)
print ('Houve alteração na variável "foco inserida?', focoUsuario == foco)
print ('Houve alteração na variável "tipo de luz" inserida?', tipodeluzUsuario == tipoDeLuz)
print ('Houve alteração na varial "brilho" inserida?',brilhoUsuario == brilho)
print ('Houve alteração na varial "contraste" inserida?', contrasteUsuario == contraste)
print ('Houve alteração na variável "resolução" inserida?', resolucaoUsuario == resolucao)
print ('Houve alteração na variável "densidade " inserida?', densidadeUsuario == densidade)
print ('Houve alteração na variável "desfoque" inserida?', desfoqueUsuario == desfoque)
print ('Houve alteração na variável " lente" inserida?', lenteUsuario == lente)


print ('tipoDecelula:', tipoDecelulaUsuario)
print ('iluminação:', iluminacaoUsuario)
print ('foco:', focoUsuario)
print ('brilho:', brilhoUsuario)
print ('contraste:', contrasteUsuario)
print ('resolução:', resolucaoUsuario)
print ('densidade :', densidadeUsuario)
print ('desfoque :', desfoqueUsuario)
print ('lente:', lenteUsuario)



print ('Muito bem, agora vamos calibrar o equipamento no sentido horizontal.\nPara isso é necessário que você aperte a primeira letra do seu nome 10 vezes')

calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()
calibrarhorizontal1 = input()

print ('Muito bem, ainda vamos calibrar o equipamento no sentido horizontal.\nPara isso é necessário que você aperte a última letra do seu nome 10 vezes')

calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()
calibrarhorizonta2 = input()


print ('a letra:', calibrarhorizontal1,'\ne a letra:', calibrarhorizonta2, '\nforam colocadas corretamente?', calibrarhorizontal1 == nome[0] and calibrarhorizonta2 == nome [-1])
print ('Obrigad@! a calibração do eixo horizontal foi realizada corretamente')

print ('Agora vamos calibrar o equipamento no sentido vertical.\nPara isso é necessário que você aperte a segunda letra do seu nome 10 vezes')

calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()
calibrarhorizontal3 = input()

print ('Muito bem, agora vamos calibrar o equipamento no sentido vertical.\nPara isso é necessário que você aperte a penúltima letra do seu nome 10 vezes')

calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()
calibrarhorizonta4 = input()

print ('a letra:', calibrarhorizontal3,'\ne a letra:', calibrarhorizonta4, '\nforam colocadas corretamente?', calibrarhorizontal3 == nome[1] and calibrarhorizonta4 == nome [-2])
print ('Obrigad@!\nA calibração do eixo vertical foi realizada corretamente')

print ('Parabéns!\nO microscópio confocal está calibrado e configurado de acordo com seu objetivo.')

