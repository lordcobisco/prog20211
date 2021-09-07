# Essa é a primeira atividade. Meu primeiro programa *-*
# Esse ícone designa um comentário. 

''' 
Registrando a maneira de registrar um bloco de comentário.
São as três aspas simples em sequência.
Neste caso, tudo que estiver entre as aspas será um comentário, sem limite de linhas.
Tudo que esta registrado como comentário não é executado como parte do programa.

Use comentários para explicar seu código e torna-lo compreensível para outros 
desenvolvedores que irão trabalhar com você e para ajudar você  a lembrar de algumas funções 
que você fez no seu proprio código.
'''

print ('Hello World')
print ('Qualquer texto ou elemento')

IssoEUmaString = "Qualquer coisa entre aspas duplas"
NaoENumeroESimString = "15"

# Mesmo que seja um número, se vier entre aspas (simples ou dupla) é considerado um string.

IstoEUmInteiro = 15
IssoEUmNumeroReal = 15.3
IssoEUmBooleano = True

print (IssoEUmaString,NaoENumeroESimString, IstoEUmInteiro,IssoEUmNumeroReal,IssoEUmBooleano)

print(type(IssoEUmaString))
print(type(IssoEUmNumeroReal))

''' 
As palavras reservadas do Python são espécies de funções e/ou instruções padronizadas que podemos 
utilizar na escrita do código. 
Como True e False 
'''


'''
ATENÇÃO - IMPORTANTE:
Por padrão, o python não associa/chama automaticamente funcionalidades (e/ou bibliotecas) 
que não são básicas. Como por exemplo: Ferramenta para plot de gráficos e cálculos matemáticos
complexos. 

IMPORT - Função utilizada para importar funcionalidades adjacentes que se 
fazem necessárias em determinado momento. Como por exemplo: math - evoca uma biblioteca de funções 
matemáticas complexas tipo seno cosseno, tangente, fatorial etc.
'''
# Exemplo teste:

import math

print('A raiz quadrada de 100 é: ', math.sqrt(100))
print(math.sqrt(IssoEUmNumeroReal))

'''
É possivel escolher importar apenas uma parte da biblioteca que desejamos utilizar.
Fazemos isso utilizando a função FROM    IMPORT
'''
# Exemplo teste2:

from math import sqrt

# Uando apenas o IMPORT fica assim: print('A raiz quadrada de 100 é: ', math.sqrt(100))
# Dessa forma, omitimos o math. antes do sqrt.

print('A raiz quadrada de 100 é: ',sqrt(100))


# Continuar a parti de Operadores de atribuição e aritmética. 3h4min22s da aula do dia 17/08

