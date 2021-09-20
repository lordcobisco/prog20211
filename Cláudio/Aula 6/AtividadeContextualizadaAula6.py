print ('Bem vind@ ao automatizador do procedimento cirúrgico!\n')

listasedativos = ['Ketamina', 'Xilazina',[]]

sedacao = int (input ('Qual droga utilizou para sedar o animal? Responda 0 para Ketamina, 1 para Xilazina e 2 para outro.\n'))
print ('Você utilizou:', listasedativos[sedacao])

if listasedativos[sedacao] == listasedativos[0]:
    print ('Esperar 10 minutos para continuar o procedimento.')
elif listasedativos[sedacao] == listasedativos[1]:
    print ('Esperar 5 minutos para continuar o procedimento.')
elif listasedativos[sedacao] != listasedativos[0] and listasedativos[1]:
    print ('Ler a bula do remédio para verificar quanto tmepo é o necessário')

print ('Continue!')

limpezacampo = int (input('O campo está limpo? Responda 0 para não e 1 para sim\n'))

if limpezacampo == 1:
    print('Continue!')
else:
    print('Limpe o campo!')

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
print('Fim do programa!')


