# Atividade Contextualizada da Aula - 06

#Programa para Cirurgia esterotáxica em animais

print('Bem-vindo(a) ao programa de cirurgia estereotáxica em animais.')
print('')
print('Este programa irá automatizar e auxiliar no procedimento cirúrgico.\n', 'Por favor, responda todas as perguntas da forma que são solicitdas. \n')

resp = input('Vamos começar a operação? Responda "sim" para continuar.\n')

# Anestesia
listasdeAnestesia = ['Ketamina', 'Xilazina',[]]

sedacao = int (input ('Qual fármaco vai ultilizar para sedar o animal? Responda 0 para Ketamina, 1 para Xilazina e 2 para outro.\n'))
print ('Você utilizou:', listasdeAnestesia[sedacao])

if listasdeAnestesia[sedacao] == listasdeAnestesia[0]:
    print ('Esperar 15 minutos para continuar o procedimento.')
elif listasdeAnestesia[sedacao] == listasdeAnestesia[1]:
    print ('Esperar 5 minutos para continuar o procedimento.')
elif listasdeAnestesia[sedacao] != listasdeAnestesia[0] and listasdeAnestesia[1]:
    print ('Ler a bula do remédio para verificar quanto tempo é o necessário')

print ('Continue!')

print('Nesta etapa iremos realizar a limpeza do campo de trabalho.\n')

limpezacampo = int (input('O campo está limpo? Responda 0 para não e 1 para sim\n'))

if limpezacampo == 1:
    print('Continue!')
else:
    print('Limpe o campo!')



# configura os eixos

print ('Agora configure os eixos.')

eixoX = int( input ('Qual o eixo X desejado?\n'))
eixoY = int ( input ('Qual o eixo Y desejado?\n'))
eixoZ = int ( input ('Qual o eixo Z desejado?\n'))

dicionarioDeValoresPadrão = {'eixoX':[6], 'eixoY':[7],'eixoZ':[5]}
listaComValoresInputados = [eixoX,eixoY, eixoZ]
tuplaComValoresInputados = (eixoX,eixoY, eixoZ)

print ('Seu eixo X escolhido é:', eixoX)
print ('Seu eixo Y escolhido é:', eixoY)
print ('Seu eixo Z escolhido é:', eixoZ)

eixoAjustado = 0

while eixoAjustado == 0:
    print ('Continue ajustando!')
    eixoAjustado = int (input ('Todos os eixos estão ajustados? Responda 0 para não  e 1 para sim\n'))

for x in dicionarioDeValoresPadrão['eixoX']:
    print ('O valor padrão para o eixoX é', x)
    
for y in dicionarioDeValoresPadrão['eixoY']:
    print ('O valor padrão para o eixoY é', y)

for z in dicionarioDeValoresPadrão['eixoZ']:
    print ('O valor padrão para o eixoZ é', z)

print ('Pode continuar a cirurgia!')
print('Fim do procedimento!')
print('fim do programa')