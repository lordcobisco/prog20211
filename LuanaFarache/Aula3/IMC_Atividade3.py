# Este programa irá calcular o seu IMC

Nome = input("Digite seu nome: ")
Peso = float(input("Digite o seu peso: "))
Altura = float(input("Digite sua altura: "))
IMC = Peso/Altura**2

print(Nome, Peso, Altura)
print(Nome, ", seu IMC é: ", IMC)

# Atualização do programa usando estruturas de decisão:

Nome = input("Digite seu nome: \n")
Peso = float(input("Digite o seu peso: \n"))
Altura = float(input("Digite sua altura: \n"))
IMC = Peso/(Altura**2)

print("Seu IMC é = ", IMC)

if IMC < 17:
    print("Você está muito abaixo do peso estimado!\n")
elif IMC > 17 and IMC < 18.5:
    print("Você está abaixo do peso!\n")
elif IMC > 18.5 and IMC < 25:
    print("Você esta dentro do peso esperado!\n")
elif IMC > 25 and IMC < 30:
    print("Você esta acima do peso estimado!\n")
elif IMC > 30:
    print("Você esta muito acima do peso estimado!\n")
else:
    print("Algo deu errado! Reinicie o programa!")