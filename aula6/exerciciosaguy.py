perguntas = [
    " O rato está habituado? (s/n)",
    "O animal tocou na barra 20x? (s/n)",
    "O som1 foi emitido e o animal tocou na basimrra esquerda? (s/n)",
    "O som2 foi emitido e o animal tocou na barra direita? (s/n)",
    " O experimento foi realizado 50x em 30 minutos? (s/n)",
    "Passar para a próxima fase do experimento? (s/n)"
]
for x in range(len(perguntas)):
    print(perguntas[x])
    c = input()
    if c == 's':
        continue
    else:
        print('Repita o experimento')
        break