# arquiObjeto = open('meuEscritosPy.txt','w')
# arquiObjeto.write('Primeira Linha do arquivo')
# arquiObjeto.write('Segunda Linha do Arquivo')

import csv

with open('/arquivo.csv', 'w', newline='\n') as arquivo:
    spamwrite = csv.writer(arquivo, delimiter=';')
    spamwrite.writerow([1,2,3,4])

