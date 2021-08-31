# EXERCÍCIO 1:
# não pode usar se e senão. tem qque escrever todas as possibilidades. fazer operação lógica para a primeira, segunda, terceira e assim sucessivamente. A resposta tem que 
#ser verdadeiro ou falso.
#Somente mostrar true e false (sem estrutura de decisão)

Peso = float(input("digite seu peso\n")) #float: é usada para informar ao programa que está é uma variável do tipo real; input: é usada para inserir dados.
Altura = float(input("digite sua altura\n")) #float: é usada para informar ao programa que está é uma variável do tipo real; input: é usada para inserir dados.
IMC = peso/pow(altura,2) #pow é utilizada para retornar o valor elevado ao expoente.

# Muito abaixo do peso quando imc menor que 17
IMC<17 = True (input("Muito abaixo do peso\n"))
IMC>17 = False
print("valor de 'IMC<17 ou IMC>17':", IMC<17 or IMC>17)

# Abaixo do peso quando imc menor que 17 e 18.5
IMC<17 and 18.5 = True (input("Abaixo do peso\n"))
IMC>17 and 18.5 = False
p
rint("valor de 'IMC<17 ou IMC>17':", IMC<17 and 18.5 or IMC>17 and 18.5)

# Peso dentro do normal quando imc entre 18.5 e 25.0
IMC<18.5 and 25 = True (input("Dentro do peso normal\n"))
IMC>18.5 and 25 = False
print("valor de 'IMC<18.5 and 25 ou IMC>18.5 and 25':", IMC<18.5 and 25 or IMC>18.5 and 25)

# Acima do peso normal quando imc entre 25 e 30
IMC<25 and 30 = True (input("Acima do peso normal\n"))
IMC>25 and 30 = False
print("valor de 'IMC<25 and 30 ou IMC>25 and 30':", IMC<25 and 30 or IMC>25 and 30)

# Muito acima do peso normal quando imc acima de 30
IMC>30 = True (input("Muito acima do peso normal\n"))
IMC<30= False
print("valor de 'IMC>30 ou IMC<30':", IMC>30 or IMC<30)



# EXERCÍCIO 1:

Inclua no exercício de IMC uma atualização:
Requisito:
Receber o IMC utilizando a função input

















