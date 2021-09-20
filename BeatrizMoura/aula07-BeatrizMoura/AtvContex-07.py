
# Simulação de Dispositivo com Led RGB

import time
import random
import sys

print('Dispositivo de Optogenética\n')
start = input('Olá! Deseja iniciar o programa? Digite S para continuar ou N para sair do programa.\n')
t = time.time()

def light_on(v):

    V = float(v)

    if(v == 1.0):
        
        color = led[0][0]

    elif(v == 2.0):
        color = led[1][0]

    else:
        color = led[2][0]
        
    return color

if start == 'S' or start == 's':

    led = (('R', 1.0), ('G',2.0), ('B',3.0)) # valores arbitrarios para determinar as tensões nos canais
    electrode = []
    channel = int(input(' Dado que existem 32 canais no eletrodo, selecione qual canal voce deseja acionar de 1 a 32: \n'))

    for i in range (1,32):

        electrode.insert(i, channel)
             
turn_on = input(' Deseja ativar o canal? Digite S para continuar ou N para sair do programa. \n' )

while(turn_on == 'S' or turn_on == 's'):
   
    for i in range (0,33):

       if i == channel - 1:

            v = input('Atenção! Informe qual a tensão do canal escolhido: 1V, 2V ou 3V: \n')

            led_RGB = light_on(v)

            print(' O LED que está ligado é o', led_RGB, 'do canal', electrode[i] )

            turn_off = input(' Caso deseje encerrar o programa, digite N.\n')
            turn_on = input(' Deseja acionar outro canal?\n') 

execution_time = time.time() - t

print( ' O tempo de execução do programa foi de: ', execution_time)

print(' Fim da execução. \n')
