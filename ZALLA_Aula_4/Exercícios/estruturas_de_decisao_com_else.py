logicValue = int(input("Você é uma pessoa inteligente? "))

if logicValue:
  print("Você é inteligente!")
else:
  print("Você não é inteligente.")

print("Fim do programa.")

#######################

numeroMenor = int(input("Digite um número menor que 10: "))

if numeroMenor > 10:
  print("Ops!")
  print("O número digitado é maior que 10!")
else:
  print("O número digitado foi:", numeroMenor)

print("Fim do programa.")

######################

acao = int(input("Digite '1' para sim e '2' para não: "))

if (acao == 1):
  print("Você disse que sim!")
elif (acao == 2):
  print("Você disse que não!")
else:
  print("O número digitado não é '1' nem '2'.")

print("Fim do programa.")

######################

botao1Apertado = int(input("O rato apertou o botão 1? "))
botao2Apertado = int(input("O rato apertou o botão 2? "))

if (botao1Apertado and not botao2Apertado):
  print("Foram adicionados 10 mg de comida.")
elif (not botao1Apertado and botao2Apertado):
  print("Foram adicionados 20 mg de comida.")
elif (not botao1Apertado and not botao2Apertado):
  print("Nenhuma comida foi adicionada.")
else:
  print("Foram adicionados 40 mg de comida.")

print("Fim do programa.")
