'''
Fundamentos de Programação - IINELS
Atividade Contextualizada 06 - Cirurgia Esterotáxica
Nome: Luiz Henrique Bertucci
Orientações: https://drive.google.com/open?id=1dJ8IbyKKS-6u7NJ40F2IT1qyUuWtyjXX&authuser=andre.dantas%40isd.org.br&usp=drive_fs
'''

print('Automatização de Cirurgia Esterotáxica\n\n')

#id = str(input('Digite a identificação do animal: (Exemplo: 001, 002, 003...)'))

listaAnimal = ['rato', 'camundongo']
listaAnestesico = ('Ketamina','Xilazina','Halotano')

animal = int(input('Qual o tipo do animal?\n 1-> rato | 2-> camundongo\n'))
anestesico = int(input('Qual o anestésico? 1-> Katemina | 2-> Xilazina | 3->Halonato\n'))

if (anestesico == 1 or anestesico == 2):
    dose = int(input('Informe a dosagem do anestésico conforme o peso do animal. (Unidade: mg)\n'))
    print('************Opções escolhidas**************')
    print('O animal, anestésico e dosagem são:')
    print('',listaAnimal[animal-1],'\n', listaAnestesico[anestesico-1],'\n', dose,' ml')
elif anestesico == 3:
    dose = int(input('Informe a dosagem do anestésico conforme o peso do animal. (Unidade: mm³)\n'))
    print('************Opções escolhidas**************')
    print('O animal, anestésico e dosagem são:')
    print('',listaAnimal[animal-1],'\n', listaAnestesico[anestesico-1],'\n', dose,' mm³')   
else:
    print('A opção não existe')       

anestesiaOK = False
while anestesiaOK == 0:
    anestesiaOK = int(input('A anestesia já fez efeito? sim-> 1 | não-> 0\n'))
print('\n\n*****Animal Anestesiado*****\nPosicione o animal na mesa\n\n')

Bregma = 1
Lambda = 2
while Bregma != Lambda:
    print('Informe os angulos bregma e lambda:')
    Bregma = float(input('Bregma: \n'))
    Lambda = float(input('Lambda: \n'))
print('\n*********Posição correta************\n')
print('Realize os seguintes passos de higienização da área a ser operada:')
print(
'   ***Retire a pele da calota do crânio\n',
'  ***Retire os tecido moles até a caixa craniana\n',
' ***Higienize com 10 volumes de H2O2\n',
'***Aplique uma pequena camada de poliacrilato para evitar sangramento\n'
)
print('Escolha os pontos de fixação dos parafusos\n Digite enter para girar 25% de uma volta de parafuso:')
parausoOK = False

for i in range(12): 
    i += 1
    if i == 12:
        print('Limite de 3 voltas alcançado') 
    parafusoOK = int(input('Número de voltas alcançado? 0-> não | 1-> sim\n'))
    if parafusoOK==1:
        break
    voltas = (i*0.25)
    print('Número de voltas: ', voltas)

print('\n*******Ajuste das cânulas********\n')
#AP = 6, LL = 3.03, DV = 4
localizacao = { 'AnteroPosterior' : 6, 'LateroLateral': 3.03, 'DorsoVentral':4}
print('Realize a furação da meninge com angulação de aproximadamente 45º\n' )
print('localização para inserção em centrímetros: ', localizacao)

print('\n Drenar qualquer sangue ou líquido cefalorraquidiano nos orifícios ')
print('\nInserir o capacete feito com a mistura de acrílico polimerizante e solvente')
print('\n Retiro o', listaAnimal[animal-1] ,' da mesa de cirurgia e leve até um ambiente pós operatório')

print('Fim do programa')
