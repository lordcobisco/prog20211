import numpy as np 
import math
import csv

ang = list()
lista_de_Variaveis = ('ACEX', 'ACEY', 'ACEZ', 'velAngX', 'velAngY', 'velAngZ')
sensor1 = list()
sensor2 = list()



# with open('C:\\Users\Mariza\Desktopjoelho.csv', 'r', newline='') as arquivo:
with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    for linha in spamreader:
        print(linha)


# Para o sensor 1 
with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    j=0
    for linha in spamreader:
        saida = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        sensor1.append(dict())
        for i in range(len(saida)):
            sensor1[j][lista_de_Variaveis[i]] = (saida[i]) 
        j+=1
    print(sensor1)

# Para o sensor 2 
with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    j=0
    for linha2 in spamreader:
        saida2 = linha2[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        sensor2.append(dict())
        for i in range(len(saida2)):
            sensor2[j][lista_de_Variaveis[i]] = (saida2[i]) 
        j+=1
    print(sensor2)


#Resolvendo a equação, o resultado aproximado fica:
#fica: ang = 2.45**(velAngY) + dado_um

dado_um = list()
def  calcang(dado_um, ang):
    return  dado_um, ang
    dado_um = float(input("Informe o valor do dado_um: "))
    ang = 2.45**[velAngY] + dado_um
print(dado_um, ang)
  

arquivotxt = open('resultadoang.txt','w')
arquivocsv = open('resultadoang.csv', 'w', newline = '')
spamwriter = csv.writer(arquivocsv, delimiter = '', quotecar = '|', quoting = csv.QUOTE_MINIMAL)
arquivotxt.write('sensor1')

for m in sensor1:
    ang.append(ang(m,ang))

for n in ang:
    print(n)
    arquivotxt.write(str(n))
    spamwriter.writerow(str(n))

print('Resultados')
arquivotxt.close()
arquivocsv.close()
    

# Para o sensor 2 

with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    j=0
    for linha2 in spamreader:
        saida2 = linha2[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        sensor2.append(dict())
        for i in range(len(saida2)):
            sensor2[j][lista_de_Variaveis[i]] = (saida2[i]) 
        j+=1
    print(sensor2)


#Resolvendo a equação, chega-se no seguinte resultado aproximado
#fica: ang = 2.45**(velAngY) + dado_um


def  calcang(dado_um, ang):
    return dado_um, ang
    dado_um=float(input("valor de dado_um: "))
    ang = 2.45**[velAngY] + dado_um
print(dado_um, ang)  

arquivotxt = open('resultadoang.txt','w')
arquivocsv = open('resultadoang.csv', 'w', newline = '')
spamwriter = csv.writer(arquivocsv, delimiter = '', quotecar = '|', quoting = csv.QUOTE_MINIMAL)
arquivotxt.write('sensor2')


for m in sensor2:
    ang.append(ang(m,ang))

for n in ang:
    print(n)
    arquivotxt.write(str(n))
    spamwriter.writerow(str(n))

print('Resultados')
arquivotxt.close()
arquivocsv.close()
    