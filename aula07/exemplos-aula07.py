# Funcoes
#'''
#def nomeFuncao(entrada1_opicional, entrada2_opicional): 

#    '''

    #Essa funcao...

  #  '''

    #

 #   return entrada1_opicional, entrada2_opicional
#
#retornoFuncao = (nomeFuncao([1,2],[2,2], 'a'))
#print(retornoFuncao[0], retornoFuncao[1])
#print(retornoFuncao)
#
#retornoFuncao = nomeFuncao(entrada2_opicional=[1,2,3,4,5,6])
#print(retornoFuncao)
#'''
#


def mensagemERRO():

    '''
    #nao tem retorna nada, nao tem parametros de entrada
   #o unico objetivo de apresentar um erro na tela quando acontecer
    #alguma coisa

    '''

    print('Deu erro, meu fi!!! ')

#erro = bool(int(input('Deu erro?\n')))

#if erro == True:
 #  mensagemERRO()


#def low_pass_filter(raw_data, filter_parameter = 0.1):

 #   filtered_data = []
  #  for i in range(len(raw_data)):
   #     if i == 0:
    #        filtered_data.append(raw_data[i])

     #   else:
      #      filtered_data.append(filtered_data[i-1]+ filter_parameter*(raw_data[i] - filtered_data[i-1])) 


    #return filtered_data
 
#print(low_pass_filter([1,2,4,5,6,7,8,9,10]))

# y = y + h*(u-y)


#raw_data = [1,2,3,4,5,6,7,8,9,10]
#print(low_pass_filter(raw_data))


def funcaoRecursiva(k):
    if k>0:
        result = k + funcaoRecursiva(k-1)
        print(result)

    else:
        result = 0
    return result

#f1 -> f2 -> f3 -> f4 -> f5 -> f6

print(funcaoRecursiva(6))