peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)

if imc<17:
    print('IMC =', imc, ' é muito baixo')
if 17<=imc<18.5:
    print('IMC =', imc, ' é baixo')
if 18.5<=imc<25:
    print('IMC =', imc, ' é normal')
if 25<=imc<30:
    print('IMC =', imc, ' é alto')
if imc>=30:
    print('IMC =', imc, ' é muito alto')