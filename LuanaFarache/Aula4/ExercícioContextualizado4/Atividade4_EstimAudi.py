'''
O presente programa tem por objetivo sistematizar um método de discriminação 
de estímulos auditivos para primatas através do condicionamento operante.
'''

Habituação = input("O animal esta habituado? Digite 1 para Sim e 0 para Não \n")

# 1. Inicialização do programa - HABITUAÇÃO:
if Habituação == 1:
    print("Programa iniciado!\n")

    Aproximação = float(input("A que distância está o animal, em centímetros? \n"))
    Aproximação1 = 30

    if Aproximação < Aproximação1:
        print("0,5ML de recompensa foi liberada!\n")

    # 2. Regime de APROXIMAÇÕES SUCESSIVAS: 

    ToqueBarra = bool
    Contador1 = 0

    ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
    ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
        ToqueBarra = bool(input("O animal tocou a barra? Digite 1 para Sim e 0 para Não \n"))
    if ToqueBarra:
        Contador1 += 1
    if Contador1 == 20:
        print ('O animal está apto a proxima fase')
    elif Contador1 < 20:
        print ('O experimento não pode seguir para a fase 2') 

elif Habituação == 0:
    print("Realize a habituação do animal antes de iniciar o programa!\n")

# Associação entre estímulo sonoro e toque na barra:
Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
contador2 = 0
if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
    contador2 += 1
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")
contador3 = 0

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
    contador3 =+ 1
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

TempoExperimento = float(input("Quanto tempo durou o experimento, em minutos? \n"))
Tempo = 30

if (TempoExperimento <= Tempo) and (contador2 == 50) and (contador3 == 50):
    print("O experimento passou para a próxima etapa!\n")
else:
    print("O experimento não poderá seguir para a proxima fase! \n")

print("Experimento finalizado!\n")