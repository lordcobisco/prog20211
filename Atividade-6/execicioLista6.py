pesoAnimal=0
procAnestesia=0
estereotaxico=0
animal=''
cmpLimpo=0
posAnimal=0
eSang=0
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
    print("Escolha do animal >>>\n")
    for k,v in animais.items():
        print("%s : Digite %d"%(v,k))
    opTipoAnimal=int(input("\nDigite a opção do Animal: "))
    animal = animais.get(opTipoAnimal)
    print("---------------------------------------------------\n")
    print("Escolha o Fármaco >>>\n")
    for k,v in farmacos.items():
        print("%s : Digite %d"%(v,k))
    opTipoFarmaco=int(input("\nDigite a opção do Fármaco: "))
    farmaco = farmacos.get(opTipoFarmaco)
    print("---------------------------------------------------\n")
    pesoAnimal=float(input("Insira o peso do animal: \n"))
    print("============= Parâmetros - Anestesia ============ \n")
    print('________________%s________________\n'%animal)
    print('___________%s______\n'%farmaco)

    if(opTipoFarmaco == 1):
        if(opTipoAnimal==1):
            ketaminaDosagem = 90*pesoAnimal # ketamina 90mg por kg
            xilazinhaDosagem = 10*pesoAnimal # 10mg a 13mg por kg 
            print("Dosagem de Ketamina em relação ao peso: %dmg "%ketaminaDosagem)
            print("Dosagem de Xilazinha em relação ao peso: %dmg "%xilazinhaDosagem)
            procAnestesia=1
        if(opTipoAnimal==2):
            ketaminaDosagem = 90*pesoAnimal # ketamina 90mg a 120mg por kg
            xilazinhaDosagem = 5*pesoAnimal # 5mg a 16mg por kg
            print("Dosagem de Ketamina em relação ao peso: %dmg "%ketaminaDosagem)
            print("Dosagem de Xilazinha em relação ao peso: %dmg "%xilazinhaDosagem)
            procAnestesia=1
    print()
    if(opTipoFarmaco==2):
        if(opTipoAnimal==1):
            ketaminaDosagem = 75*pesoAnimal #Ketamina 75mg por kg
            acepromazinaDosagem = 2.5*pesoAnimal #Acepromazina 2,5mg por kg
            print("Dosagem de Ketamina em relação ao peso: %dmg"%ketaminaDosagem)
            print("Dosagem de Acepromazina em relação ao peso: %dmg"%acepromazinaDosagem)
            procAnestesia=1
        if(opTipoAnimal==2):
            ketaminaDosagem = 90*pesoAnimal #Ketamina 90mg a 120mg por kg
            acepromazinaDosagem = 2.5*pesoAnimal #Acepromazina 2,5mg por kg
            print("Dosagem de Ketamina em relação ao peso: %dmg"%ketaminaDosagem)
            print("Dosagem de Acepromazina em relação ao peso: %dmg"%acepromazinaDosagem)
            procAnestesia=1
while(estereotaxico==0):
    print('====================================')
    efAnestOp = int(input("Anestésico fez efeito? 1 - Sim ou 0 - Não: \n"))
    if(efAnestOp == 1):
        print('--------------------------------------------')
        print('___Posicionamento do Animal___\n')
        while(posAnimal==0):
            procPosiOp=0
            print('|X| Posicione as barras que suportam o peso do animal no ouvido')
            print('|X| Verifique a angulação da cabeça do animal. Não deve haver diferenças.')
            procPosiOp = int(input('\nRealizou os procedimentos acima? 1 - Sim ou 0 - Não: '))
            if(procPosiOp ==1):
                print('--------------------------------------------')
                print('___Limpeza do Campo de Trabalho___\n')
                while(cmpLimpo == 0):
                    print('|X| Retire a pelagem que recobre a parte superior da calota craniana')
                    print('|X| Retire os tecidos moles até alcançar a parte óssea da caixa craniana')
                    print('|X| Limpe a calota craniana de qualquer resto de Pele com H2O 10 volumes')
                    limpezaOk = int(input('\nRealizou os procedimentos acima? 1- Sim ou 0 - Não: \n'))
                    if(limpezaOk==1):
                        print('--------------------------------------------')
                        print('___Evitando Sangramentos___\n')
                        while(eSang==0):
                            print('|X| Utilize uma pequena camada de poliacrilato em todo perímetro externo\n')
                            poliacri = int(input('Realizou os procedimentos acima? 1- Sim ou 0 - Não: \n'))
                            estereotaxico=1
                            posAnimal=1
                            cmpLimpo=1
                            fixParaf = 0
                            if(poliacri==1):
                                eSang=1
                                print('--------------------------------------------')
                                print('___Fixação de Parafusos___\n')
                                while(fixParaf == 0):
                                    print('|X| Escolha um ponto para fixação do Parafuso (Parte Posterior da Calota Craniana)')
                                    print('|*| Cuidado para não aprofundar muito. No máximo 3 voltas')
                                    parafuso = int(input('Realizou os procedimentos acima? 1- Sim ou 0 - Não: \n'))
                                    if(parafuso==1):
                                        print('--------------------------------------------')
                                        print('___Cálculos de Posicionamento da Agulha___\n')
                                        print('|X| Posicione a agulha sobre o Bregma.\n')
                                        ap = float(input('Informe o posicionamento AnteroPosterior: '))
                                        ll = float(input('Informe o posicionamento LateroLateral: '))
                                        dv = float(input('Informe o posicionamento DorsoVentral: '))
                                        calAp = ap-0.42
                                        calLla = ll+0.30
                                        calLlb = ll-0.30
                                        calDv = dv-0.20
                                        print('|#| Cálculo para AP: %f'%calAp)
                                        print('|#| Cálculo para LL lado A: %f / LL lado B: %f'%(calLla,calLlb))
                                        print('|#| Cálculo para DV: %f'%calDv)

                                        print('|X| ')
                                        fixParaf=1
                                    else:
                                        print('--------------------------------------------')
                                        print('___Fixação de Parafuso___\n')
                                        print('|!| Realize esse procedimento para prosseguir!')
                                        fixParaf=0
                            if(poliacri==0):
                                eSang=0
                                print('--------------------------------------------')
                                print('___Evitando Sangramentos___\n')
                                print('|!| Realize esse procedimento para prosseguir!')
                    if(limpezaOk==0):
                        print('--------------------------------------------')
                        print('___Limpeza do Campo de Trabalho___\n')
                        print('|!| Realize esse procedimento para prosseguir!')
            if(procPosiOp == 0):
                print('-----------------------------------------')
                print('___Posicionamento do Animal___\n')
                print('|!| Realize esse procedimento para prosseguir!')
                posAnimal=0
                estereotaxico=1
            
    if(efAnestOp == 0):
        estereotaxico=0
        print('\nAguarde mais um pouco ou aumente a dosagem do sedativo')

            
            


     

    
