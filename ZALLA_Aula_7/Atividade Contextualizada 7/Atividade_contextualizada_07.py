import random  # Biblioteca de dados randomicos, para simular o input do dispositivo conectado ao rato.
import keyboard  # biblioteca de leitura de teclado windows para reconhecer uma comando teclado.

#Dois dispositivos, um dispositivo (1) no rato, lendo o tipo de sinal emitido e outro dispositivo (2) externo, lendo a intensidade de sinal emitido pelo dispositivo 1.

### Estado cores do led dispositivo 1, onde FALSE = desligado e TRUE = ligado ###
Led_red_dispotitivo_1 =  False
Led_green_dispositivo_1 = False
Led_blue_dispositivo_1 = False

### Estado cores do led dispositivo 2, onde FALSE = desligado e TRUE = ligado ###
Led_red_dispotitivo_2 =  False
Led_green_dispositivo_2 = False
Led_blue_dispositivo_2 = False


while True:
    ### Ações dispositivo 1
    ### tipo de sinal emitidos pelo dispositivo 1 no rato
    tipo_de_sinal = random.randint(1, 3)    # numero randomico gerado de 1 a 3, simulando o tipo de sinal emitido pelo rato
    print('tipo de sinal dispositivo no rato (1 = recompensa, 2 = comportamento social e 3 = memória): ', tipo_de_sinal) 

    intensidade_de_sinal = random.randint(1, 10)  # numero randomico gerado de 1 a 10, simulando a intensidade de sinal emitido pelo rato
    print('intensidade de sinal do dispositivo no rato (0 a 10): ', intensidade_de_sinal)


    if tipo_de_sinal == 1:    ### dispositivo 1 ascende led Verde ###
        Led_red_dispotitivo_1 = False
        Led_green_dispositivo_1 = True
        Led_blue_dispositivo_1 = False
        print("dispositivo 1 (rato), acende led VERDE (recompensa)")

    if tipo_de_sinal == 2:    ### dispositivo 1 ascende led Vermelho ###
        Led_red_dispotitivo_1 = True
        Led_green_dispositivo_1 = False
        Led_blue_dispositivo_1 = False
        print("dispositivo 1 (rato), acende led VERMELHO (social)")

    if tipo_de_sinal == 3:    ### dispositivo 1 ascende led AZUL ###
        Led_red_dispotitivo_1 = False
        Led_green_dispositivo_1 = False
        Led_blue_dispositivo_1 = True
        print("dispositivo 1 (rato), acende led AZUL (memória)")


    ### Ações dispositivo 2
    ### Cores do led indicam a intensidade do sinal enviado do dispositivo 1 (rato) para o dispositivo 2 (externo)

    if intensidade_de_sinal >= 0 and intensidade_de_sinal <= 3: ### dispositivo 2 ascende led Verde ###
        Led_red_dispotitivo_1 = False
        Led_green_dispositivo_1 = True
        Led_blue_dispositivo_1 = False
        print("dispositivo 2 (externo), acende led VERDE (INTENSIDADE DE SINAL BAIXA)")

    if intensidade_de_sinal >= 4 and intensidade_de_sinal <= 7: ### dispositivo 2 ascende led AMARELO ###
        Led_red_dispotitivo_1 = True
        Led_green_dispositivo_1 = True
        Led_blue_dispositivo_1 = False
        print("dispositivo 2 (externo), acende led AMARELO (INTENSIDADE DE SINAL MÉDIA)")

    if intensidade_de_sinal >= 8 and intensidade_de_sinal <= 10: ### dispositivo 2 ascende led VERMELHO ###
        Led_red_dispotitivo_1 = True
        Led_green_dispositivo_1 = False
        Led_blue_dispositivo_1 = False
        print("dispositivo 2 (externo), acende led VERMELHO (INTENSIDADE DE SINAL ALTA)")

    time.sleep(5) ### Intervalo do SFTW, fazendo o mesmo refazer a leitura a cada 5 segundos ###

    if keyboard.is_pressed('q'):          ### segurar a tecla "Q" para parada da aplicação.
        print("PARADA SOLICITADA")
        break
