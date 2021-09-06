# def nomeFuncao(entrada1_opicional=1, entrada2_opicional=5):
#     '''
#     Essa função ...........
#     '''
#     return entrada1_opicional,entrada2_opicional

# retornoFunção = (nomeFuncao(1,2))
# print (retornoFunção[1])

# retornoFunção1,retornoFunção2 = (nomeFuncao(1,2))
# print (retornoFunção1,retornoFunção2)

# retornoFunção = (nomeFuncao(([1,2],[1,2])),'a')
# print (retornoFunção[0])

# retornoFunção = nomeFuncao (entrada2_opicional=[1,2,3,4,5,6])
# print(retornoFunção)

# def mensagem_de_erro():
#     '''Esta função não retorna nada, não tem parametros de entrada, 
#     meu único objetivo é apresentar um erro na tela quando acontecer
#     alguma coisa'''
#     print('Deu erro meu fi!!')

# erro = bool (int (input('Deu erro?')))
#     if erro == True:
#         mensagem_de_erro()

# def low_pass_filter (raw_data, filter_parameter = 0.1):
#     filtered_data = []
#     for i in range(len(raw_data)):
#         if i == 0:
#             filtered_data.append(raw_data[i])
#         else:
#             filtered_data.append(filtered_data[i-1] + filter_parameter*(raw_data[i] - filtered_data[i-1]))

#     return filtered_data
# print (low_pass_filter([1,2,3,4,5,6,7,8,9,10]))

# def funçãoRecursiva(k):
#     if (k>0):
#         result = k + funçãoRecursiva (k-1)
#         print(result)
#     else:
#         result = 0
#     return result
#f1->f2->f3->f4->f5->f6
# print(funçãoRecursiva(6))

