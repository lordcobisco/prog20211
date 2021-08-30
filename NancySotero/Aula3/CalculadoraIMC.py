'''Programa para Calcular IMC
Aluna: Nancy Sotero
Semestre: 2021.2'''

peso = 73
altura = 1.75
IMC = peso/altura**2

print(IMC)
print("muito abaixo do peso", IMC<=17)
print("abaixo do peso", IMC>17 and IMC<=18.5)
print("peso normal", IMC>18.5 and IMC<=25)
print("acima do peso", IMC>25 and IMC<=30)
print("muito acima do peso", IMC>30)

#Atuallização - IMC com Input

peso = float(input("Digite seu peso"))
print("seu peso é", peso, "kg")
altura = float(input("Digite sua altura"))
print(altura, "m")
IMC = peso/altura**2
print("valor do seu IMC", IMC)

print(IMC)
print("muito abaixo do peso -", IMC<=17)
print("abaixo do peso -", IMC>17 and IMC<=18.5)
print("peso normal -", IMC>18.5 and IMC<=25)
print("acima do peso -", IMC>25 and IMC<=30)
print("muito acima do peso -", IMC>30)