peso = float(input('Digite seu peso em quilogramas \n'))
print('Peso informado: ', peso, 'Kg')
altura = float(input('Digite sua altura em metros \n'))
print('Altura informada: ', altura, 'cm')

import math
imc = (peso/altura**2)
print('Seu IMC é:\n', imc)

print(imc <= 17, "Seu IMC indica que você está abaixo do peso ideal")
print(imc > 17 and imc <=18, "Seu IMC indica que você está no peso normal")
print(imc > 18.5 and imc <= 25, "Seu IMC indica que você está no peso normal")
print(imc > 25 and imc <=30, "Seu IMC indica que você está abaixo do peso normal")
print(imc > 30, "Seu IMC indica que você está acima do peso normal")
