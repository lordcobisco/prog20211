peso = float(input('Qual seu peso?(kg), Exemplo: 50.0\n'))
altura = float(input('Qual sua altura?(m), Exemplo: 1.50\n'))
imc = peso / (altura**2)

print ('seu imc é de', imc)
print ('Muito abaixo do peso', imc < 17)
print ('Abaixo do peso normal', 17 < imc < 18.5)
print ('Peso dentro do normal', 18.5 < imc < 25.0)
print ('Acima do peso normal', 25 < imc < 30)
print ('Muito acima do peso', imc > 30)

print ('Obrigado!')