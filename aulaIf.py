'''
Aula de if e else, mostrando em vários contextos 
como usar a estrutura
'''
# voceEntendeu = int(input('Você entendeu o conteúdo? Responda 0 para não entendeu e 1 para entendeu '))
 
# if voceEntendeu:
#     print("Legal, continue se esforçando")




# botao1Apertado = int(input("O rato apertou o botão 1?\n"))
# botao2Apertado = int(input("O rato apertou o botão 2?\n"))

# # Tabela verdade do e
# #  False and False = False
# #  True  and False = False
# #  False and True  = False
# #  True  and True  = True

# if botao1Apertado and (not botao2Apertado):
#     print("Foram adicionados 10mg de açucar")

# # Tabela verdade do ou
# #  False and False = False
# #  True  and False = True
# #  False and True  = True
# #  True  and True  = True

# if botao1Apertado or (not botao2Apertado):
#     print("ou,Foram adicionados 10mg de açucar")

# strPreguiçoso  = input("Você é uma pessoa preguiçosa\n")
# strinteligente = input("Você é uma pessoa inteligente\n")

# if(strPreguiçoso == 's' and strinteligente == 'n'):
#     print('Você é preguiçoso e não inteligente')

# voceEInteligente = int(input("Você é uma pessoa inteligente\n"))

# if voceEInteligente:
#     print('Você é inteligente\n')
#     print('Você é inteligente\n')
# else:
#     print('Você não é inteligente')
#     print('Você não é inteligente')


# numeroMenor = int(input('Digite um numero menor que 5:\n'))

# if numeroMenor < 5:
#     print('O numero digitado foi: ', numeroMenor)
# else:
#     print('Ops!\n Você digitou um numero maior ou igual a 5')
 

# print('Esse é o menu de seleção para o seu programa de processamento de dados\n')
# ação = int(input('Digite 1 para entrar na opção de inserção dos dados e 2 para processar os dados.\n'))

# if ação == 1:
#     print('Você selecionou a opção de upload!')
# elif ação == 2:
#     print('Você selecionou a opção de processamento!')
# else:
#     print('Você não selecionou uma opção válida!')



# botao1Apertado = int(input("O rato apertou o botão 1?\n"))
# botao2Apertado = int(input("O rato apertou o botão 2?\n"))

# if botao1Apertado and not botao2Apertado:
#     print('Foram adicionados 10mg de comida')
# elif not botao1Apertado and botao2Apertado:
#     print('Foram adicionados 20mg de comida')
# elif not botao1Apertado and not botao2Apertado:
#     print('Sem comida')
# else:
#     print('Os botões parecem estar com problema')


from math import pow 
Nome = input("Digite o seu nome\n")
peso   = float(input("Digite o seu peso\n"))
altura = float(input("Digite a sua altura\n"))
imc = peso/pow(altura,2)
imc = peso/(altura**2)
imc = peso/(altura*altura)

if imc<17:
    print('Abaixo do peso')
elif :
    print('Foram adicionados 20mg de comida')
elif :
    print('Sem comida')
else:
    print('Os botões parecem estar com problema')


print("fim de programa")