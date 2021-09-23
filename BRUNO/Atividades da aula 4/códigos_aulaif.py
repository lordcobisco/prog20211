'''
Aula de if e else, mostrando em vários contextos como usar a estrutura
'''
# VoceEntendeu = int(input("você entendeu o conteúdo? Responda 0 para não entendeu e 1 para entendeu"))

# if VoceEntendeu:
#    print("Legal, continue se esforçando")


botao1Apertado = int(input("O rato apertou o botão1?\n")) 
botao2Apertado = int(input("O rato apertou o botão2?\n")) 

# Tabela verdade do ou
# False and False = False
# True and False = False
# False and True = False
# True and True = False

# if botao1Apertado and (not botao2Apertado):
#    print("Foram adicionados 10mg de açucar")

# strPreguiçoso = input("Você é uma pessoa preguiçosa\n")
# strinteligente = input("Você é uma pessoa inteligente\n")

# if(strPreguiçoso == 's' and strinteligente == 'n'):
#    print('Você é preguiçoso e não inteligente')

# voceEInteligente = int(input("Você é uma pessoa inteligente\n"))

# if voceEInteligente:
#    print("Você é inteligente\n")
#    print("Você é inteligente\n")
# else:
#    print("Você não é  inteligente\n")
#    print("Você não é  inteligente\n")

# numeroMenor = int(input("Digite um número menor que 5:\n"))
# if numeroMenor < 5:
#    print('O número digitado foi: ', numeroMenor)
# else:
#    print('Ops!\n Você digitou um número maior ou igual a 5')
#print("fim de programa")

# print("Esse é menu de seleção para o seu programa de processamento de dados\n ")
# ação = int(input("Digite 1 para entrar na opção de inserção dos dados e 2 para processar os dados.\n"))

# if ação == 1:
#    print("Você selecionou a opção de upload")
# elif ação == 2:
#    print('você selecionou a opção de processamento!')
# else:
#    print('Você não selecionou uma opção válida!')


if botao1Apertado and not botao2Apertado:
   print('Foram adicionados 10mg de comida')
elif not botao1Apertado and botao2Apertado:
   print('Foram adicionados 20mg de comida')
elif not botao1Apertado and not botao2Apertado:
   print('Sem comida')
else:
   print('Os botões parecem estar com problema')
    
print('fim de programa')

