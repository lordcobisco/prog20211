pesoAnimal=0
procAnestesia=0
estereotaxico=0
animal=''
cmpLimpo=0
posAnimal=0
eSang=0
listHistProc = []
farmacos={
          1:"Ketamina e Xilazinha",
          2:"Ketamina e Acepromazinha"
         }
animais=(
          "Ratos",
          "Camundongos"
        )
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
    for i in range(len(animais)):
        print("%s : Digite %d "%(animais[i],i))
    opTipoAnimal=int(input("\nDigite a opção do Animal: "))
    for i in range(len(animais)):
        if i == opTipoAnimal:
            animal = animais[i]
    listHistProc.append({'animal':animal})
    print("---------------------------------------------------\n")
    print("Escolha o Fármaco >>>\n")
    for k,v in farmacos.items():
        print("%s : Digite %d"%(v,k))
    opTipoFarmaco=int(input("\nDigite a opção do Fármaco: "))
    farmaco = farmacos.get(opTipoFarmaco)
    listHistProc.append({'farmaco':farmaco})
    print("---------------------------------------------------\n")
    pesoAnimal=float(input("Insira o peso do animal: \n"))
    listHistProc.append({'PesoAnimal':pesoAnimal})
    print("============= Parâmetros - Anestesia ============ \n")
    print('________________%s________________\n'%animal)
    print('___________%s______\n'%farmaco)

    if(opTipoFarmaco == 1):
        if(opTipoAnimal==0):
            ketaminaDosagem = 90*pesoAnimal # ketamina 90mg por kg
            xilazinhaDosagem = 10*pesoAnimal # 10mg a 13mg por kg 
            print("Dosagem de Ketamina em relação ao peso: %dmg "%ketaminaDosagem)
            print("Dosagem de Xilazinha em relação ao peso: %dmg "%xilazinhaDosagem)
            procAnestesia=1
            listHistProc.append({'DosagemKetamina':ketaminaDosagem,'DosagemXilazinha':xilazinhaDosagem})
        if(opTipoAnimal==1):
            ketaminaDosagem = 90*pesoAnimal # ketamina 90mg a 120mg por kg
            xilazinhaDosagem = 5*pesoAnimal # 5mg a 16mg por kg
            print("Dosagem de Ketamina em relação ao peso: %dmg "%ketaminaDosagem)
            print("Dosagem de Xilazinha em relação ao peso: %dmg "%xilazinhaDosagem)
            procAnestesia=1
            listHistProc.append({'DosagemKetamina':ketaminaDosagem,'DosagemXilazinha':xilazinhaDosagem})
    print()
    if(opTipoFarmaco==2):
        if(opTipoAnimal==0):
            ketaminaDosagem = 75*pesoAnimal #Ketamina 75mg por kg
            acepromazinaDosagem = 2.5*pesoAnimal #Acepromazina 2,5mg por kg
            print("Dosagem de Ketamina em relação ao peso: %dmg"%ketaminaDosagem)
            print("Dosagem de Acepromazina em relação ao peso: %dmg"%acepromazinaDosagem)
            procAnestesia=1
            listHistProc.append({'DosagemKetamina':ketaminaDosagem,'DosagemAcepromazina':acepromazinaDosagem})
        if(opTipoAnimal==1):
            ketaminaDosagem = 90*pesoAnimal #Ketamina 90mg a 120mg por kg
            acepromazinaDosagem = 2.5*pesoAnimal #Acepromazina 2,5mg por kg
            print("Dosagem de Ketamina em relação ao peso: %dmg"%ketaminaDosagem)
            print("Dosagem de Acepromazina em relação ao peso: %dmg"%acepromazinaDosagem)
            procAnestesia=1
            listHistProc.append({'DosagemKetamina':ketaminaDosagem,'DosagemAcepromazina':acepromazinaDosagem})
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
                listHistProc.append({'posicionamentoAnimal':procPosiOp})
                while(cmpLimpo == 0):
                    print('|X| Retire a pelagem que recobre a parte superior da calota craniana')
                    print('|X| Retire os tecidos moles até alcançar a parte óssea da caixa craniana')
                    print('|X| Limpe a calota craniana de qualquer resto de Pele com H2O 10 volumes')
                    limpezaOk = int(input('\nRealizou os procedimentos acima? 1- Sim ou 0 - Não: \n'))
                    if(limpezaOk==1):
                        print('--------------------------------------------')
                        print('___Evitando Sangramentos___\n')
                        listHistProc.append({'limprezaCampoT':limpezaOk})
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
                                listHistProc.append({'evitandoSangramento':poliacri})
                                while(fixParaf == 0):
                                    print('|X| Escolha um ponto para fixação do Parafuso (Parte Posterior da Calota Craniana)')
                                    print('|*| Cuidado para não aprofundar muito. No máximo 3 voltas')
                                    parafuso = int(input('Realizou os procedimentos acima? 1- Sim ou 0 - Não: \n'))
                                    if(parafuso==1):
                                        listHistProc.append({'FixaçãoParafusos':fixParaf})
                                        print('--------------------------------------------')
                                        print('___Cálculos de Posicionamento da Agulha___\n')
                                        print('|X| Posicione a agulha sobre o Bregma.\n')
                                        ap = float(input('Informe o posicionamento AnteroPosterior: '))
                                        ll = float(input('Informe o posicionamento LateroLateral: '))
                                        dv = float(input('Informe o posicionamento DorsoVentral: '))
                                        print('\n')
                                        calAp = ap-0.42
                                        calLla = ll+0.30
                                        calLlb = ll-0.30
                                        calDv = dv-0.20
                                        print('|#| Cálculo para AP: %.2f'%calAp)
                                        print('|#| Cálculo para LL lado A: %.2f / LL lado B: %.2f'%(calLla,calLlb))
                                        print('|#| Cálculo para DV: %.2f'%calDv)
                                        print('|X| ')                                    
                                        fixParaf=1
                                        canGuia=0
                                        listHistProc.append({'AP':calAp,'LLA':calLla,'LLB':calLlb,'DV':calDv})
                                        print('--------------------------------------------')
                                        print('___Inserção das Cânulas-Guia___\n')
                                        while(canGuia==0):
                                            print('|X| Faça a perfuração no AnteroPosterior a %.2f cm'%calAp)
                                            print('|X| Informe o lado do Hemisfério LateroLateral para inserção da 1ª Cânula\n')
                                            eHemi = int(input('|?| Hemisfério Direito - Digite 1 / Hemisfério Esquerdo 2: '))
                                            if(eHemi==1):
                                                print('\n|X| Faça a perfuração no LateroLareal Direito a %.2f cm'%calLla)
                                                print('|X| Com a broca, faça um furo até alcançar as meninges.')
                                                print('|!| Cuidado para não perfurar as meninges.')
                                                print('|X| Perfure o Crânio a +- 45° graus')
                                                canGuia=1
                                                listHistProc.append({'Hemisfério':eHemi})                                                
                                                perfuracao = int(input('\nRealizou os procedimentos acima? 1- Sim ou 0 - Não:'))
                                                print('___Inserção das Cânulas-Guia___\n')
                                                print('---------------------------------------------')
                                                if(perfuracao==1):
                                                    listHistProc.append({'CanulaInsert':perfuracao}) 
                                                    print('\n|X| Introduza a cânula-guia previamente confeccionada até %.2f.'%calDv)
                                                    print('|X| Drene o sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado.')
                                                    print('|X| Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável')
                                                    print('|X| Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso.')
                                                    print('|X| Deixe secar até ficar suficientemente rígido.')
                                                    print('---------------------------------------------------\n')
                                                    print('|X| O próximo passo é a fixação da outra cânula-guia.') 
                                                    print('|X| Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia não se mova')
                                                    print('|X| Introduza a cânula-guia previamente confeccionada até %.2f.'%calDv)
                                                    print('|X| Drene o sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado.')
                                                    print('|X| Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia não se mova')
                                                    print('\n|end| Acomodar o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados.')
                                                    canGuia=1
                                                if(perfuracao==0):
                                                    canGuia=0
                                                    print('___Inserção das Cânulas-Guia___\n')
                                                    print('|!| Realize esse procedimento para prosseguir!\n')
                                            elif (eHemi==2):
                                                print('|X| Faça a perfuração no LateroLareal Esquerdo a %.2f cm'%calLlb)
                                                print('|X| Com a broca, faça um furo até alcançar as meninges.')
                                                print('|!| Cuidado para não perfurar as meninges.')
                                                print('|X| Perfure o Crânio a +- 45° graus\n')
                                                listHistProc.append({'Hemisfério':eHemi})
                                                perfuracao1 = int(input('Realizou os procedimentos acima? 1- Sim ou 0 - Não: \n'))
                                                if(perfuracao1==1):
                                                    listHistProc.append({'Drenagem':perfuracao})
                                                    print('\n|X| Introduza a cânula-guia previamente confeccionada até %.2f.'%calDv)
                                                    print('|X| Drene o sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado.')
                                                    print('|X| Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável')
                                                    print('|X| Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso.')
                                                    print('|X| Deixe secar até ficar suficientemente rígido.')
                                                    print('---------------------------------------------------\n')
                                                    print('|X| O próximo passo é a fixação da outra cânula-guia.') 
                                                    print('|X| Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia não se mova')
                                                    print('|X| Introduza a cânula-guia previamente confeccionada até %.2f.'%calDv)
                                                    print('|X| Drene o sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado.')
                                                    print('|X| Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia não se mova')
                                                    print('\n|end| Acomodar o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados.')
                                                    print('')
                                                    canGuia=1
                                                if(perfuracao1==0):
                                                    canGuia=0
                                                    print('___Inserção das Cânulas-Guia___\n')
                                                    print('|!| Realize esse procedimento para prosseguir!\n')

                                            else:
                                                print('--------------------------------------------')
                                                print('___Inserção das Cânulas-Guia___\n')
                                                print('|!| Para prosseguir, informe o número correspondente ao hemisfério\n')
                                                canGuia=0      
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
        print('\nAguarde mais um pouco ou aumente a dosagem do Anestésico')
print('=============================================')
for i in range(len(listHistProc)):
    print('Histórico \n',listHistProc[i])
            
            


     

    
