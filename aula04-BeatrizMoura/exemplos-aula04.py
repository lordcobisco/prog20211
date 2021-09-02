
# ---------- Exercicio do botao -------------

#botao1on = int (input('O rato apertou o botao 1?\n'))
#botao2on = int (input('O rato apertou o botao 2?\n'))

#if botao1on and (not botao2on):
#    print('Foram adicionados 10mg de acucar')

# ---------------- Exercicio do Preguicoso/Inteligente ----------------

#preguicoso = input('Voce eh preguicoso?\n')
#inteligente = input('Voce eh inteligente?\n')

#if preguicoso == 's' and inteligente == 's':
#    print('Voce eh preguicoso e inteligente')

#elif preguicoso == 's' and inteligente == 'n':
 #   print('Voce eh preguicoso e nao eh inteligente')

#elif preguicoso == 'n' and inteligente == 's':
 #   print('Voce nao eh preguicoso e eh inteligente')


#elif preguicoso == 'n' and inteligente == 'n':
 #   print('Voce nao eh preguicoso e nao eh inteligente')

  #  print('programa encerrado')

# ----------------- Exercicio do Numero Menor ------------------

#numenoMenor = int (input('Digite um numero menor que 5:\n'))

#if numenoMenor < 5:
#    print('O numero digitado eh menor que 5')
#else:
#    print('Voce digitou um numero acima de 5')
#print('fim do programa')

# ---------- Exercicio de Acao ------------------

#print('Esse eh o numero de selecao para o seu programa de processamento de dados\n')

#acao = int(input('Digite 1 para entrar na opcao de Insercao de Dados e 2 para Processamento de Dados \n'))

#if acao == 1:
 #   print('Voce selecionou a opcao de upload')
#elif acao == 2:
 #   print ('Voce selecionou a opcao de processamento')
#else:
 #   print('Voce selecionou uma opcao invalida')
#print('Fim do programa')

# --------- Botao ON ou OFF ----------------------------

botao1on = int (input('O rato apertou o botao 1?\n'))
botao2on = int (input('O rato apertou o botao 2?\n'))

if botao1on and not botao2on:
    print('Foram adicionados 10mg de comida')
elif not botao1on and botao2on:
    print('Foram adicionados 20mg de comida')
elif not botao1on and not botao2on:
    print('Sem comida')
else:
    print('Os botoes apresentam problemas')
print(' fim do programa')