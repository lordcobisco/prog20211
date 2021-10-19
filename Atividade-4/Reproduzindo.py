'''
Reproduzindo os exemplos práticos
'''
individuoInteligente = int(input("Você é uma pessoa inteligente\n"))

if individuoInteligente:
    print('Você é inteligente\n')
else:
    print('Você não é inteligente')

numeroMaior = int(input('Digite um numero maior que 5:\n'))

if numeroMenor > 5:
    print('O numero digitado foi: ', numeroMaior)
else:
    print('Opa, o número é menor que 5')
 

botaoApertado1 = int(input("O rato apertou o botão 1, digite 1 para sim ou 2 para não?"))
botaoApertado2 = int(input("O rato apertou o botão 2, digite 1 para sim ou 2 para não? "))

if botaoApertado1 and not botaoApertado2:
    print('Foram adicionados 10mg de comida')
