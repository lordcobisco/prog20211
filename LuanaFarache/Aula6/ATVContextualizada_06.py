'''
Rotina criada para atender aos requisitos da atividade contextualizada 6 - Disciplina de introdução à programação.

Desenvolva um programa em Python que automatize o procedimento cirúrgico estereotáxico apresentado, assumindo que:

a.	As entradas (seja informações de máquina, posicionamentos a serem medidos etc.) serão traduzidas em inputs no programa.
b.	O detalhamento das etapas é informado na tela para o usuário a cada passo do procedimento.
c.	O programa deve conter estruturas de tomada de decisão (if-elif-else).
d.	O programa deve conter estruturas de repetição (while-for).
e.	O programa deve conter pelo menos 1 variável de cada tipo (lista, tupla e dicionário)

'''

# Automatização de cirurgia estereotáxia em animais para fins de pesquisa:

#QUESTÃO A)
OpAnimal=('Rato','Camudongo','Coelho')
Animal=0
while Animal==0:
    Animal = int(input('Insira uma valor de 1 a 3 para informar a ESPÉCIE de animal: \n 1-Rato \n 2-Camudongo \n 3-Coelho \n'))
    if Animal == 1 or Animal == 2 or Animal == 3:
        print('Você escolheu a opção:',OpAnimal[Animal-1],'\n')
    else:
        print('Digite uma informação válida!!')
        Animal=0

OpAnestesia=('Cetamina + Xilazina','Cetamina + Midazolan','Halotano(Gasoso)')
Anestesia=0
while Anestesia==0:
    Anestesia = int(input('Insira uma valor de 1 a 3 para informar os fármacos ANESTÉSICOS: \n 1-Cetamina + Xilazina \n 2-Cetamina + Midazolan \n 3-Halotano(Gasoso) \n'))
    if Anestesia == 1 or Anestesia == 2 or Anestesia == 3:
        print('Você escolheu a opção:',OpAnestesia[Anestesia-1],'\n')
    else:
        print('Digite uma informação válida!! \n')
        Anestesia=0

Peso = int(input('Insira o valor do PESO do animal em kg: \n'))

if Anestesia == 1:
    if Animal == 1 or Animal == 2:
        Cetamina=80*Peso
        Xilazina=15*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Xilazina,'mg de Xilazina \n')
    else: 
        Cetamina=50*Peso
        Xilazina=10*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Xilazina,'mg de Xilazina \n')
elif Anestesia == 2:
    if Animal == 1 or Animal == 2:
        Cetamina=80*Peso
        Midazolan=5*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Midazolan,'mg de Midazolan \n')
    else:
        Cetamina=50*Peso
        Midazolan=2*Peso
        print('Para anestesiar o animal, ministre',Cetamina, 'mg de Cetamina e',Midazolan,'mg de Midazolan \n')   
else:
    print('Para anestesiar o animal, realize a Indução com agente inalatório Halotano em até 5% e Manutenção entre 1 a 3% \n')

print('Após a anestesia, realize o POSICIONAMENTO do animal no estereotáxico. Verifique a angulação da cabeça do animal, a qual deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana. \n')
Posicionamento=0
while Posicionamento==0:
    Posicionamento = int(input('O posicionamento do Animal foi realizado adequadamente? Insira 0 ou 1 para: \n 0 - Animal MAL Posicionado \n 1 - Animal BEM Posicionado \n'))
    if Posicionamento == 1:
        print('Você escolheu realizou o posicionamento do animal adequadamente! \n')
    elif Posicionamento == 0:
        print('Corrija o posicionamento do Animal... \n')
    else:
        print('Digite uma informação válida!! \n')
        Posicionamento=0

print('Realize a LIMPEZA do campo de trabalho. \n')
Limpeza=0
while Limpeza==0:
    Limpeza = int(input('A LIMPEZA do campo de trabalho foi realizada? Insira 0 ou 1 para: \n 0 - Não \n 1 - Sim \n'))
    if Limpeza == 1:
        print('Você realizou a LIMPEZA do campo de trabalho! \n')
    elif Limpeza == 0:
        print('Faça a LIMPEZA do campo de trabalho... \n')
    else:
        print('Digite uma informação válida!! \n')
        Limpeza=0

print('Aplique uma pequena camada de poliacrilato. \n')
CamadaP=0
while CamadaP==0:
    CamadaP = int(input('A aplicação da CAMADA de poliacrilato foi realizada? Insira 0 ou 1 para: \n 0 - Não \n 1 - Sim \n'))
    if CamadaP == 1:
        print('Você realizou a aplicação da CAMADA de poliacrilato! \n')
    elif CamadaP == 0:
        print('Faça a aplicação da CAMADA de poliacrilato... \n')
    else:
        print('Digite uma informação válida!! \n')
        CamadaP=0

print('Determine os pontos para FIXAÇÃO dos parafusos e realize a FIXAÇÃO. \n')
FixaçãoPf=0
while FixaçãoPf==0:
    FixaçãoPf = int(input('A FIXAÇÃO dos parafusos foi realizada? Insira 0 ou 1 para: \n 0 - Não \n 1 - Sim \n'))
    if FixaçãoPf == 1:
        print('Você realizou a FIXAÇÃO dos parafusos! \n')
    elif FixaçãoPf == 0:
        print('Faça a FIXAÇÃO dos parafusos... \n')
    else:
        print('Digite uma informação válida!! \n')
        FixaçãoPf=0

AjusteCoordenadas={}
AjusteCoordenadas['Ajustes'] = {'AP' : 0.42, 'LL' : 0.30, 'DV' : 0.20}
CoordenadasEs={}
CoordenadasEs['HipoCA1'] = {'AP' : float(input('Insira a medida AnteroPosterior (AP) em cm:')), 'LL' : float(input('Insira a medida LateroLateral (LL) em cm:')),'DV' : float(input('Insira a medida DorsoVentral (DV) em cm:'))}
# #CoordenadasEs['Amígdala'] = {'AP' : float(input('Insira a medida AnteroPosterior (AP) em cm:')), 'LL' : float(input('Insira a medida LateroLateral (LL) em cm:')),'DV' : float(input('Insira a medida DorsoVentral (DV) em cm:'))}
# #CoordenadasEs['CortexMotor'] = {'AP' : float(input('Insira a medida AnteroPosterior (AP) em cm:')), 'LL' : float(input('Insira a medida LateroLateral (LL) em cm:')),'DV' : float(input('Insira a medida DorsoVentral (DV) em cm:'))}

AP = CoordenadasEs['HipoCA1'].get('AP')-AjusteCoordenadas['Ajustes'].get('AP')
LL1 = CoordenadasEs['HipoCA1'].get('LL')-AjusteCoordenadas['Ajustes'].get('LL')
LL2 = CoordenadasEs['HipoCA1'].get('LL')+AjusteCoordenadas['Ajustes'].get('LL')
DV = CoordenadasEs['HipoCA1'].get('DV')-AjusteCoordenadas['Ajustes'].get('DV')

print('Valores calculados são:\n AP=',AP,'LL1=',LL1,'LL2=',LL2,'DV=',DV,'\n')

print('Localize os pontos de INSERÇÃO das cânulas-guia, faça os furos. \n')
Inserção=0
while Inserção==0:
    Inserção = int(input('A INSERÇÃO das cânulas-guia foi realizada? Insira 0 ou 1 para: \n 0 - Não \n 1 - Sim \n'))
    if Inserção == 1:
        print('Você realizou a INSERÇÃO das cânulas-guia! \n')
    elif Inserção == 0:
        print('Faça a INSERÇÃO das cânulas-guia... \n')
    else:
        print('Digite uma informação válida!! \n')
        Inserção=0

Escolha=0
while Escolha==0:
    Escolha = int(input('Escolha o Hemisfério do LL. Insira 0 ou 1 para: \n 1 - Direito \n 2 - Esquerdo \n'))
    if Escolha == 1:
        print('Você escolheu o hemisfério Direito! \n')
    elif Escolha == 2:
        print('Você escolheu o hemisfério esquerdo \n')
    else:
        print('Digite uma informação válida!! \n')
        Escolha=0

Ângulo=0
while Ângulo==0:
    Ângulo = int(input('O ÂNGULO de perfuração está adequado? Insira 0 ou 1 para: \n 0 - Não \n 1 - Sim \n'))
    if Ângulo == 1:
        print('Você ajustou o ângulo adequadamente! \n')
    elif Ângulo == 0:
        print('Ajuste o ângulo... \n')
    else:
        print('Digite uma informação válida!! \n')
        Ângulo=0

Final=0
while Final==0:
    Final = int(input('Você realizou as etapas de drenagem e de instalação da segunda cânula? Insira 0 ou 1 para: \n 0 - Não \n 1 - Sim \n'))
    if Final == 1:
        print('Finalize a cirurgia e deixe o animal em repouso isolado! \n')
    elif Final == 0:
        print('Realize as etapas de drenagem e de instalação da segunda cânula... \n')
    else:
        print('Digite uma informação válida!! \n')
        Final=0

print('EXPERIMENTO FINALIZADO!')

#REFERÊNCIA: https://www.ufmg.br/bioetica/cetea/index2.php?option=com_content&do_pdf=1&id=22#:~:text=c)%20Rotule%20com%20a%20informa%C3%A7%C3%A3o,a%20%C2%BD%20da%20dose%20inicial.






















