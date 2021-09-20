# Os comandos, em Python, são executados de cima para baixo e da esquerda para a direita.
# print("Vamos programar em Python")

# VariavelLogica = bool(int(input("Você esta acompanhando? Digite 0 para não e 1 para sim ")))

#if VariavelLogica:
 #   print("Vai dar certo!")

#print("Fim do programa")

#if 3>2:
    #print("Luana")

'''
Para o comando do IF é necessário que haja:
IF + (condição declarada. Ex: 3<2) + : (os 2 pontos já chama a indentação 
automaticamente) + comando indentado.
Se a indentação e os : não estiverem presentes vai haver erro sintático, em alguns casos também pode ser 
semântico, e não irá ocorrer a compilação e interpretação adequada do código. 
'''

# Tabela verdade para operações lógicas com AND:
# False and False = False
# True  and False = False
# False and True = False
# True  and True = True

# Tabela verdade para operações lógicas com OR:
# False or False = False
# True  or False = True
# False or True = True
# True  or True = True



#Botão1Apertado = int(input("O rato pressionou o botão 1? \n"))
#Botão2Apertado = int(input("O rato pressionou o botão 2? \n"))

#if Botão1Apertado and (not Botão2Apertado):
    #print("Foram ofertados 10mg de glicose")

#if Botão1Apertado or (not Botão2Apertado):
    #print("Foram ofertados 5mg de glicose")

#StrPreguiçoso = int(input("Você é uma pessoa preguiçosa? \n" ))
#StrInteligente = int(input("Você é uma pessoa inteligente? \n" ))

#if(StrPreguiçoso == 's' and StrInteligente == 'n'):
    #print("Você é preguiçosos e não inteligente!")
#print("Fim de programa!")

#if(StrInteligente == "sim"):
    #print("Muito bem, continue assim!")
#else:
    #print("Vá estudar!")

#NumeroMenor = int(input("Digite um número menor que 5: \n"))

#if NumeroMenor < 5:
    #print("O número digitado foi:" , NumeroMenor)
#else:
    #print("Ops! \n")
    #print("Você digitou um número maior ou igual a 5")

#print("Fim do programa!")

print('Esse é o menu de seleção para o seu programa de processamento de dados\n')
Ação = int(input('Digite 1 para acessar a opção de Inserção de dados e 2 para processar os dados\n'))
 
if Ação == 1:
    print("Você selecionou a opção de upload")
elif Ação == 2:
    print("Você selecionou a opção de processamento de dados")
else:
    print("Você não selecionou uma opção válida!")
    print("Fim do programa!")


# Teste da função "IF... ELIF... ELSE":
NumeroMenor = int(input("Digite um número: \n"))

if NumeroMenor < 10:
    print("O número digitado é menor que 10! \n")
elif NumeroMenor > 10:
    print("O número digitado é maior que 10! \n")
elif NumeroMenor == 10:
    print("O número digitado foi 10!")
else:
    print("Ops! \n")
    print("Você digitou um número muito diferente de 10")

print("Fim do programa!")

Botão1Apertado = int(input("O rato pressionou o botão 1? \n"))
Botão2Apertado = int(input("O rato pressionou o botão 2? \n"))

if Botão1Apertado and not Botão2Apertado:
    print("Foram ofertados 10mg de comida!\n")
elif not Botão1Apertado and Botão2Apertado:
    print("Foram ofertados 20mg de comida!\n")
elif not Botão1Apertado and not Botão2Apertado:
    print("Não foi adicionado comida!\n")
else:
    print("Algo deu errado! Os botões parecem estar com problema.")

