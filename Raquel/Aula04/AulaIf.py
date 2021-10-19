vocêEndendeu = int(input("você endendeu o conteúdo? Responda 0 para não e 1 para endendeu"))


if vocêEndendeu:
    print("legal continue se esforçando")
    

print("depois do if")  

botao1Apertado = int(input("o rato apertou o botão 1?"))
botao2Apertado = int(input("o rato apertou o botão2?"))

# Tabela verdade do e
# False and False = False
# True and True = True
# false and False = False
# True and True = True

if botao1Apertado and (not botao2Apertado):
    print("foram adicionados 10mg de açucar")

strPreguiçoso = input("você é uma pessoa preguiçosa")


voceEInteligente = int (input("você é uma pessoa inteligente\n"))
if voceEInteligente:
    print('você é inteligente\n')
else:
    print('você não é inteligente')    



numeroMenor = int(input('Digite um numero menor que 5:\n'))
if numeroMenor <5:
    print('o numero digitado foi:',numeroMenor)


print('esse é o menu de seleçãpo para seu progrma de processamneto de dados \n')

ação = int(input('Digite 1 para entrar na opção de inserção dos dados e 2 para processar dados' ))






print("fim de programa")