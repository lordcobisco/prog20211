'''
Fundamentos de Programação - IINELS
Atividade Contextualizada 03 - Microscópio Confocal
Nome: Luiz Henrique Bertucci
Site com informações Microscópio https://www.olympus-lifescience.com/pt/laser-scanning/fv3000/#!cms[focus]=cmsContent2543
'''

#Declaração de variáveis 
resolucao = '600x600' # máximo 4000x4000 px
laser_principal = '405' # 405, 488, 561, 640 nm
laser_secundario = '0' # 0, 445, 514 ou 594 nm
metodo_espectral = '50' # 1-100 nm
rotacao_rastreamento = '50' # 0-360 graus
scanner = 'ressonante' #ressonante ou galvanometro
modo_scanner = 'XT' # opções : PT, XT, XZ, XY, XZT e XYZ.
fps_scanner = '30' #10, 20 ou 30 fps
diametro_pinhole = '100' # 50 a 800 um
zoom_optico = '1' # De 1 a 50X
nome = 'usuário'


#Início 
print ('Esse programa tem como objetivo receber parâmetros para a utilização de um microscópio confocal \n')

nome = str(input('Digite seu nome:\n'))
nome = nome.upper()

new_resolucao = str(input('Digite um valor para a resolução, até 4000x4000 pixel:\n')) 
new_laser_principal = str(input('Digite um valor para o laser, entre 405, 488, 561 ou 640 nm:\n'))
new_laser_secundario = str(input('Digite um valor para o laser secunário, entre 0, 445, 514 ou 594 nm:\n'))
new_metodo_espectral = str(input('Digite um valor para o detector espetral entre 1 e 100 nm:\n'))
new_rotacao_rastreamento = str(input('Digite um valor para a rotação de rastreamento entre 0 e 360 graus:\n'))
new_scanner = str(input('Digite o escâner selecionado, ressonante ou galvanometro:\n'))
new_modo_scanner = str(input('Digite o modo do escâner, entre PT, XT, XZ, XY, XZT e XYZ:\n'))
new_fps_scanner = str(input('Digite um valor para de fps o escâner entre 10, 20 ou 30:\n'))
new_diametro_pinhole = str(input('Digite um valor para pinhole, entre 50 e 800 um:\n'))
new_zoom_optico = str(input('Digite um valor de Zoom optico, de 1 a 50x:\n'))

print('\n\n***Lista de variáveis alteradas***\n')
print('Resolução:............', new_resolucao.upper() != resolucao.upper(),'\n') 
print('Laser principal:......', new_laser_principal.upper() != laser_principal.upper(), '\n') 
print('Laser secundário:.....', new_laser_secundario.upper() != laser_secundario.upper(), '\n')
print('Detector espectral:...', new_metodo_espectral.upper() != metodo_espectral.upper(), '\n')  
print('Rotação:..............', new_rotacao_rastreamento.upper() != rotacao_rastreamento.upper(), '\n') 
print('Escâner:..............', new_scanner.upper() != scanner.upper(), '\n') 
print('Modo do escâner:......', new_modo_scanner.upper() != modo_scanner.upper(), '\n') 
print('FPS escâner:..........', new_fps_scanner.upper() != fps_scanner.upper(), '\n') 
print('Diâmetro do pinhole:..', new_diametro_pinhole.upper() != diametro_pinhole.upper(), '\n') 
print('Zoom óptico:..........', new_zoom_optico.upper() != zoom_optico.upper(), '\n\n')

print('\n\n***Parâmetros atualizados***\n')
print('Resolução:............', new_resolucao.upper(),'pixels\n') 
print('Laser principal:......', new_laser_principal.upper(), 'nm\n') 
print('Laser secundário:.....', new_laser_secundario.upper(), 'nm\n')
print('Detector espectral:...', new_metodo_espectral.upper(), 'nm\n')  
print('Rotação:..............', new_rotacao_rastreamento.upper(), '°\n') 
print('Escâner:..............', new_scanner.upper(), '\n') 
print('Modo do escâner:......', new_modo_scanner.upper(), '\n') 
print('FPS escâner:..........', new_fps_scanner.upper(), 'fps\n') 
print('Diâmetro do pinhole:..', new_diametro_pinhole.upper(), 'um\n') 
print('Zoom óptico:..........', new_zoom_optico.upper(), 'x\n\n\n')

print('***Etapa de Calibração***\n')
print('Para calibrar o eixo horizontal, digite a primeira letra do seu nome 10 vezes ')
x1 = input()
x1 = input()
x1 = input()
x1 = input()
x1 = input()
x1 = input()
x1 = input()
x1 = input()
x1 = input()
x1 = input()
print('Agora digite a última letra do seu nome 10 vezes ')
x2= input()
x2= input()
x2= input()
x2= input()
x2= input()
x2= input()
x2= input()
x2= input()
x2= input()
x2= input()
print('Calibração eixo horizontal foi validada?......', x1.upper() == nome[0] and x2.upper() == nome[-1])

print('Para calibrar o eixo vertical, digite a segunda letra do seu nome 10 vezes ')
y1= input()
y1= input()
y1= input()
y1= input()
y1= input()
y1= input()
y1= input()
y1= input()
y1= input()
y1= input()
print('Agora digite e penultima letra do seu nome 10 vezes')
y2= input()
y2= input()
y2= input()
y2= input()
y2= input()
y2= input()
y2= input()
y2= input()
y2= input()
y2= input()
print('Calibração eixo vertical foi validada?......', y1.upper() == nome[1] and y2.upper() == nome[-2])
print('\n\n\n***Parâmetros definidos e calibração realizada***')







