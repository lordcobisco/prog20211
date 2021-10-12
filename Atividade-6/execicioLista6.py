pesoAnimal=0
procAnestesia=0
farmacos={
          1:"Ketamina e Xilazinha",
          2:"Ketamina e Acepromazinha"
         }
animais={
          1:"Ratos",
          2:"Camundongos"
        }
# print("==============Recursos Disponíveis=================")
# print("|X| Fármacos Disponíveis :: ")
# for y in farmacos.values():
#     print("Anestésico: %s ."%y)
# print("---------------------------------------------------")
# print("|X| Animais Disponíveis :: ")
# for y in animais.values():
#     print("Espécie: %s ."%y)
print("=============== Dosagem da Anestesia ================ \n")
while (procAnestesia == 0):
    print("Escolha do animal >>>")
    for k,v in animais.items():
        print("%s : Digite %d"%(v,k))
    opTipoAnimal=int(input("Digite a opção do Animal: "))
    print("---------------------------------------------------\n")
    print("Escolha o Fármaco >>>")
    for k,v in farmacos.items():
        print("%s : Digite %d"%(v,k))
    opTipoFarmaco=int(input("Digite a opção do Fármaco: "))
    print("---------------------------------------------------\n")
    pesoAnimal=float(input("insira o peso do animal: "))
    # print("Iniciar procedimento de Anestesia em Ratos \n")
    # resp = int(input("1: Ketamina e Xilazinha / 2: Halotano: "))
    if(opTipoFarmaco == 1):
        ketaminaDosagem = 90*pesoAnimal # ketamina 90mg por kg
        xilazinhaDosagem = 10*pesoAnimal # 10mg a 13mg por kg 
        print("Dosagem de Ketamina em relação ao peso: %dmg "%ketaminaDosagem)
        print("Dosagem de Xilazinha em relação ao peso: %dmg "%xilazinhaDosagem)
        procAnestesia=1
    if(opTipoFarmaco==2):
        ketaminaDosagem = 75*pesoAnimal #Ketamina 75mg por kg
        acepromazinaDosagem = 2.5*pesoAnimal #Acepromazina 2,5mg por kg
        print("Dosagem de Ketamina em relação ao peso: %dmg"%ketaminaDosagem)
        print("Dosagem de Acepromazina em relação ao peso: %dmg"%acepromazinaDosagem)
        procAnestesia=1

    
