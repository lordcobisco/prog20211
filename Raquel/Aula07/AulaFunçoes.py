# def nomeFunção definir a função

def nomeFuncao(entrada1_opcinal,enrada2_opcional): 
    '''
    Essa função ...
    '''
#
    return entrada1_opcinal,enrada2_opcional

#criando função corretamente

retornoFunção = (nomeFuncao([1,2,3],3,3))
print (retornoFunção[0])

retornoFunção1, retornoFunção2 = nomeFuncao(1,2)
print(retornoFunção1,retornoFunção2)

retornoFunção = (nomeFuncao([1,2],2))
print(retornoFunção[0])

retornoFunção =  nomeFuncao (entrada2_opcional=[1,2,3,4,5,6])
print(retornoFunção)

def mensagemDeErro ():
    '''Esta função não retorna nada, não tem parâmento de entrada
    meu unico objetivo é apresentar um erro na tela quando acontecer
    alguma coisa '''
print ('deu erro meu')

erro = bool(int(input('deu erro?')))
if erro == True:
    mensagemDeErro()

def low_pass_filter (raw_data,filter_parameter = 0.1):
    if type(raw_data)!= type([]):
        mensagemDeErro()
    filtered_data = []
    for i in range(len (raw_data)):
        if i == 0:
            filtered_data.append (raw_data [i])
        else:
            filtered_data.append(
                filtered_data[i -1] +filter_parameter*(raw_data[i])
                                                -filtered_data[i-1])
    return filtered_data

              

raw_data = [1,2,3,4,5,6,7,8,9,10]
print (low_pass_filter(raw_data))    

def funçãoRecursiva(k):
    if (k>0):
        result = k + funçãoRecursiva(k-1)
        print(result)
    else:
        result = 0
    return result 
#f1->f2->f3->f4->f5->f6   #sem usar for
print(funçãoRecursiva(6))
