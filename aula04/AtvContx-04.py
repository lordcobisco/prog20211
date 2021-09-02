
print('Este programa eh destinado a desenvolver o comportamento condicionado de animais\n')
print("Fase 1\n")

distancia = 30 # variavel inicial para discriminar a distancia limite entre o animal e as barras

habituacao = str(input(" Deseja iniciar o processo de habituacao? Digite Sim ou Nao:\n"))

if habituacao == 'Sim':

    print("Daremos inicio ao treinamento!\n")

    d0 = float(input(" Digite a qual o valor da distancia que o animal se encontra da barra:\n"))
    
    if distancia < d0:
        print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d1 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d0 < d1:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d2 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d2 < d1:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d3 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d3 < d2:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d4 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d4 < d3:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d5 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d5 < d4:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d6 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d6 < d5:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d7 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d7 < d6:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d8 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d8 < d7:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d9 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d9 < d8:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d10 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d10 < d9:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d11 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d11 < d10:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d12 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d12 < d11:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d13 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d13 < d12:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d14 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d14 < d13:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d15 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d15 < d14:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d16 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d16 < d15:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d17 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d17 < d16:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

    d18 = float(input(" Digite qual a nova distancia marcada entre o animal e as barras:\n"))

    if d18 < d17:
         print( " Sera liberado 0.5ml de recompensa! ")
    else:
        print("O animal nao atendeu ao estimulo. Liberacao de recompensa negada! ")

        print(" O animal praticou durante 20 repeticoes! Daremos inicio a Fase 2 do treinamento!\n")


        # inicio da tentativa 1

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 1


        # inicio da tentativa 2

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 2

         # inicio da tentativa 3

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 3

         # inicio da tentativa 4

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 4

         # inicio da tentativa 5

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 5

         # inicio da tentativa 6

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 6

         # inicio da tentativa 7

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 7

         # inicio da tentativa 8

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 8

         # inicio da tentativa 9

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 9

         # inicio da tentativa 10

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 10


# inicio da tentativa 11

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 11


        # inicio da tentativa 12

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 12

         # inicio da tentativa 13

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 13

         # inicio da tentativa 14

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 14

         # inicio da tentativa 15

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 15

         # inicio da tentativa 16

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 16

         # inicio da tentativa 17

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 17

         # inicio da tentativa 18

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 18

         # inicio da tentativa 19

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 19

         # inicio da tentativa 20

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 20



        # inicio da tentativa 21

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 21


        # inicio da tentativa 22

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 22

         # inicio da tentativa 23

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 23

         # inicio da tentativa 24

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 24

         # inicio da tentativa 25

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 25

         # inicio da tentativa 26

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 26

         # inicio da tentativa 27

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 27

         # inicio da tentativa 28

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 28

         # inicio da tentativa 29

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 29

         # inicio da tentativa 30

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 30


# inicio da tentativa 31

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 31


        # inicio da tentativa 32

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 32

         # inicio da tentativa 33

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 33

         # inicio da tentativa 34

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 34

         # inicio da tentativa 35

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 35

         # inicio da tentativa 36

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 36

         # inicio da tentativa 37

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 37

         # inicio da tentativa 38

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 38

         # inicio da tentativa 39

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 39

         # inicio da tentativa 40

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 40


         # inicio da tentativa 41

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 41


        # inicio da tentativa 42

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 42

         # inicio da tentativa 43

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 43

         # inicio da tentativa 44

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 44

         # inicio da tentativa 45

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 45

         # inicio da tentativa 46

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 46

         # inicio da tentativa 47

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 47

         # inicio da tentativa 48

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 48

         # inicio da tentativa 49

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 49

         # inicio da tentativa 50

        somphee = str(input('Observe se o animal toca a barra esquerda ao ouvir o som phee! Digite s ou n:\n'))
        somtrill = str(input('Observe se o animal toca a barra esquerda ao ouvir o som trill! Digite s ou n:\n'))

        if (somphee == 's' and somtrill == 's'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 'n' and somtrill == 's'):
            print ("Som phee: não liberar recompensa.")
            print ("Som trill: liberar 0,5ml de recompensa!")
        elif (somphee == 's' and somtrill == 'n'):
            print ("Som phee: liberar 0,5ml de recompensa!")
            print ("Som trill: não liberar recompensa.")
        else:
         print ("Não liberar recompensa, o treinamento nao foi realizado com sucesso!") # fim da repeticao 50

         print('Foram realizadas 50 sessoes de estimulos sonoros')

         tempo = float(input('Digite quanto tempo durou a Fase 2 da sessao de treinamento\n'))

         if tempo > 30:
             print(' O tempo excedeu 30 minutos e o treinamento nao podera ser contabilizado. Realize novamente o treinamento apos 4 horas de descanso!')
         else:
            print(' O treinamento foi realizado com sucesso! O treinamento podera seguir para proxima fase.\n')
else:
    print(' Feche o programa e o reabra em seguida.')
print(' Fim do programa.')














