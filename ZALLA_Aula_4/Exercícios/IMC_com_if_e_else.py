peso = float(input("Por favor, informe seu peso em kg: "))
altura = float(input("Por favor, informe sua altura em m: "))

imc = peso / (altura**2)

if imc<17:
  print("Muito abaixo do peso normal, pois imc =",imc)
elif imc>=17 and imc<=18.5:
  print("Abaixo do peso normal, pois imc =",imc)
elif imc>18.5 and imc<=25:
  print("Peso dentro do normal, pois imc =",imc)
elif imc>25 and imc<=30:
  print("Acima do peso normal, pois imc =",imc)
else:
  print("Muito acima do peso normal, pois imc =",imc)
