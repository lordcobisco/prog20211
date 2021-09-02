# Mensagem apresentada para usuario

print("Olá, caro usuári@! Este programa tem como objetivo simular a interface do Microscroscópio")

# Variáveis necessárias para que o programa funcione

resol = 1.5 
iluminação = 0.3
celula = 3 
abertura = 2
calibracaoHorizontal = 4.5
calibracaoVertical = 6.5
lente = 'media'
filtroLuz = 'azul'
densidadeImg = 4
desfoque = 1.5 

#Solicitar informações necessárias para calibrar o equipamento
nome = input('Insira seu nome\n')
q1 = float(input('Digite o valor de resolucao desejado\n'))
print('Houve alteracao na variavel inserida?', q1 != resol)

q3 = float(input('Digite o valor de iluminacao desejado\n'))
print('Houve alteracao na variavel inserida?', q3 != iluminação)

q5 = float(input('Digite o valor para celula desejada\n'))
print('Houve alteracao na variavel inserida?', q5 != celula)

q7 = float(input('Digite o valor para parametro de abertura desejado\n'))
print('Houve alteracao na variavel inserida?', q7 != abertura)

q9 = float(input('Digite o valor para calibracao horizontal desejado\n'))
print('Houve alteracao na variavel inserida?', q9 != calibracaoHorizontal)

q11 = float(input('Digite o valor para calibracao vertical desejado\n'))
print('Houve alteracao na variavel inserida?', q11 != calibracaoVertical)

q13 = input('Digite qual espessura (baixa, media ou alta) da lente desejada\n')
print('Houve alteracao na variavel inserida?', q13 != lente)

q15 = input('Digite qual filtro de luz desejado\n')
print('Houve alteracao na variavel inserida?', q15 != filtroLuz)

q17 = float(input('Digite o valor para densidade de imagem desejado\n'))
print('Houve alteracao na variavel inserida?', q17 != densidadeImg)

q19 = float(input('Digite o grau de desfoque da imagem \n'))
print('Houve alteracao na variavel inserida?', q19 != desfoque)

#Retorno ao usuário das informações digitadas

print('Seus parametros sao: \n', q1, 'resolucao\n',
                               q3,  'iluminacao\n',
                               q5, 'celula\n',
                               q7, 'abertura\n',
                               q9, 'calibracao horizontal\n',
                               q11, 'calibracao vertical\n',
                               q13, 'espessura da lente\n',
                               q15, 'filtro de luz\n',
                               q17, 'densidade da imagem\n',
                               q19, 'grau de desfoque\n'     
     )


print ('Vamos calibrar o equipamento no sentido horizontal.\n Para isso pressione a primeira letra do seu nome 10 vezes')

calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)
calibrarhorizontal1 = input()
print (calibrarhorizontal1)

print ('Para calibrar o equipamento no sentido horizontal.\nPara isso é necessário que você aperte a última letra do seu nome 10 vezes')

calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)
calibrarhorizontal2 = input()
print (calibrarhorizontal2)

print ('a letra:', calibrarhorizontal1,'\ne a letra:', calibrarhorizontal2, '\nforam colocadas corretamente?', calibrarhorizontal1 == nome[0] and calibrarhorizontal2 == nome [-1])
print ('A calibracao foi realizada com sucesso!')
