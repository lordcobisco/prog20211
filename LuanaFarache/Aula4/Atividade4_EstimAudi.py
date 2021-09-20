'''
O presente programa tem por objetivo sistematizar um método de discriminação 
de estímulos auditivos para primatas através do condicionamento operante.
'''

Habituação = input("O animal esta habituado ao estímulo? Digite 1 para Sim e 0 para Não \n")

# 1. Inicialização do programa - HABITUAÇÃO:
if Habituação == 1:
    print("Programa iniciado!\n")
elif Habituação == 0:
    print("Realize a habituação do animal antes de iniciar o programa!\n")

Aproximação = float(input("A que distância esta o animal? \n"))
Aproximação1 = 30
ToqueBarra = int(input("Quantas vezes o animal tocou a barra? \n"))

# 2. Regime de APROXIMAÇÕES SUCESSIVAS: 
if Aproximação < Aproximação1:
    print("0,5ML de recompensa foi liberada!\n")

if ToqueBarra == 20:
    print("O experimento passou para a próxima etapa!\n")
elif ToqueBarra < 20:
    print("São necessários 20 toques na barra para passar para a etapa seguinte!\n")
else:
    print("Algo deu errado! A barra parece estar com problema\n")

# Associação entre estímulo sonoro e toque na barra:
Som1 = int(input("O som 1 foi emitido? Digite 1 para Sim e 0 para Não \n"))
Som2 = int(input("O som 2 foi emitido? Digite 1 para Sim e 0 para Não \n"))
BarraEsquerda = input("O animal tocou a barra ESQUERDA? Digite 1 para Sim e 0 para Não \n")
BarraDireita = input("O animal tocou a barra DIREITA? Digite 1 para Sim e 0 para Não \n")

if Som1 and BarraEsquerda:
    print("0,5ML de recompensa foi liberada!\n")
elif not Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif not Som1 and BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")
elif Som1 and not BarraEsquerda:
    print("A recompensa não pode ser liberada!\n")

if Som2 and BarraDireita:
    print("0,5ML de recompensa foi liberada!\n")
elif not Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif not Som2 and BarraDireita:
    print("A recompensa não pode ser liberada!\n")
elif Som2 and not BarraDireita:
    print("A recompensa não pode ser liberada!\n")

QuantidadeExperimentos = int(input("Quantas vezes o experimento foi realizado? \n"))
QuantidadeExperimentos1 = 50
TempoExperimento = int(input("Qual o tempo de duração do experimento? \n"))
TempoExperimento1 = 30

if (QuantidadeExperimentos == QuantidadeExperimentos1) and (TempoExperimento == TempoExperimento1):
    print("O experimento passou para a próxima etapa!\n")
elif (QuantidadeExperimentos > QuantidadeExperimentos1) and (TempoExperimento > TempoExperimento1):
    print("O experimento não poderá seguir para a proxima fase! \n")
elif (QuantidadeExperimentos <= QuantidadeExperimentos1) and (not (TempoExperimento <= TempoExperimento1)):
    print("O experimento não poderá seguir para a proxima fase! \n")
elif (not(QuantidadeExperimentos <= QuantidadeExperimentos1)) and (TempoExperimento <= TempoExperimento1):
    print("O experimento não poderá seguir para a proxima fase! \n")

print("Experimento finalizado!\n")
print("Fim do programa!")