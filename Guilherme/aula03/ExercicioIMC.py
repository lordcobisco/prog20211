
print('Indice de Massa Coporal (IMC)')
altura = float(input('por favor digite aqui a sua altura:'))
peso = float(input('por favor digite aqui o seu peso'))
print('sua altura è %sm e o seu peso é %skg'%(altura , peso))
imc = peso / (altura **2)
print('Seu IMC é: %s'%(imc))
print('')
print('Muito abaixo do peso:',imc < 17)
print ('')
print ('Abaixo do peso normal:', 17 <= imc <18.5)
print('')
print('dentro do peso normal:', 18.5 <= imc <25)
print('')
print('Acima do peso normal:', 25<= imc <30)
print('')
print('Muito acima do peso:', imc >30)
