# Variáveis
anestésico1 = ('ketamina e xilazina')
anestésico2 = ('halonato')
HD = ('hemisfério direito')
HE = ('hemisfério esquerdo')

# Programa

Apresentação = ("Bem vindo ao sistema estereotáxico para cirurgias em pequenos animais")
print(Apresentação)
mensagem1 = int(input('Iniciar procedimento cirurgico? Digite 1 para sim e 0 para não '))
print(bool(mensagem1))

print('Estes são os anestésicos disponiveis:', anestésico1, 'ou', anestésico2)
input("tipo de anestésico selecionado: ")

mensagem2 = int(input('Aplicar anestésico? Digite 1 para sim e 0 para não '))
print(bool(mensagem2))

dosecorreta = int(input("O anestésico fez efeito? "))
if dosecorreta:
    print('posicione o animal no estereotáxico')
elif not dosecorreta:
    print('aumentar a dose de anestésico') 
else:
    print('O rato é resistente a este anestésico, aplique novamente com a outra droga')

mensagem3 = ('verifique se a cabeça do animal não tem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana.')
print(mensagem3)

mensagem4 = int(input('Iniciar limpeza do campo de trabalho? Digite 1 para sim e 0 para não  '))
print(bool(mensagem4))
mensagem5 = ('As etapas a seguir serão realizadas:')
print(mensagem5)
dicionário = {'retirar pelagem':(), 'retirar tecidos moles':('epiderme, derme, tecido conjuntivo'), 'limpar calota craniana':()}
for dicionário in dicionário:
    print(dicionário) 

mensagem6 = ('utilize uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.')
print(mensagem6)

mensagem7 = ("Escolha o local de posiciionamento dos parafusos, coloque a agulha sobre o bregma e preencha aqui com as coordenadas de CA1")
print(mensagem7)
input('AP =' ) # 6.00
input('LL =' ) # 3.63 e 3.03 BILATERAL
input('DV =' ) # 4.00

mensagem8 = int(input('Localizar pontos de insersão a partir das cordenadas para inserção de canula? Digite 1 para sim e 0 para não'))
print(bool(mensagem8))
mensagem9 = ('Em qual hemisfério inserir a primeira cânula?', HD, 'ou', HE)
print(mensagem9)
input('hemisfério selecionado: ')

mensagem10 = ('os procedimentos a seguir serão realizados:')
print(mensagem10)

listadeprocedimentos = ['perfurar crânio a 45º de inclinação',' introduzir cânula até DV 4.00', 'drenar sangue ou LCR do orifício criado']
print(listadeprocedimentos)

mensagem11 = ('Em seguida, misture acrílico polimerizante com solvente e faça um capacete abrangendo crânio, canula e parafuso')
print(mensagem11)
mensagem12 = ('levante o braço do estereotáxico lentamente e o posicione sobre o outro ponto de inserção da canula, introdui-la até DV 4,00')
print(mensagem12)

while HD or HE == True:
    print('Repetir procedimentos no outro hemisfério', listadeprocedimentos )
    break

mensagem13 = ('espalhe o cimento sobre a maior área do crânio, deixando espaço entre o capacete e o início da área tecidual')
print(mensagem13)
mensagem14 = ('Acomode o animal em caixa aquecida por lâmpada e sem outros animais, quando despertar colocá-lo de volta na sua caixa-moradia.')
print(mensagem14)

print('fim de procecimento')



