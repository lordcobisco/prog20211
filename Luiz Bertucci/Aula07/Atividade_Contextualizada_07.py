'''
Fundamentos de Programação - IINELS
Atividade Contextualizada 07 - Optogenética
Nome: Luiz Henrique Bertucci
Orientações: https://docs.google.com/presentation/d/1M5wvnejQbzEGdQsFDux3ikWJhyj58LTd/edit#slide=id.p39
'''
import time


def defineRGB(tensaoArg):
    rgb = {3:'vermelho', 4 : 'verde', 5 : 'azul' }
    if tensaoArg == 3 or tensaoArg == 4 or tensaoArg == 5:
        temp = rgb[tensaoArg]
    else:
        temp = 'Erro : Fora do range de RGB'
    return temp


canaisON = int(input('Digite a quantidade de canais do experimento: (Máximo 32)\n')) 

canal = []
tensao= []
tempoLiga = []

for i in range (canaisON):
    i += 1
    print('SETUP', i, 'Digite o número do canal, a tensão (entre 3, 4 e 5 Volts)  e o tempo(segundos) em que deve ser ligado')
    temp = int(input('Canal: \n'))
    canal.append(temp)
    temp = int(input('Tensão: \n'))
    tensao.append(temp)
    temp = float(input('Tempo: \n'))
    tempoLiga.append(temp)

print ('Iniciar teste com os seguintes parâmetros:')
for i in range(canaisON):
    i+=1
    print('Canal:', canal[i-1], '| Cor:', defineRGB(tensao[i-1]), '| Tempo:', tempoLiga[i-1])

print('******Iniciar estimulação optogenética******')

timeOver = time.time() + (max(tempoLiga))
#print(timeAtual, timeOver)

timeAtual = time.time()

while(timeOver >= timeAtual)*100:
    for i in range(len(tempoLiga)):
        i += 1
        temp = tempoLiga[i-1]
        #print(temp)
        #print(timeOver-timeAtual)
        if ( temp < max(tempoLiga) and((timeOver - timeAtual)*100)<= temp) and (temp <= ((timeOver - timeAtual)*100)+0.1):
          print('SETUP ',(i-1), ' encerrado.\n Tempo previsto:',tempoLiga[i-1], '\nTempo executado: ', (timeOver - timeAtual)*100)
        #print(time.time())
        #print(tempoLiga[i-1]) 
    timeAtual = time.time()    
print('TODOS OS CANAIS ENCERRADOS\nTempo de estimulação total: ',max(tempoLiga)) 
