#variavel

arquivoObjeto = open('nomeDoArquivo1.txt','w')
#print(arquivoObjeto)
#faço operação quando usa o ponto .
arquivoObjeto.write('Escrevendo a primeira linha do arquivo\n')
arquivoObjeto.write('Escrevendo a segunda linha do arquivo\n')
arquivoObjeto.close()
#fechar antes de finalizar
#duas forma de dizer onde o arquivo esta
#caminho relativo /

#Ler o arquivo
arquivoObjeto= open ('arquivo/nomeDoarquivo.txt','r')
conteudoarquivo = arquivoObjeto.read()
print(conteudoarquivo)
#ler uma linha especifica
#conteudoarquivo = arquivoObjeto.read()
for i in range (10):
    conteudoarquivo = arquivoObjeto.read(i)
    print(conteudoarquivo)
conteudoarquivo = arquivoObjeto.readlines(2)
print(conteudoarquivo)
conteudoarquivo = arquivoObjeto.readlines()
print (arquivoObjeto[1])

# ler linha por linha
for linha in arquivoObjeto:
    print(linha)

#escrever alguma coisa em uma lista
lista = ['eu ','escrevo','a lista','toda','de','uma','vez']
arquivoObjeto.writelines(lista)
arquivoObjeto.close()
arquivoObjeto = open ('arquivo/nomeDoArquivo.txt','r')
for linha in arquivoObjeto:
    print(linha)
    arquivoObjeto.close()
#ler e escrver
with open('arquivo/nomedoarquivo.txt','r') as arquivo:
    for line in arquivo:
        print(line)
        print(arquivo.closed)

#ler arquivo csv usar uma biblioteca que entende como o csv funciona
import csv
with open('nomeDoArquivo.csv','w',newline='\n') as arquivo:
    spamwriter = csv.writer(arquivo, delimiter = ';')
    spamwriter.writerow()
    spamwriter.writerow([1,2,3,4])

with open('nomeDoArquivo.csv','w',newline='\n') as arquivo:
    spamreader = csv.reader(arquivo, delimiter = ';')
    for row in spamreader :
        print(row)
        
