
import csv
import math 

with open("coletaFlexJoelho.csv","r") as csvFile:
  reader = csv.reader(csvFile)
  data = []
  for row in reader:
     if len(row) !=0:
        data = data + [row]
csvFile.close()

print(data)

archive = []
sensors = []

for line in archive:
    valor = line.split('],""[')
    sensor1 = valor[0].split('[')[1]
    sensor2 = valor[1].split(']"""')[0]

    for sensor01 in sensor1.split(","):
        sensors.append(float(sensor01))
    for sensor02 in sensor2.split(","):
        sensors.append(float(sensor02))

print (sensors)                             

def cal():
    angulo = 0
    v = []

    for i in range(4,len(sensors),4):
        angulo = 0.98(angulo+sensors[i]*0.05)+(1-0.98)*sensors[i-3]
        v.append(angulo)

    return v 