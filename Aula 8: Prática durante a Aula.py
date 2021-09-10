# Leitura de arquivos TXT

arquivo_objeto = open('nome_do_arquivo.txt','w')
print(arquivo_objeto)
arquivo_objeto.write('escrevendo a primeira linha do arquivo\n')
arquivo_objeto.write('escrevendo a segunda linha do arquivo\n')
arquivo_objeto.close()


arquivo_objeto = open ('arquivos/arquivo_objeto.txt', 'r')
conteudo_do_arquivo = arquivo_objeto.read()

for i in range(10): 
    conteudo_do_arquivo = arquivo_objeto.read(i)
    print(conteudo_do_arquivo)

conteudo_do_arquivo = arquivo_objeto.readlines()
print(conteudo_do_arquivo[0])

arquivo_objeto = open ('arquivos/arquivo_objeto.txt', 'r')
for linha in arquivo_objeto:
    print(linha)

arquivo_objeto = open ('arquivos/arquivo_objeto.txt', 'r')
lista = ['eu','escrevo','a lista','toda','de','uma','vez']
arquivo_objeto.writelines(lista)
arquivo_objeto.close()


for linha in arquivo_objeto:
    print(linha)
arquivo_objeto.close()


with open ('arquivos/arquivo_objeto.txt', 'r') as arquivo:
    for line in arquivo:
        print(line)
print(arquivo.closed)

# Leitura de arquivos CSV
import csv # Essa é uma biblioteca que ajuda a lidade com o tipo de arquivo csv
with open ('nomeDoArquivo.csv', 'w',newline='\n') as arquivo:
    spamwriter = csv.writer(arquivo, delimiter=' ')
spamwriter.writerow(['escrevendo alguma coisa na linha']

with open ('nomeDoArquivo.csv', 'w',newline='\n') as arquivo:
    spamwriter = csv.writer(arquivo, delimiter=';')
spamwriter.writerow([1,2,3,4]

with open ('nomeDoArquivo.csv', 'r',newline='\n') as arquivo:
    spamreader = csv.writer(arquivo, delimiter=';')
    for row in spamreader:

##################################################




