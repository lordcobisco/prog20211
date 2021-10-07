habituação = int(input('O animal está habituado?'))
aprocimação_30cm = int(input(" O animal se aproximou da barra a uma distância menor que 30cm? "))
if aprocimação_30cm:
    print('liberar 0,5ml de rec')
else:
    print('aguardar o animal se aproximar')

animal_tocou_na_barra = int(input("O animal tocou na barra?"))
if animal_tocou_na_barra:
     print('liberar 0,5ml de rec')
else:
    print('aguardar animal tocar na barra')
for i in range(20):
    print("O animal tocou na barra, liberar 0,5ml de rec") 

print("O experimento passou para a próxima etapa")

barraEsquerdaApertada = int(input("O animal tocou na barra esquerda ao ouvir o som1? "))
if barraEsquerdaApertada:
    print('liberar 0,5ml de rec')
else:
    print('Não liberar nada')
barraDireitaApertada = int(input("O animal tocou na barra direita ao ouvir o som2?"))
if barraDireitaApertada:
    print('liberar 0,5ml de rec')
for i in range(50):
    print('O animal tocou em uma das barras, liberar 0,5 de rec')

print('O experimento passou para a próxima fase')