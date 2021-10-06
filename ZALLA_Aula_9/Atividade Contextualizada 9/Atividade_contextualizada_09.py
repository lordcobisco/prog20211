# Definição de variáveis, dados e matrizes:

import numpy as np

array_sensor1 = np.array([0, 1, 2, 3, 4, 5])
array_sensor2 = np.array([0, 1, 2, 3, 4, 5])

variacao_sensor1 = np.array([0])
variacao_sensor2 = np.array([0])
diferenca_sensor1 = np.array([0])
diferenca_sensor2 = np.array([0])

# Leitura do arquivo .csv original e reorganização das informações:

import csv

with open('Aula8.csv','r',newline='') as arquivo_csv:
    arquivo_leitura = csv.reader(arquivo_csv,delimiter=',')

    for linha in arquivo_leitura:
        linha[0] = linha[0].replace('"','')
        linha[0] = linha[0].replace('],[',', ')
        linha[0] = linha[0].replace('[','')
        linha[0] = linha[0].replace(']','')
        linha[0] = linha[0].replace(' ','')

        dados_brutos = linha[0].split(',')

        for i in range(12):
            dados_brutos[i] = float(dados_brutos[i])
        
        array_temp1 = np.array(dados_brutos[0:6])
        array_temp2 = np.array(dados_brutos[6:12])

        array_sensor1 = np.vstack((array_sensor1,array_temp1))
        array_sensor2 = np.vstack((array_sensor2,array_temp2))

    array_sensor1 = array_sensor1[1:,:]
    array_sensor2 = array_sensor2[1:,:]

    array_geral = np.stack((array_sensor1,array_sensor2))

# ((((array_geral[0,i,0]) / (math.sqrt((array_geral[0,i,1]) ** 2 + (array_geral[0,i,2]) ** 2))) * 180) / math.pi)
# ((((array_geral[1,i,0]) / (math.sqrt((array_geral[1,i,1]) ** 2 + (array_geral[1,i,2]) ** 2))) * 180) / math.pi)

# (((M * (array_geral[0,i,4]) * dt) + ((resultadosDadoa[0,i,0]) * (1 - M))) / (1 - M))
# (((M * (array_geral[1,i,4]) * dt) + ((resultadosDadoa[1,i,0]) * (1 - M))) / (1 - M))

# Definição da classe:

class Angulo:
    def __init__(self, sensor, tipo):
        self.sensor = sensor
        self.tipo = tipo

    def calcular_dadoa(self, resultadosDadoa1 = np.array([0]), resultadosDadoa2 = np.array([0])):

        import math

        if self.sensor == 1 and self.tipo == 'dadoa':
            for i in range(len(array_geral[0])):
                resultadosDadoa1_temp = np.array(((((array_geral[0,i,0]) / (math.sqrt((array_geral[0,i,1]) ** 2 + (array_geral[0,i,2]) ** 2))) * 180) / math.pi))
                resultadosDadoa1 = np.hstack((resultadosDadoa1,resultadosDadoa1_temp))
            return resultadosDadoa1[1:2001]

        elif self.sensor == 2 and self.tipo == 'dadoa':
            for i in range(len(array_geral[1])):
                resultadosDadoa2_temp = np.array(((((array_geral[1,i,0]) / (math.sqrt((array_geral[1,i,1]) ** 2 + (array_geral[1,i,2]) ** 2))) * 180) / math.pi))
                resultadosDadoa2 = np.hstack((resultadosDadoa2,resultadosDadoa2_temp))
            return resultadosDadoa2[1:2001]

    def calcular_angulo(self, M = 0.98, dt = 0.05, resultadosAngulo1 = np.array([0]), resultadosAngulo2 = np.array([0])):

        if self.sensor == 1 and self.tipo == 'ângulo':
            for i in range(len(array_geral[0])):
                resultadosAngulo1_temp = np.array((((M * (array_geral[0,i,4]) * dt) + ((resultadosDadoa1[i]) * (1 - M))) / (1 - M)))
                resultadosAngulo1 = np.hstack((resultadosAngulo1,resultadosAngulo1_temp))
            return resultadosAngulo1[1:2001]

        elif self.sensor == 2 and self.tipo == 'ângulo':
            for i in range(len(array_geral[1])):
                resultadosAngulo2_temp = np.array((((M * (array_geral[1,i,4]) * dt) + ((resultadosDadoa2[i]) * (1 - M))) / (1 - M)))
                resultadosAngulo2 = np.hstack((resultadosAngulo2,resultadosAngulo2_temp))
            return resultadosAngulo2[1:2001]

# Chamar os objetos da classe para execução das funções:

dadoa_1 = Angulo(1,'dadoa')
angulo_1 = Angulo(1,'ângulo')
dadoa_2 = Angulo(2,'dadoa')
angulo_2 = Angulo(2,'ângulo')

resultadosDadoa1 = dadoa_1.calcular_dadoa()
resultadosDadoa2 = dadoa_2.calcular_dadoa()

resultadosAngulo1 = angulo_1.calcular_angulo()
resultadosAngulo2 = angulo_2.calcular_angulo()

resultadosAngulo = np.vstack((resultadosAngulo1,resultadosAngulo2))

# Cálculos requisitados:

somatorio = resultadosAngulo.sum()

media = (resultadosAngulo.sum()) / (len(resultadosAngulo[0]) + len(resultadosAngulo[1]))

menor_angulo = resultadosAngulo.min()

maior_angulo = resultadosAngulo.max()

integral1 = np.cumsum(resultadosAngulo[0])

integral2 = np.cumsum(resultadosAngulo[1])

for i in range(len(resultadosAngulo[0])):
    diferenca1_temp = (resultadosAngulo[0].sum()) / (len(resultadosAngulo[0]) - ((resultadosAngulo[0,i]) ** 2)) / len(resultadosAngulo[0])
    diferenca_sensor1 = np.hstack((diferenca_sensor1,diferenca1_temp))

    diferenca2_temp = (resultadosAngulo[1].sum()) / (len(resultadosAngulo[1]) - ((resultadosAngulo[0,i]) ** 2)) / len(resultadosAngulo[1])
    diferenca_sensor2 = np.hstack((diferenca_sensor2,diferenca1_temp))


for i in range(len(resultadosAngulo[0]) - 1):
    variacao1_temp = np.array((resultadosAngulo[0,i+1]) - (resultadosAngulo[0,i]))
    variacao_sensor1 = np.hstack((variacao_sensor1,variacao1_temp))

    variacao2_temp = np.array((resultadosAngulo[1,i+1]) - (resultadosAngulo[1,i]))
    variacao_sensor2 = np.hstack((variacao_sensor2,variacao2_temp))

graus_arredondados = np.around(resultadosAngulo, 0)

# Informações a serem exibidas:

print("O somatório de todos os ângulos é:",somatorio)
print("A média de todos os ângulos é:",media)
print("O menor ângulo é:",menor_angulo)
print("O maior ângulo é:",maior_angulo)
print("A integral (soma acumulada) do vetor de ângulos para o 'Sensor 1' é:",integral1[-1])
print("A integral (soma acumulada) do vetor de ângulos para o 'Sensor 2' é:",integral2[-1])
print("A diferença da média e cada valor do vetor ao quadrado dividida pelo tamanho do vetor para o 'Sensor 1' é:",diferenca_sensor1[1:2001])
print("A diferença da média e cada valor do vetor ao quadrado dividida pelo tamanho do vetor para o 'Sensor 2' é:",diferenca_sensor2[1:2001])
print("As variações angulares (ang-n+1 menos ang-n) no 'Sensor 1' são de:",variacao_sensor1[1:2000])
print("As variações angulares (ang-n+1 menos ang-n) no 'Sensor 2' são de:",variacao_sensor2[1:2000])
print("Todos os ângulos, em graus e arredondados, são:",graus_arredondados)
