var1_1 = "Cel_ nervosas"
var1_2 = "cel_ musculares"
var1_3 = "cel_ epiteliais"
var2_1 = "corantes"
var2_2 = "agentes fluorecentes"
var2_3 = "anticorpos"
var3_1 = "Argônio"
var3_2 = "Hélio/Neônio"
var4_1 = "objetiva1"
var4_2 = "objetiva2"
var5_1 = "x10"
var5_2 = "x25"
var5_3 = "x50"
var5_4 = "x100"
var6_1 = "50%"
var6_2 = "75%"
var6_3 = "100%"
var7_1 = "5um"
var7_2 = "10um"
var7_3 = "15um"
var8_1 = "512x512"
var8_2 = "1024x1024"
var9_1 = "JPG"
var9_2 = "PNG"
var9_3 = "PDF"
var10_1 = "meucomputador"
var10_2 = "gitdesktop"
var11_1 = "true"
var11_2 = "false"

Apresentacao = ("Esse programa tem como objetivo receber dados para o funcionamento do microscópio confocal")
print(Apresentacao)
Mensagem1 = ("preencha adequadamente com os parametros desejados para programar o aparelho para o seu uso")
print(Mensagem1)

print("Estes são os tipos de célula: ", var1_1, var1_2, " ou ", var1_3, " = ")
informacao1 = input("tipo de célula a ser escaneada: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estes são os tipos de tratamento das células: ", var2_1, var2_2, " ou ", var2_3, " = ")
Informacao2 = input("tipo de tratamento das células: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estes são os tipos de laser que podem ser usados: ", var3_1, " ou ", var3_2, " = ")
Informacao3 = input("tipo de laser a ser usado: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estes são os tipos de lentes a serem usadas: ", var4_1, " ou ", var4_2, " = ")
informacao4 = input("tipo de lente a ser usada: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estas são as resoluções de imagem do aparelho: ", var5_1, var5_2, var5_3, " ou ", var5_4, " = ")
informacao5 = input("resolução da imagem desejada: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estas são as faixas de iluminação do aparelho: ", var6_1, var6_2, " ou ", var6_3, " = ")
informacao6 = input("faixa de iluminação necessária: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estes são os diametros do foco de luz do aparelho: ", var7_1, var7_2, " ou ", var7_3, " = ")
informacao7 = input("diametro do ponto iluminado: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estas são as resoluções das imagens ao ser capturadas: ", var8_1, " ou ", var8_2, " = ")
informacao8 = input("resolução da imagem a ser capturada: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("Estes são os formatos em que as imagens podem ser salvas: ", var9_1, var9_2, " ou ", var9_3, " = ")
informacao9 = input("formato da imagem salva: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

print("estes são os locais para armazenamento das imagens: ", var10_1, " ou ", var10_2, " = ")
informacao10 = input("local de armazenamento das imagem: ")
mensagem2 = int(input("Houve alteração na variável inserida? Digite 0 para verdadeiro ou 1 para falso: "))
print(bool(mensagem2))

mensagem3 = ("As informações de configurações setadas pelo usuário são: ", informacao1,Informacao2,Informacao3,informacao4,informacao5,informacao6,informacao7,informacao8,informacao9,informacao10)
print(mensagem3)

ajustehorizontal = input("primeira e última letra do seu nome 10X")
print("aparelho corretamente calibrado ", ajustehorizontal)

ajustevertical = input("segunda e penúltima letra do seu nome 10X")
print("aparelho corretamente calibrado ", ajustevertical)

print("Término da calibração do sistema")


