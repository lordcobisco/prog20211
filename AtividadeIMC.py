

altura = float(1.65)
peso = float(65)
imc = peso/(altura*altura)
print(imc)


altura = float(input('Entre com sua altura:'))  
peso = float(input('Entre com seu peso:'))  
imc = peso/(altura * altura)  
print('Seu índice de massa corporal é {:.2f}'.format(imc))  

imc = 23.88
if imc < 18:
    print('você está abaixo do peso')
if imc > 18 and imc < 25:
    print('você está no peso ideal')
if imc > 25:
    print('você está acima do peso')             