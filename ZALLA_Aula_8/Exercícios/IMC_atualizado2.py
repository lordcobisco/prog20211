informacoes = {'Peso': [], 'Altura': [], 'IMC': [], 'Situação': []}

def calculoIMC(peso,altura):
    imc = peso / (altura**2)
    if imc<17:
        situacao = "Muito abaixo do peso normal."
        print("Muito abaixo do peso normal, pois imc =",imc)
    elif imc>=17 and imc<=18.5:
        situacao = "Abaixo do peso normal."
        print("Abaixo do peso normal, pois imc =",imc)
    elif imc>18.5 and imc<=25:
        situacao = "Peso dentro do normal."
        print("Peso dentro do normal, pois imc =",imc)
    elif imc>25 and imc<=30:
        situacao = "Acima do peso normal."
        print("Acima do peso normal, pois imc =",imc)
    elif imc>30:
        situacao = "Muito acima do peso normal"
        print("Muito acima do peso normal, pois imc =",imc)
    
    informacoes['Peso'].append(peso)
    informacoes['Altura'].append(altura)
    informacoes['IMC'].append(imc)
    informacoes['Situação'].append(situacao)


    repeticao = int(input('Digite 1 para repetir o programa ou digite 0 para finalizá-lo e salvar as informações dadas até agora: [1/0] '))
    while repeticao != 1 and repeticao != 0:
        repeticao = int(input('Desculpe, não entendi. Acho que você digitou um número diferente de 1 ou 0. Por favor, para repetir o programa, digite 1, ou, para encerrar, digite 0: [1/0] '))
    else:
        if repeticao == 1:
            peso = float(input("Por favor, informe seu peso em kg: "))
            altura = float(input("Por favor, informe sua altura em m: "))
            calculoIMC(peso,altura)
        elif repeticao == 0:
            print('Fim do programa. Vamos salvar as informações geradas até agora.\n')

peso = float(input("Por favor, informe seu peso em kg: "))
altura = float(input("Por favor, informe sua altura em m: "))

calculoIMC(peso,altura)

# Salvar as informações geradas:

modo_salvar = input("Você deseja salvar as informações sobre o IMC em que formato? [csv/txt] ")
nome_arquivo = input("Qual o nome que deseja dar para o referido arquivo? ")

while modo_salvar != 'csv' and modo_salvar != 'txt':
        modo_salvar = input('Desculpe, não entendi o formato que você deseja. Digite um formato adequado: [csv/txt] ')

else:
    if modo_salvar == 'csv':
        import csv

        with open((nome_arquivo+'.csv'),'w',newline='') as arquivo_csv:

            arquivo_escrita = csv.writer(arquivo_csv,delimiter=',')

            arquivo_escrita.writerow(['Peso'] + ['Altura'] + ['IMC'] + ['Situação'])

            for i in range(len(informacoes['IMC'])):
                arquivo_escrita.writerow([informacoes['Peso'][i]] + [informacoes['Altura'][i]] + [informacoes['IMC'][i]] + [informacoes['Situação'][i]])
                
        print('Os dados já foram salvos no formato .csv.')

    elif modo_salvar == 'txt':

        arquivo_txt = open((nome_arquivo+'.txt'),'w')

        arquivo_txt.write('Pesos: '+str(informacoes['Peso'])+'\n')
        arquivo_txt.write('Alturas: '+str(informacoes['Altura'])+'\n')
        arquivo_txt.write('IMCs: '+str(informacoes['IMC'])+'\n')
        arquivo_txt.write('Situações: '+str(informacoes['Situação']))

        arquivo_txt.close()

        print('Os dados já foram salvos no formato .txt.')