#Exercício do cálculo do IMC
print("")
print("")
print("------------------------")
print("")
print("Calcule seu IMC")
peso = float(input("Informe o peso: \n"))
altura = float(input("Informe o altura: \n"))
imc = (peso / (altura*altura))
print("")
if(imc <17):
    print ('[!] Usuário muito abaixo do peso \n')
if ((imc >=17) and (imc <=18.5)):
    print ('[!] Usuário peso normal \n')
if((imc >=18.5)and(imc <=25)):
    print ('[!] Usuário peso normal \n')
if((imc >=25)and(imc <=30)):
    print ('[!] Usuário peso normal \n')
if(imc >30):
    print ('[*.*] Usuário muito acima do peso \n')