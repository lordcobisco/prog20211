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


# Continuar a parti de Operadores de atribuição e aritmética. 3h4min22s da aula do dia 17/08 - OK

ResultadoSoma = 3+5 # Soma
print(ResultadoSoma)
print(2-3,6*5,8/2) # Subtração, Multiplicação, Divisão
print(2**10) # Exponenciação
print(10//9,7//2) # Selecionar apenas a parte inteira da divisão
print(11%10,7%2) # Selecionar apenas o resto da divisão

# É possível utilizar argumentadores compostos, ou seja, que compreendem mais de uma operação no mesmo símbolo.
# Exemplo:

soma = 0
soma += 3 # Significa que: soma = soma + 3

print(soma); soma = soma+3; print(soma)

'''
Aplicação dos operadores compostos: É utilizado, por exemplo, para aplicação em filtros. Filtros utilizam soma cumulativa.
Integral numérica (utiliza soma cumulativa).
É possível fazer a composição de operadores para todas as operações matemáticas.
'''

divisão = 100
divisão /= 3; print(divisão); divisão = divisão/3; print(divisão)

subtração = 0
subtração -= 3; print(subtração); subtração = subtração-3; print(subtração)

multiplicação = 1
multiplicação *= 3; print(multiplicação); multiplicação = multiplicação*3; print(multiplicação)

# Também é possível realizar atribuições compostas:
# Exemplo:
a,b,c = 1,2,3
print(a,b,c)

'''
Outro tipo de variável que é possível ser declarada de forma composta, são as chamadas TUPLA.
Esses elementos nao são classificados como números inteiros nem reais, são TUPLAS.
Elas devem ser escritas entre parêntese, EX: (x,y) = (1,2).
É Muito útil na manipulação de vetores para fazer acesso.
'''

# Os operadores mostrados até agora, são chamados de aritméticos, pois expressam operações aritméticas.

# Os outros tipos de operadores são chamados de lógicos ou relacionais.
# Representam operadores lógicos do tipo, sim e não, falso e verdadeiro, etc.
# Exemplo:

parede = "Branca"
parede2 = "Preto"

# Quando utilizo dois iguais - == - estou fazendo uma pergunta lógica.
# Quando utilizo apenas um igual - = - estou realizando uma atribuição, 
# ou seja, dizendo que determinada coisa é igual a outra. Como quando declaro o valor de uma variável.

print(parede == "Branca") # Neste exemplo a pergunta é: A parede é branca?
print(parede != "Branca") # Neste exemplo a pergunta é: A parede é diferente de branca?
print(not(parede == "Branca")) # Neste exemplo a pergunta é: A parede não é branca?

print(not(parede == "Branca") & (parede == "Branca")) 

'''
No exemplo a cima, a pergunta é: A parede não é branca e branca?
Poderia ser outra cor também - No caso de utilizar o argumentador E (& ou AND), 
só basta que um dos elemento seja falso para que toda a operação seja falsa.
'''

print(not(parede == "Branca") | (parede == "Branca"))
'''
No exemplo a cima, a pergunta é: A parede não é branca ou branca?
No caso de utilizar o argumentador OU (| ou OR), só basta que um dos elementos seja verdadeiro
para que toda a operação seja verdadeira.
'''

# Para o resultado das operações lógicas utilizamos a Tabela Verdade. 

'''
Operações lógicas são realizadas atraves da comparação de elementos, seja na relação de:
== igual; != diferente, > maior; < menor; >= maior ou igual; <= menor ou igual.
Exemplos:
'''
print(2<3, 4>5, 2<=3, 4>=5, 2==3, 4!=5) # O resultado dessas operações serão valores lógicos de falso ou verdadeiro.

# ATIVIDADE - Índice de Massa Corporal - IMC

peso = 64
altura = 1.73
IMC = peso/altura**altura 

print(IMC)

'''
Deu errado - Só deu certo o MuitoBaixoPeso
MuitoBaixoPeso = "<17"
AbaixoDoPeso = ">17.1 and <18.5"
PesoNormal = ">18.6 and <25"
AcimaDoPeso = ">25 and <30"
MuitoSobrepeso = ">30"
'''

'''
Deu arrado
MuitoBaixoPeso = "<17"
AbaixoDoPeso = "<18.5"
PesoNormal = (<25)
AcimaDoPeso = "<30"
MuitoSobrepeso = ">30"
'''

#print(IMC == "<17", ">17.1 and <18.5", ">18.6 and <25", ">25 and <30", ">30") - Errado!


'''
Errado!
print(IMC == AbaixoDoPeso)
print(IMC == PesoNormal)
print(IMC == AcimaDoPeso)
print(IMC == MuitoSobrepeso
'''

# Agora deu certo! *-*
print(IMC <= 17)
print(IMC <= 18.5)
print(IMC <= 25)
print((IMC >= 25) & (IMC <= 30))
print(IMC >= 30)

# Entrada e saída de dados:

# Peso = input("Digite o seu peso: ") # Input sempre retorna em formato de string.
# É preciso converter o string para inteiro. Para isso, utiliza a função FLOAT

nome = input("Digite seu nome: ")
Peso = float(input("Digite o seu peso: "))

print(nome, ", seu peso é: ", peso)