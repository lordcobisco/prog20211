comando=1
print('\n')
while(comando==1):
    textoSemFormatacao=str(input("Insira O texto: \n"))
    textoComFormatacao= textoSemFormatacao.replace(';',',').replace(' ','')
    
    print('\n')
    print(textoComFormatacao)
    comando = int(input('Continuar Digite 1: \n'))
    if (comando == 1):
        comando=1
    else:
        comando=0
    