#a.	Crie as variáveis necessárias para que o programa funcione corretamente.
#b.	Inicialize as variáveis com valores padrão adequados.


resolucaoDaImagemDesejada = "30x45"
tipoDeCelulaASerEscaneada = " basofila"
faixaDeIluminacaoNecessaria = "5"
intensidadeDosLasers = "4"
ganho = "30 x40"
offset = " 50"
formatoDaImagem = "retrato"
zoomFactor = "4x"
pixelSize = "44"
velocidadeDaVarredura = "3"


#c.	Crie uma pequena mensagem de apresentação do programa para realizar
#uma interface com o usuário. Ex.: “Esse programa tem como objetivo receber dados para ...”

print("Esse programa tem como objetivo receber dados para configuração de um microscópio confocal")
print("\n"*3) #print para salto de linha


#d. Solicite algumas informações necessárias para a configuração de um microscópio dessa
# natureza. Buscar pelo menos 10 itens para essas informações de entrada.
# Ex.: resolução da imagem desejada, tipo de célula a ser escaneada,
# faixa de iluminação necessária.

#e.	Para cada informação digitada, apresente na tela a seguinte mensagem:
# “Houve alteração na variável inserida? ”. Após a mensagem, apresentar verdadeiro ou falso
# com base no que foi digitado pelo usuário e o que estava armazenado na variável.
# Obs.: Não deve ser utilizado if aqui.

print("Digite a resolucao da imagem desejada")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != resolucaoDaImagemDesejada)
resolucaoDaImagemDesejada = entradaDigitada

print("Digite o tipo de célula a ser escaneada")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != tipoDeCelulaASerEscaneada)
tipoDeCelulaASerEscaneada = entradaDigitada

print("Digite a faixa de iluminação necessária")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != faixaDeIluminacaoNecessaria)
faixaDeIluminacaoNecessaria = entradaDigitada

print("Digite intensidade dos lasers")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != intensidadeDosLasers)
intensidadeDosLasers = faixaDeIluminacaoNecessaria

print("Digite o ganho desejado")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != ganho)
ganho = entradaDigitada

print("Digite o offset desejado")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != offset)
offset = entradaDigitada

print("Digite formato da imagem desejado")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != formatoDaImagem)
formatoDaImagem = entradaDigitada

print("Digite o zoom factor desejado")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != zoomFactor)
zoomFactor = entradaDigitada

print("Digite o pixel size desejado")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != pixelSize)
pixelSize = entradaDigitada

print("Digite a velocidade da varredura desejada")
entradaDigitada = input()
print("Houve alteração na variável inserida? ")
print(entradaDigitada != velocidadeDaVarredura)
velocidadeDaVarredura = entradaDigitada

#f.	Retorne ao usuário de forma organizada as informações que foram digitadas.
# Ex.: “As informações de configurações setadas pelo usuário são: ...”

print("") #print para salto de linha
print("") #print para salto de linha
print("") #print para salto de linha
print("") #print para salto de linha
print("") #print para salto de linha

print("As informações de configurações setadas pelo usuário são: ")
print("Resolução da imagem desejada: ",resolucaoDaImagemDesejada)
print("Tipo de Célula a ser escaneada: ",tipoDeCelulaASerEscaneada)
print("Faixa de iluminação necessária: ",faixaDeIluminacaoNecessaria)
print("Intensidade dos lasers: ",intensidadeDosLasers)
print("Ganho: ",ganho)
print("Offset: ",offset)
print("Formato da imagem: ",formatoDaImagem)
print("Zoom factor: ",zoomFactor)
print("Pìxel size: ",pixelSize)
print("Velocidade da varredura: ",velocidadeDaVarredura)



#g.	Após setada as configurações iniciais o usuário deve utilizar dois caracteres para a
# calibração do equipamento no sentido horizontal. Para isso, ele deve apertar a tecla
# correspondente à primeira letra do sejgghjdfdgu nome 10x e à última letra dso seu nome 10x.
#para calibração e continuar processo apertar 10x a tecla u e 10 vezes a tecla z
print("Calibração no sentido horizontal\n")

print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")

print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("digite a tecla z")
u = input()
print("\n")
print("Calibração no sentido vertical\n")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla a")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("digite a tecla u")
u = input()
print("\n")
print("término de calibração do microscópio confocal")
































#h.	Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
# foi corretamente digitada e mostrar o caractere pressionado.


#i.	Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento
# no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda letra do
# seu nome 10x e à penúltima letra do seu nome 10x.

#j.	Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
# foi corretamente digitada e mostrar o caractere pressionado.

#k.	Finalmente, o programa deverá apresentar na tela que houve o
#término da calibração do sistema.

#l.	Para verificar que o programa está funcionando corretamente, execute-o colocando um
# breakpoint na linha 15. Tire um print da tela mostrando a linha parada e as informações
# armazenadas nas variáveis até então.