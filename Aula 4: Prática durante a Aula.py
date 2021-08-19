#Play list de Inteligência artificial: https://www.youtube.com/watch?v=_PTDRLtWTxA&list=PLeGe5_wof0_bGLaVFT_de6NUFIKALslVf.

#Precisamos nos preocupar com a indentação. Apertamos o TAB.
#TAB costuma ser 4 espaços. isso é sintaxe. è algo obrigatóriod e ser aprendido

#só um IF vai executar um trecho se o código for VERDADEIRO

from typing import Match


if 3>2: #como o resultado é verdadeiro, o programa vai executar.
    print ("Thiago")
    print ("Thiago")


if 3<2: #como o resultado é falso, o programa não vai executar.
    print ("Thiago")
    print ("Thiago")

#if uma condição/pergunta lógica...
#não faz sentido definir sempre que algo vai ser verdadeiro ou falso. a decisão precisa ser tomada com base em algo que pode mudar.
#nesse caso, vai precisar de um input, por exemplo;
#andré sempre gosta de colcoar o nome da varipavl or extenso, poque quando for fazer manutenção, tem como ler o codio de uma forma mais fácil

voceEntendeu = (int(input('você entendeu o conteúdo? Responda 0 para não entendeu e 1 para entendeu'))) 
if voceEntendeu:
    print ("Legal, continue se esforçando")

botao1Apertado = int(input("o rato apertou o botão 1?\n"))
botao2Apertado = int(input("o rato apertou o botão 2?\n"))

if botao1Apertado and (not botao2Apertado):
    print ("foram adicionados 10mg de açucar")

if botao1Apertado or (not botao2Apertado):
    print ("foram adicionados 10mg de açucar")

#Tabelaverdade do AND
# False and False =
# False and False =
# False and False =
# False and False =

strPreguiçoso = input ("você é uma pessoa preguiçosa\n?")
strinteligente = input("você é uma pessoa inteligente\n?")

if strPreguiçoso == 's' and strinteligente == 'n':
    print ('você é preguiçoso e não inteligente')
strPreguiçoso

if strinteligente == 's' and strPreguiçoso == 'n':
    print ('você é inteligente e não preguiçoso')
strinteligente

print("fim de programa")



voceEInteligente = int(input("você é inteligente"))

if voceEInteligente:
    print ('você não é inteligente\n')
else:
    print ('você não é inteligente\n')

print ('fim de programa') #não deu certo. tentar corrigir depois.


numeroMenor = int(input('digite um numero menor que 5:\n'))
if numeroMenor:
    print ('o numero digitado foi: ', numeroMenor)
else:
    print("Ops!\n você digitou um numero maior ou igual a 5")
print ("fim de programa")



# A diferença do ELIF para o ELSE é que o ELSE não precisa de condição para ser executado.

from math import pow
Nome = input("digite o seu nome\n")
Peso = float(input("digite o seu peso\n"))
Altura = float(input("digite a sua altura\n"))
IMC = Peso/pow(Altura,2)
