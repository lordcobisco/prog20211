# Variáveis
Anestésicos = ['Ketamina'],['xilazina']
Anestésicos1 = {'halotano'}
print("Opções de anestésicos:",Anestésicos,Anestésicos1)


print("Seja bem-vindo ao programa automatizado de cirurgia estereotáxica para pequenos animais")
NomeCirurgiao = input("Digite seu nome:\n")
DtaCirurgia = input("Digite a data da cirurgia:\n")
ModeloAnimal = input("Qual o modelo animal?\n")

print("Passo 1: Aplique a anestesia no animal.")

Anestésicos1 = (int(input("Quando o efeito do analgésico inicar, digite 1:\n")))
if Anestésicos1 == 1:
    print("Passo 2: Posicione o animal no estereotáxico.")

Posicionamento = (int(input("Quando posicioná-lo, digite 2:\n")))
if Posicionamento == 2:
    print("Passo 3: Agora posicione as barras de suporte de peso no ouvido externo do animal.")

LevePiscada = (int(input("Quando concluir, digite 3:\n")))
if LevePiscada == 3:
    print("Passo 4: Verifique a angulação da cabeça do animal, a qual deve estar sem diferenças entre o bregma e o lambda, para ter uma superfície de cirurgia plana.")

AngulacaoCabeca = (int(input("Quando finalizar, digite 4:\n")))
if AngulacaoCabeca == 4:
    print("Passo 5: Retire a pelagem que recobre a parte superior da calota craniana.")

RetiradaTecidosMoles = (int(input("Quando retirar, digite 5:\n")))
if RetiradaTecidosMoles == 5:
    print("Passo 6: Retire os tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana.") 

LimpezaCalotaCraniana = (int(input("Quando retirar, digite 6:\n")))
if LimpezaCalotaCraniana == 6:
    print("Passo 7: Limpe a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H 2 O 2 10 volumes.")  

Poliacrilato = (int(input("Quando Limpar, digite 7:\n")))
if Poliacrilato == 7:
    print("Passo 8: Utilize uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.") 
    print("Cuidado para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.")

Poliacrilato = (int(input("Quando concluir, digite 8:\n")))
if Poliacrilato == 8:
    print("Passo 9: Posicione a agulha (devidamente preparada para o tamanho da cânula e que servirá de suporte para a fixação das cânulas) sobre o bregma.")

PosicionamentoAgulha = (int(input("Quando posicionar, digite 9:\n")))
if PosicionamentoAgulha == 9:
    print("Passo 10: Calcule o posicionamento AnteroPosterior (AP), LateroLateral (LL) e DorsoVentral (DV).")

CalculoPosicionamento = (int(input("Quando calcular, digite 10:\n")))
if CalculoPosicionamento == 10:
    print("Passo 11: Calcule os valores encontrados nas réguas a partir do posicionamento da agulha.")

AgulhaBregma = (int(input("Quando calcular, digite 11:\n")))
if AgulhaBregma == 11:
    print("Passo 12: Localize os pontos de inserção das cânulas-guia.")

PontosInsercao = (int(input("Quando localizar, digite 12:\n")))
if PontosInsercao == 12:
    print("Passo 13: De acordo com os valores encontrados nos cálculos AnteroPosterior (6,00) e LateroLateral (3,63 e 3,03), faça furos para a introdução das cânulas-guia.")
    print("A não perfuração das meninges é o procedimento ideal, e para conseguir isso apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +- 45 0 de angulação.")

Furos = (int(input("Quando fizer os furos, digite 13:\n")))
if Furos == 13:
    print("Passo 14: Introduza a cânula-guia previamente confeccionada até o valor DorsoVentral (4,00) que foi calculado anteriormente.")

IntroducaoCanulaGuia = (int(input("Quando introduzir, digite 14:\n")))
if IntroducaoCanulaGuia == 14:
    print("Passo 15: Drene qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio, utilizando pequenos rolos de papel absorvente.")

Drenagem = (int(input("Quando a drenagem estiver concluída, digite 15:\n")))
if Drenagem == 15:
    print("Passo 16: Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável \n(o ideal é que a mistura seja capaz de cobrir a parte desejada sem escorrer por todo o crânio).")

MisturaExpessa = (int(input("Quando a mistura ficar espessa e maleável, digite 16:\n")))
if MisturaExpessa == 16:
    print("Passo 17: Fixe a outra cânula-guia, levantando levemente o braço do estereotáxico cuidando para que a cânula-guia previamente fixada não se movimente.")

FixacaoCanula2 = (int(input("Quando fixar, digite 17:\n")))
if FixacaoCanula2 == 17:
    print("Passo 18: Posicione a agulha sobre o outro ponto de inserção da cânula-guia e introduza a cânula-guia até o valor DV (4,00) calculado previamente.")

PosicaoEIntroducaoAgulha = (int(input("Quando posicionar, digite 18:\n")))
if PosicaoEIntroducaoAgulha == 18:
    print("Passo 19: Siga novamente a descrição do item 9 e após fixar a cânula conforme item 10.")###########################

EspalharCimento = (int(input("Após repetir estes passos, digite 19:\n")))
if EspalharCimento == 19:
    print("Passo 20: Espalhe o cimento sobre a maior área do crânio, sempre deixando um espaço entre o capacete e o início da área tecidual. \nEste cuidado previne de um futuro descolamento do capacete devido a entrada de sangue ou outro líquido entre o capacete e o crânio.")

Confirmacao_ = (int(input("Após espalhar o cimento, digite 20:\n")))
if Confirmacao_ == 20:
    print("Levante bem devagar seguindo as instruções do item contida no item 11.")######################
    print("Acomode o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados.")
    print("Assim que o animal despertar, coloque-o de volta a sua caixa-moradia.")

print("Fim de Programa")

