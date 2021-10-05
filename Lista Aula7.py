import time

# DISPOSITIVO 1
def DISPOSITIVO_um(rA, gA, bA):
    return rA, gA, bA
    

listaRed = list()    #vermelho
listaGreen = list()  #verde
listaBlue = list()   #azul

contador_zero=0
while contador_zero<32:
    pass
    
    fimdoexperimento_um = 0 
    while not fimdoexperimento_um:
        fimdoexperimento_um = int(input(" Sair do experimento? Digite 1 pra continuar \n"))
       
           
    else: 
        
        
        rA = int(input("Dispositivo 1. Digite valores para R: \n"))
        listaRed.append(rA)
        if rA<5: print("Led vermelho, intensidade baixa \n")
        if rA==5: print("Led vermelho, intensidade média \n")
        if rA>5: print("Led vermelho, intensidade alta \n")
        x = int(input("Por quanto tempo o Led vai ficar aceso?"))
        time.sleep(x)

    fimdoexperimento_dois = 0 
    while not fimdoexperimento_dois:
        fimdoexperimento_dois = int(input("Sair do experimento? Digite 1 pra continuar\n"))
        
    else: 
        gA = int(input("Dispositivo 1. Digite valores para G: \n"))
        listaGreen.append(gA)
    if gA<5: print("Led verde, intensidade baixa \n")
    if gA==5: print("Led verde, intensidade média \n")
    if gA>5: print("Led verde, intensidade alta \n")
    y = int(input("Por quanto tempo o Led vai ficar aceso?"))
    time.sleep(y)

    fimdoexperimento_tres = 0 
    while not fimdoexperimento_tres:
        fimdoexperimento_tres = int(input("Você deseja sair do experimento? Digite 1 pra continuar: \n"))
        

    else: 

        bA = int(input("Dispositivo 1. Digite valores para B: \n"))
        listaBlue.append(bA)
    if bA<5: print("Led azul, intensidade baixa \n")
    if bA==5: print("Led azul, intensidade média \n")
    if bA>5: print("Led azul, intensidade alta \n")
    z = int(input("Por quanto tempo o Led vai ficar aceso?"))
    time.sleep(z)

    print(DISPOSITIVO_um(rA,gA,bA))
    
    contador_zero = contador_zero + 1


        
else:
    pass
    print("Pronto \n")

print(" Lista de R: \n")
print(listaRed)
print(" Lista de G: \n")
print(listaGreen)
print(" Lista de B: \n")
print(listaBlue)




# DISPOSITIVO 2

def DISPOSITIVO_dois(rB, gB, bB,):
    return rB, gB, bB

listaRedB = list()
listaGreenB = list()
listaBlueB = list()
    
contador_um=0
while contador_um<32:
    pass

    fimdoexperimento_quatro = 0 
    while not fimdoexperimento_quatro:
        fimdoexperimento_quatro = int(input(" Você deseja sair do experimento? Digite 1 pra continuar \n"))
        
         
    else: 
    
        rB = int(input("Dispositivo 2. Digite valores para R: \n"))
        listaRed.append(rB)
    if rB<5: print("Led vermelho, intensidade baixa \n")
    if rB==5: print("Led vermelho, intensidade média \n")
    if rB>5: print("Led vermelho, intensidade alta \n")
    w = int(input("Por quanto tempo o Led vai ficar aceso?"))
    time.sleep(w)

    fimdoexperimento_cinco = 0 
    while not fimdoexperimento_cinco:
        fimdoexperimento_cinco = int(input("Você deseja sair do experimento? Digite 1 pra continuar\n"))
        
    else: 
        gB = int(input("Dispositivo 1. Digite valores para G: \n"))
        listaGreen.append(gB)

    if gB<5: print("Led verde, intensidade baixa \n")
    if gB==5: print("Led verde, intensidade média \n")
    if gB>5: print("Led verde, intensidade alta \n")
    t = int(input("Por quanto tempo o Led vai ficar aceso?"))
    time.sleep(t)

    fimdoexperimento_seis = 0 
    while not fimdoexperimento_seis:
        fimdoexperimento_seis = int(input("Você deseja sair do experimento? Digite 1 pra continuar\n"))
        

    else: 

        bB = int(input("Dispositivo 1. Digite valores para B: \n"))
        listaBlue.append(bB)
    if bB<5: print(" Led azul, intensidade baixa \n")
    if bB==5: print(" Led azul, intensidade média \n")
    if bB>5: print(" Led azul, intensidade alta \n")
    m = int(input("Por quanto tempo o Led vai ficar aceso?"))
    time.sleep(m)

    print(DISPOSITIVO_dois(rB,gB,bB))

    contador_um = contador_um + 1
    

else:
    pass
    print("\n Pronto \n")

print("\n Lista de R: \n")
print(listaRedB)
print("\n Lista de G: \n")
print(listaGreenB)
print("\n Lista de B: \n")
print(listaBlueB)

# DISPOSITIVO 1:

listaExperimento = list()
lista_tempo_inicio = list()
listatempodeexperimento = list()
listaexperimentos = list()
listadado_exp = list()
i = 0
numero = int(input("\n Quantidade de experimentos: \n"))
while i < numero:
    print("experimento ",i+1)
    tempodeinicio = int(input("\n Informe o tempo de início do experimento: \n"))
    lista_tempo_inicio.append(tempodeinicio)
    dado_exp = input("\n Digite a data: \n")
    listadado_exp.append(dado_exp)
    #print(lista_tempo_inicio)
    
    i+=1
    
else:
    print('\n ok \n')

print(lista_tempo_inicio)
print(listadado_exp)


# DISPOSITIVO 2:
        

listaExperimentoB = list()
lista_tempo_inicioB = list()
listatempodeexperimentoB = list()
experimentoB = list()
listadado_expB = list()
n = 0
numeroB = int(input("\n Quantidade de experimentos: \n"))
while n < numeroB:
    print("experimento ",n+1)
    tempodeinicioB = int(input("Informe o tempo de início do experimento:\n"))
    lista_tempo_inicioB.append(tempodeinicioB)
    dado_expB = input("Digite a data: \n")
    listadado_expB.append(dado_expB)
    #print(lista_tempo_inicio)
    
    n+=1
    
else:
    print('\n ok \n')

print(lista_tempo_inicioB)
print(listadado_expB)

# COMPARAÇÃO 

if dado_exp == dado_expB:
    
    if lista_tempo_inicio == lista_tempo_inicioB:

        print("os dispositivos estão alinhados no tempo \n")
    else: print("os dispositivos não estão alinhados no tempo \n")
else: print("os dispositivos não estão alinhados no tempo \n")





# FIM 