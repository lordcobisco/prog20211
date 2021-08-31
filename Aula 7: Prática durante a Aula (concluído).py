

# FASE DE CRIAÇÃO/DECLARAÇÃO DA FUNÇÃO (NOME, ENTRADA, SAÍDAS E O QUE ELA VAI FAZER).

def nomeFuncao(entrada1_opcional, entrada2_opcional): #def quer dizer definindo uma função. tem que tem um nome da função também. (nomeFuncao) o nome da função dev seguir o mesmo padrão. o i
  '''
  Essa função...
  '''
  return variavel1_opcional,variavel2_opcional

# FASE DE UTILIZAÇÃO

print(nomeFuncao(1,2)) #retorna a variável em forma de uma tupla.

#ou 

retornoFunção = (nomeFuncao[1])
print(retornoFunção)

#ou

retornoFunção1,retornoFunção2 = nomeFuncao(1,2)
print(retornoFunção1,retornoFunção2)


retornoFunção = (nomeFuncao (([1,2],[1,2])), 'a')
print(retornoFunção[0])

retornoFunção = nomeFuncao (entrada2_opcional=[1,2,3,4,5,6])
print(retornoFunção[0])

def mensagem_de_erro():
''' Esta função não retorna nada, não tem parâmetros de entrada,
meu único objetivo é apresentar eero na tela quando acontecer alguma coisa'''
print('deu erro')

erro = bool(int(input('Deu erro')))
if mensagem_de_erro == true:
  mensagem_de_erro()

  
def low_pass_filter(raw_data,filter_parameter = 0.1):
  filtered_data = []
  for i in range (len(raw_data)):
    if i == 0:
      filtered_data.append(raw_data[])
    else:
      filtered_data.append(
        filtered_dataraw_data[i+1] + filtered_dataraw*(raw_data[1] - diltered_data [i-1]))
  return filtered_data
  
print(low_pass_filter([1,2,3,4,5,6,7,8,9,10]))


# y = y +h*(u-y): não lembro que comando é esse.

raw_data = [1,2,3,4,5,6,7,8,9,10]
print(low_pass_filter(raw_data))

# Exemplo incompleto do slide
def tri_recursion(k):
  if (k>0):
    Result = k+tri_recursion(k-1)
    print(result)

#Exemplo escrito pelo professor
def funçãoRecursiva(k):
  if (k>0):
    result = k + funçãoRecursiva(k+1)
    print(result)
  else:
    result = 0
  return result
#f1->f2->f3->f4->f5->f6
print(funçãoRecursiva(6))
  


