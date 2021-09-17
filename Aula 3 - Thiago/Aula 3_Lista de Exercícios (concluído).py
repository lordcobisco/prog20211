## CRIAÇÃO DO CÓDIGO

# a. Crie as variáveis necessárias para que o programa funcione corretamente.

'''não compreendi a diferença entre essa letra A e as letras B e D. Tirar dúvida com André e executar este comando'''

# b. Inicialize as variáveis com valores padrão adequados.

'''não compreendi a diferença entre essa letra B e as letras A e D. Tirar dúvida com André e executar este comando'''

# c. Crie uma pequena mensagem de apresentação do programa para realizar uma interface com o usuário. Ex.: “Esse programa tem como objetivo receber dados para ...”
print('Este programa tem como objetivo receber dados para gerar imagens de objetos complexos com alta resolução e em formato tridimensional')

# d. Solicite algumas informações necessárias para a configuração de um microscópio dessa
# natureza. Buscar pelo menos 10 itens para essas informações de entrada. Ex.: resolução
# da imagem desejada, tipo de célula a ser escaneada, faixa de iluminação necessária.

Start_position = input("digite a posição inicial dos eixos X e Y: \n")

End_position = input("digite a posição final dos eixos X e Y: \n")

X_Setp = input("digite o valor do passo nos eixos X e Y: \n")

Number_of_surface = input("digite o número de superfícies a serem construídas: \n")

Z_Setp = input("digite o valor do passo no eixo Z: \n")

Number_of_readings = input("digite o número de leituras a serem executadas: \n")

T_Set = input("digite o tempo de integração do espectrômetro: \n")

Detection_WL = input("digite o comprimento de onda a ser detectado: \n")

Plot_style = input("digite o estilo de enredo a ser construído: \n")

Surface_gap = input("digite o valor da distância entre as superfícies: \n")

Confocal_parameter = input("digite o parâmetro confocal a ser utilizado: \n")


# e. Para cada informação digitada, apresente na tela a seguinte mensagem: “Houve alteração na variável inserida? ”. 
# Após a mensagem, apresentar verdadeiro ou falso com base no que foi digitado pelo usuário e o que estava armazenado 
# na variável. Obs.: Não deve ser utilizado if aqui.'''

Alteracao_de_variavel = input("Houve alteração na variável inserida?")
print(Alteracao_de_variavel)

var_logica1 '''com base no que foi digitado pelo usuário e o que estava armazenado na variável'''= True
var_logica2 '''com base no que foi digitado pelo usuário e o que estava armazenado na variável'''= False
print("valor de 'var_logica1 ou var_logica2': ", var_logica1 or var_logica2)

#f. Retorne ao usuário de forma organizada as informações que foram digitadas. Ex.: “As informações de configurações setadas pelo usuário são: ...”

print("o número de superfícies informado foi: %s e o valor da distância entre as superfícies digitado foi %s:" %(Numero_de_Superficies, Valor_do_Passo_no_Eixo_Y)) #ainda não está finalizado, mas a lógica é mais ou menos essa.

# g. Após setada as configurações iniciais o usuário deve utilizar dois caracteres para a calibração do equipamento no sentido horizontal. Para isso, ele deve apertar a tecla
#correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.

Nome_Usuario = input("Digite o seu nome")
print(Nome_Usuario)
Nome_Usuario[0]


'''1''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False
    
'''2''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''3''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''4''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''5''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''6''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''7''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''8''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''9''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False

'''10''' Calibracao_do_equipamento_horizontal = input("Digite a primeira letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [0] = True
                      != [0] = False
            
            
'''1''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''2''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''3''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False

'''4''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''5''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''6''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''7''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''8''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''9''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False
            
'''10''' Calibracao_do_equipamento_horizontal = input("Digite a última letra do seu nome: \n")
         print(Calibracao_do_equipamento_horizontal)
         Nome_Usuario == [-1] = True
                      != [-1] = False



# h. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação 
# foi corretamente digitada e mostrar o caractere pressionado.

print(Nome_Usuario == [-1],'A informação foi corretamente digitada')


#i. Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento 
# no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda letra do
# seu nome 10x e à penúltima letra do seu nome 10x.


'''1''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''2''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''3''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''4''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''5''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''6''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''7''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''8''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''9''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False

'''10''' Calibracao_do_equipamento_vertical = input("Digite a segunda letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [1] = True
                      != [1] = False



'''1''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''2''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''3''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''4''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''5''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''6''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''7''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''8''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''9''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False

'''10''' Calibracao_do_equipamento_vertical = input("Digite a penúltima letra do seu nome: \n")
         print(Calibracao_do_equipamento_vertical)
         Nome_Usuario == [-2] = True
                      != [-2] = False


#j. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
# foi corretamente digitada e mostrar o caractere pressionado.

print(Nome_Usuario == [-2],'A informação foi corretamente digitada')

#k. Finalmente, o programa deverá apresentar na tela que houve o término da calibração do sistema.

print('A calibração do sistema foi finalizada com sucesso')

#l. Para verificar que o programa está funcionando corretamente, execute-o colocando um 
# breakpoint na linha 15. Tire um print da tela mostrando a linha parada e as informações
# armazenadas nas variáveis até então.
