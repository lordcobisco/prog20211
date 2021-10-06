# Definição de variáveis, tuplas, listas e/ou dicionários:

dados_brutos = []
sensor_1 = []
sensor_2 = []

resultadosDadoa = {'Sensor 1':[],'Sensor 2':[]}
resultadosAngulo = {'Sensor 1':[],'Sensor 2':[]}

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

        sensor_1.append(dados_brutos[0:6])
        sensor_2.append(dados_brutos[6:12])

    for i in range(len(sensor_1)):
        (sensor_1[i][0]) = float(sensor_1[i][0])
        (sensor_1[i][1]) = float(sensor_1[i][1])
        (sensor_1[i][2]) = float(sensor_1[i][2])
        (sensor_1[i][3]) = float(sensor_1[i][3])
        (sensor_1[i][4]) = float(sensor_1[i][4])
        (sensor_1[i][5]) = float(sensor_1[i][5])
    
    for i in range(len(sensor_2)):
        (sensor_2[i][0]) = float(sensor_2[i][0])
        (sensor_2[i][1]) = float(sensor_2[i][1])
        (sensor_2[i][2]) = float(sensor_2[i][2])
        (sensor_2[i][3]) = float(sensor_2[i][3])
        (sensor_2[i][4]) = float(sensor_2[i][4])
        (sensor_2[i][5]) = float(sensor_2[i][5])

# Definição da classe:

class Angulo:
    def __init__(self, sensor, tipo):
        self.sensor = sensor
        self.tipo = tipo

    def calcular_dadoa(self):

        import math

        if self.sensor == 1 and self.tipo == 'dadoa':
            for i in range(len(sensor_1)):
                resultadosDadoa['Sensor 1'].append(((((sensor_1[i][0]) / (math.sqrt((sensor_1[i][1]) ** 2 + (sensor_1[i][2]) ** 2))) * 180) / math.pi))

        elif self.sensor == 2 and self.tipo == 'dadoa':
            for i in range(len(sensor_2)):
                resultadosDadoa['Sensor 2'].append(((((sensor_2[i][0]) / (math.sqrt((sensor_2[i][1]) ** 2 + (sensor_2[i][2]) ** 2))) * 180) / math.pi))

    def calcular_angulo(self, M = 0.98, dt = 0.05):

        if self.sensor == 1 and self.tipo == 'ângulo':
            for i in range(len(sensor_1)):
                resultadosAngulo['Sensor 1'].append((((M * (sensor_1[i][4]) * dt) + ((resultadosDadoa['Sensor 1'][i]) * (1 - M))) / (1 - M)))

        elif self.sensor == 2 and self.tipo == 'ângulo':
            for i in range(len(sensor_2)):
                resultadosAngulo['Sensor 2'].append((((M * (sensor_2[i][4]) * dt) + ((resultadosDadoa['Sensor 2'][i]) * (1 - M))) / (1 - M)))

# Chamar os objetos da classe para execução das funções:

dadoa_1 = Angulo(1,'dadoa')
angulo_1 = Angulo(1,'ângulo')
dadoa_2 = Angulo(2,'dadoa')
angulo_2 = Angulo(2,'ângulo')

dadoa_1.calcular_dadoa()
dadoa_2.calcular_dadoa()

angulo_1.calcular_angulo()
angulo_2.calcular_angulo()

# Salvar os dados em .txt:

novo_arquivo_txt = open('anguloProcessado.txt','w')

novo_arquivo_txt.write('Ângulos para o Sensor 1: '+str(resultadosAngulo['Sensor 1'])+'\n')
novo_arquivo_txt.write('\nÂngulos para o Sensor 2: '+str(resultadosAngulo['Sensor 2']))

novo_arquivo_txt.close()

# Salvar os dados em .csv:

with open('anguloprocessado.csv','w',newline='') as novo_arquivo_csv:

    arquivo_escrita = csv.writer(novo_arquivo_csv,delimiter=',')

    arquivo_escrita.writerow(['Sensor 1'] + ['Sensor 2'])

    for i in range(len(resultadosAngulo['Sensor 1'])):
        arquivo_escrita.writerow([resultadosAngulo['Sensor 1'][i]] + [resultadosAngulo['Sensor 2'][i]])
