
nome = input('Digite seu nome: \n')
peso = float(input('Digite seu peso: \n'))
altura = float(input('Digite sua altura em metros \n'))

print(nome, 'seu peso eh: \n', peso)

import math
imc = (peso/altura**2)

if imc <=17:
    print("Seu IMC indica que você está abaixo do peso ideal")
elif imc > 17 and imc <=18:
    print( "Seu IMC indica que você está no peso normal")
elif imc > 18.5 and imc <= 25:
    print("Seu IMC indica que você está no peso normal")
elif imc > 25 and imc <=30:
    print("Seu IMC indica que você está abaixo do peso normal")
else:
    print(imc > 30, "Seu IMC indica que você está acima do peso normal")