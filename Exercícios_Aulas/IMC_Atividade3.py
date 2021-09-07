# Este programa irá calcular o seu IMC

Nome = input("Digite seu nome: ")
Peso = float(input("Digite o seu peso: "))
Altura = float(input("Digite sua altura: "))
IMC = Peso/Altura**2

print(Nome, Peso, Altura)
print(Nome, ", seu IMC é: ", IMC)