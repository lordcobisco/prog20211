logicValue = int(input("Você é uma pessoa inteligente? "))

if logicValue:
  print("Não deixe o trabalho para depois!")

print("Fim do programa.")

########################

botao1Apertado = int(input("O rato apertou o botão 1? "))
botao2Apertado = int(input("O rato apertou o botão 2? "))

if (botao1Apertado and not botao2Apertado):
  print("Foram adicionados 10 mg de comida.")
if (not botao1Apertado and botao2Apertado):
  print("Foram adicionados 20 mg de comida.")
if (not botao1Apertado and not botao2Apertado):
  print("Nenhuma comida foi adicionada.")
if (botao2Apertado and botao2Apertado):
  print("Foram adicionados 40 mg de comida.")

print("Fim do programa.")

########################

logicLazy = int(input("Você é uma pessoa preguiçosa? "))
logicInteligent = int(input("Você é uma pessoa inteligente? "))

if (logicLazy and not logicInteligent):
  print("Você é preguiçosa mas não é inteligente.")
if (not logicLazy and not logicInteligent):
  print("Você não é preguiçoso nem inteligente.")
if (logicLazy and logicInteligent):
  print("Você é preguiçoso e inteligente.")
if (not logicLazy and logicInteligent):
  print("Você não é preguiçoso mas é inteligente.")

print("Fim do programa.")

#######################

strLazy = input("Você é uma pessoa preguiçosa? ")
strInteligent = input("Você é uma pessoa inteligente? ")

if (strLazy == "s" and strInteligent == "n"):
  print("Você é preguiçosa mas não é inteligente.")
if (strLazy == "n" and strInteligent == "n"):
  print("Você não é preguiçoso nem inteligente.")
if (strLazy == "s" and strInteligent == "s"):
  print("Você é preguiçoso e inteligente.")
if (strLazy == "n" and strInteligent == "s"):
  print("Você não é preguiçoso mas é inteligente.")

print("Fim do programa.")
