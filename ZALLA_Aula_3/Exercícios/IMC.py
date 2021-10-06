
peso = float(input("Por favor, informe seu peso em kg: "))
altura = float(input("Por favor, informe sua altura em m: "))

imc = peso / (altura**2)

print("Muito abaixo do peso normal:",imc<17)
print("Abaixo do peso normal:",imc>=17 and imc<=18.5)
print("Peso dentro do normal:",imc>18.5 and imc<=25)
print("Acima do peso normal:",imc>25 and imc<=30)
print("Muito acima do peso normal:",imc>30)
