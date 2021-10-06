# Nada que for colocado aqui aparecerá no programa
# Nem será utilizado por ele

print("Hello World!")

'''
Nada que for colocado aqui aparecerá no programa
Nem será utilizado por ele
'''

#######################

num = input("Digite um número: ")
print(num)

login = input("Login: ")
senha = input("Senha: ")
print("O usuário informado foi: %s, e a senha digitada foi: %s." %(login, senha))

#######################

# Atribuição e operadores aritméticos

resultadoSoma = 12+55 #Atribuição
print(resultadoSoma)

print(12+55) #Soma

print(12-55) #Subtração

print(10*55) #Multiplicação

print(55/5) #Divisão

print(12**2) #Exponenciação

print(55//7) #Parte inteira da divisão

print(55%7) #Resto da divisão

# Operadores compostos

maisIgual, menosIgual, vezesIgual, divididoIgual, moduloIgual = 20

maisIgual += 4
menosIgual -= 4
vezesIgual *= 4
divididoIgual /= 4
moduloIgual %= 3

x,y,z = 3,6,9
x,y,z = x*3,x+y+z,x*y*z

(a, b) = (2, 3)

# Expressões lógicas e operadores relacionais

varLogica = True
print("Valor de 'not varLogica': ",not varLogica)

varLogica1 = True
varLogica2 = False
print("Valor de 'varLogica1 e varLogica2: ",varLogica1 and varLogica2)
print("Valor de 'varLogica1 ou varLogica2: ",varLogica1 or varLogica2)

print(3==3)
print(3!=3)
print(3>3)
print(3<3)
print(3>=3)
print(3<=3)

#####################

# Variáveis

varString = "Souvenir Zalla"
print(varString)
print(type(varString))

varInt = 25
print(varInt)
print(type(varInt))

varFloat = 5.96
print(varFloat)
print(type(varFloat))

varBool = True
print(varBool)
print(type(varBool))

# Importando módulos

import math
print(math.sqrt(25))

from math import sqrt
print(sqrt(25))
