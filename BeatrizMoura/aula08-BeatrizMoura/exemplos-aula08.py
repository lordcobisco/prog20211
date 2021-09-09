
# Aula sobre Arquivos
'''
arquivoObjeto = open('nomeDoArquivo1.txt', 'w')
#print(arquivoObjeto)

arquivoObjeto.write('Escrevendo a primeira linha do arquivo!\n')
arquivoObjeto.write('Escrevendo a segunda linha do arquivo!\n')

arquivoObjeto.close()

'''

#arquivoObjeto = open('nomeDoArquivo1.txt', 'r')
#conteudoArquivo = arquivoObjeto.read

#for i in range(10):
 #   conteudoArquivo = arquivoObjeto.read(i)
  #  print(conteudoArquivo)

#conteudoArquivo = arquivoObjeto.readlines()
#print(conteudoArquivo[1])

'''

arquivoObjeto = open('nomeDoArquivo1.txt', 'w')
lista = ['eu',' escrevo',' a lista toda ', ' de uma', ' vez']
arquivoObjeto.writelines(lista)
arquivoObjeto.close()
arquivoObjeto = open('nomeDoArquivo1.txt', 'r')


for linha in arquivoObjeto:
    print(linha)
arquivoObjeto.close()

'''

#with open('nomeDoArquivo1.txt', 'r') as arquivo:
 #   print(arquivo.closed)
  #  for line in arquivo:
   #     print(line)
#print(arquivo.closed)

import csv
with open('nomeDoArquivo.csv', 'w', newline='\n') as arquivo:
    spamWriter = csv.writer(arquivo, delimiter= ';')
    spamWriter.writerow(['escrevendo alguma coisa na linha'])
    spamWriter.writerow([1,2,3,4])


with open('nomeDoArquivo.csv', 'r', newline='\n') as arquivo:
    spamReader = csv.reader(arquivo, delimiter= ';')
    spamReader.writerow(['escrevendo alguma coisa na linha'])
    for row in spamReader:
        print(row)
    