'''Programa para utilização de Microscópio Confocal
Aluna: Nancy Sotero
Semestre: 2021.2'''

print("Caro usuário, este programa tem como objetivo a inserção de informações necessárias para o bom funcionamento do Microscópio Confocal do Laboratório de Microscopia do IIN-ELS. Preencha os seguintes campos:")

resolucaoDeImagem = 1024 
tipoDeCelula = 5    
iluminacao = 500   
ampliacaoZoom = 40 
bateria = 110  
tempoDeUso = 30
lentes = 8  
calibracaoHorizontal = 1.7 
calibracaoVertical = 2.4  
intensidadeLaser = 25 

Imagem = float(input("Digite a resolução da imagem: "))
print("Houve alteração na variável inserida?", Imagem != resolucaoDeImagem)

Celula = float(input("Digite o tipo da célula: "))
print("Houve alteração na variável inserida?", Celula != tipoDeCelula)

Iluminacao = float(input("Digite a faixa de iluminação desejada: "))
print("Houve alteração na variável inserida?", Iluminacao != iluminacao)

Zoom = float(input("Digite a ampliação da imagem: "))
print("Houve alteração na variável inserida?", Zoom != ampliacaoZoom)

Bateria = float(input("Digite o tipo de bateria: "))
print("Houve alteração na variável inserida?", Bateria != bateria)

Tempo = float(input('Digite o tempo de uso do microscópio: '))
print("Houve alteração na variável inserida?", Tempo != tempoDeUso)

Lentes = float(input('Digite a quantidade de lentes: '))
print("Houve alteração na variável inserida?", Lentes != lentes)

Horizontal = float(input('Digite o valor de calibração horizontal em pixels: '))
print("Houve alteração na variável inserida?", Horizontal != calibracaoHorizontal)

Vertical = float(input('Digite o valor de calibração vertical em pixels: '))
print("Houve alteração na variável inserida?", Vertical != calibracaoVertical)

Laser = float(input('Digite a intensidade do laser: '))
print("Houve alteração na variável inserida?", Laser != intensidadeLaser)

print("Caro usuário, foram escolhidas as seguintes configurações:")

print("Resolução da Imagem:", Imagem, 'pixel')
print("Tipo de Célula: célula tipo ", Celula)
print("Faixa de Iluminação:", Iluminacao, 'amp')
print("Ampliação da Imagem:", Zoom, 'x')
print("Tipo de bateria:", Bateria, 'volts')
print("Tempo de Uso:", Tempo, 'minutos')
print("Quantidade de Lentes:", Lentes)
print("Valor de calibração horizontal:", Horizontal, 'pixels')
print("Valor de calibração vertical em pixels:", Vertical, 'pixels')
print("Intensidade do laser:", Laser)

Verificacao = 0
while(Verificacao == 0):

    print("Caro usuário, para realizar a Calibração Horizontal do microscópio, digite 10x a primeira letra do seu nome")
    Horizontal1 = input()
    Horizontal2 = input()
    Horizontal3 = input()
    Horizontal4 = input()
    Horizontal5 = input()
    Horizontal6 = input()
    Horizontal7 = input()
    Horizontal8 = input()
    Horizontal9 = input()
    Horizontal10 = input()

    Contador = 0 
    if(Horizontal1 == Horizontal2): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal3): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal4): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal5): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal6): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal7): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal8): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal9): 
        Contador = Contador + 1
    if(Horizontal1 == Horizontal10): 
        Contador = Contador + 1

    print("Agora, digite 10x a última letra do seu nome")
    Horizontal1a = input()
    Horizontal2a = input()
    Horizontal3a = input()
    Horizontal4a = input()
    Horizontal5a = input()
    Horizontal6a = input()
    Horizontal7a = input()
    Horizontal8a = input()
    Horizontal9a = input()
    Horizontal10a = input()

    if(Horizontal1a == Horizontal2a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal3a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal4a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal5a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal6a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal7a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal8a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal9a): 
        Contador = Contador + 1
    if(Horizontal1a == Horizontal10a): 
        Contador = Contador + 1

    print ('Você digitou a letra:', Horizontal1,'e:', Horizontal1a, 'corretamente?', Contador==18) 
    if(Contador==18):
        Verificacao = 1 
        print('Calibração Horizontal Concluída')
    else:
        print('Erro - Repetir Calibração Horizontal')

Verificacao = 0
while(Verificacao == 0):

    print("Caro usuário, para realizar a Calibração Vertical do microscópio, digite 10x a segunda letra do seu nome")
    Vertical1 = input()
    Vertical2 = input()
    Vertical3 = input()
    Vertical4 = input()
    Vertical5 = input()
    Vertical6 = input()
    Vertical7 = input()
    Vertical8 = input()
    Vertical9 = input()
    Vertical10 = input()

    Contador = 100
    if(Vertical1 == Vertical2): 
        Contador = Contador + 1
    if(Vertical1 == Vertical3): 
        Contador = Contador + 1
    if(Vertical1 == Vertical4): 
        Contador = Contador + 1
    if(Vertical1 == Vertical5): 
        Contador = Contador + 1
    if(Vertical1 == Vertical6): 
        Contador = Contador + 1
    if(Vertical1 == Vertical7): 
        Contador = Contador + 1
    if(Vertical1 == Vertical8): 
        Contador = Contador + 1
    if(Vertical1 == Vertical9): 
        Contador = Contador + 1
    if(Vertical1 == Vertical10):
        Contador = Contador + 1

    print("Agora, digite 10x a penúltima letra do seu nome")
    Vertical1a = input()
    Vertical2a = input()
    Vertical3a = input()
    Vertical4a = input()
    Vertical5a = input()
    Vertical6a = input()
    Vertical7a = input()
    Vertical8a = input()
    Vertical9a = input()
    Vertical10a = input()

    if(Vertical1a == Vertical2a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical3a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical4a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical5a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical6a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical7a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical8a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical9a): 
        Contador = Contador + 1
    if(Vertical1a == Vertical10a): 
        Contador = Contador + 1

    print ('Você digitou a letra:', Vertical1,'e:', Vertical1a, 'corretamente?', Contador==118)
    if(Contador==118):
        Verificacao = 1
        print('Calibração Vertical Concluída')
    else:
        print('Erro - Repetir Calibração Vertical')


print('Calibração Finalizada! Você pode iniciar o uso do Microscópio Confocal.')

#fim
