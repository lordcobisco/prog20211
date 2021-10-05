# Atividade contextualizada da aula 3
# criação de um programa para o microscópio confocal
# aluno: Pedro Sales

print('Bem vindo ao microscópio confocal, neste programa você irá inserir dados para que o microscópio capture e nos forneça imagens')


tipocelular = 4 # varia de 1 a 5
intensidadeluminosa = 80 # varia de 0 a 100
contraste = 5 # varia de 1 a 10
profundidade = 10 # varia de 0 a 100
eixox = 30 # varia de 0 a 100
eixoy = 70 # varia de 0 a 100
zoom = 200 # varia de 0 a 1000
intensidadeLaser = 90 # varia de 0 a 100
lente1 = 1 # varia de 1 a 5
lente2 = 3 # varia de 1 a 5

TipoCelular = input('Qual tipo celular você deseja focalizar? Escolha de 1 a 5\n')
print('Houve alteração da variável inserida?')
print(tipocelular != TipoCelular)

IntensidadeLuminosa = input('Qual é a intensidade de luz desejada? De 0 a 100\n')
print('Houve alteração da variável inserida?')
print(intensidadeluminosa != IntensidadeLuminosa)

Contraste = input('Escolha o contraste de 1 a 10\n')
print('Houve alteração da variável inserida?')
print(Contraste != contraste)

Profundidade = input('Selecione a profundidade do foco. Escolha de 0 a 100\n')
print('Houve alteração da variável inserida?')
print(Profundidade != profundidade)

EixoX = input('Escolha a posição do foco no eixo X, entre 0 a 100\n')
print('Houve alteração da variável inserida?')
print(EixoX != eixox)

EixoY = input('Escolha a posição do foco no eixo Y, entre 0 e 100\n')
print('Houve alteração da variável inserida?')
print(EixoY != eixoy)

Zoom = input('Escolha o zoom entre 0 e 1000\n')
print('Houve alteração da variável inserida?')
print(Zoom != zoom)

IntensidadeDoLaser = input('Escolha a intensidade do laser, entre 0 e 100\n')
print('Houve alteração da variável inserida?')
print(IntensidadeDoLaser != intensidadeLaser)

Lente1 = input('Escolha a posição da lente 1, entre 1 a 5\n')
print('Houve alteração da variável inserida?')
print(Lente1 != lente1)

Lente2 = input('Escolha a posição da lente 2, entre 1 e 5\n')
print('Houve alteração da variável inserida?')
print(Lente2 != lente2)

print('As configurações setadas pelo usuário são:\n')
print(TipoCelular)
print(IntensidadeLuminosa)
print(Contraste)
print(Profundidade)
print(EixoX)
print(EixoY)
print(Zoom)
print(IntensidadeDoLaser)
print(Lente1)
print(Lente2)

print('Agora vamos calibrar o equipamento, primeiro digite seu nome, depois você irá digitar a primeira e ultima letra do seu nome 10x, na sequência irá digitar a segunda e a penúltima letra do seu nome mais 10x')

NomeDeUsuario = input('Digite seu primeiro nome:')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')
input('Digite a primeira e última letras do seu nome\n')

input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')
input('Digite a segunda e penúltima letras do seu nome\n')

print('Aparelho calibrado e pronto para uso.')