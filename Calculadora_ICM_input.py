nome = input("Digite seu nome: ")

peso = float(input("Digite o seu peso: "))

altura = float(input("Digite sua altura: "))

ICM = peso/(altura**2)
print(ICM)
print(ICM < 18.5, "ICM abaixo da média, procure um especialista!"); print(18.5 < ICM < 25, "Parabéns! ICM normal!"); print(ICM > 25, "Alerta! ICM acima da média, procure um especialista.")