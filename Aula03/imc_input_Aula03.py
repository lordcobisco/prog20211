peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)

print("IMC muito baixo:")
print(imc<17)

print("\nIMC muito baixo:")
print(17<=imc<18.5)

print("\nIMC normal:")
print(18.5<=imc<25)

print("\nIMC alto:")
print(25<=imc<30)

print("\nIMC muito alto:")
print(imc>=17)
