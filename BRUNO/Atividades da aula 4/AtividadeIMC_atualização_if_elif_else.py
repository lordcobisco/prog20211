# Nome = (input("Digite o seu nome\n")) 
# Peso = float(input("Digite o seu peso\n")) 
# Altura = float(input("Digite a sua altura\n"))
# imc = Peso/(Altura*Altura)

# print("Muito abaixo do peso quando imc menor que 17")
# print(imc<17.0)

# print("Abaixo do peso normal quando imc entre 17 e 18,5")
# print(imc>17.0,imc<18.5)

# print("Peso dentro do normal quando imc entre 18,5 e 25,0")
# print(imc>18.5, imc<25)

# print("Acima do peso normal quando imc entre 25,0 e 30,0")
# print(imc>25.0, imc<30.0)

# print("Muito acima do peso quando imc acima de 30")
# print(imc>30.0)

# print("Muito abaixo do peso quando imc menor que 17")
# Resposta1 = input("Seu imc está nessa faixa? Digite 0 para falso ou 1 para veradeiro: ")

# print("Abaixo do peso normal quando imc entre 17 e 18,5")
# resposta2 =input("Seu imc está nessa faixa? Digite 0 para falso ou 1 para veradeiro: ")

# print("Peso dentro do normal quando imc entre 18,5 e 25")
# resposta3 = input("Seu imc está nessa faixa? Digite 0 para falso ou 1 para veradeiro: ")

# print("Acima do peso normal quando imc entre 25,0")
# resposta4 = input("Seu imc está nessa faixa? Digite 0 para falso ou 1 para veradeiro: ")

# print("Muito acima do peso quando imc acima de 30")
# resposta5 = input("Seu imc está nessa faixa? Digite 0 para falso ou 1 para veradeiro: ")

Nome = (input("Digite o seu nome\n")) 
Peso = float(input("Digite o seu peso\n")) 
Altura = float(input("Digite a sua altura\n"))
imc = Peso/(Altura*Altura)

if imc <17:
    print("Abaixo do peso")
elif imc>17.0 and imc<18.5:
    print("Abaixo do peso normal")
elif imc>18.5 and imc<25:
    print("Peso dentro do normal")
elif imc>25.0 and imc<30.0:
    print("Acima do peso normal")
elif imc>30.0:
    print("imc>30.0")
else:
    print("Resposta inválida")


