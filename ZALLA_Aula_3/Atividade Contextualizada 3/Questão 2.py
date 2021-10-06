# Inicialização e configuração do equipamento

tipoDeCelula_anterior = "procarionte"
faixaDeIlum_anterior = 488
intensidade_anterior = 0.25
objetiva_anterior = 20
diametroDoPonto_anterior = 0.45
velScanner_anterior = 4
detectorGain_anterior = 0
amplifierOffset_anterior = 0
resolucao_anterior = 512
pasta_anterior = "C/userPublic/Desktop"
formato_anterior = ".lsm"


print("Olá, este programa possui como objetivo receber dados para ajustar o microscópio corretamente e gerar a imagem desejada.")

print("O tipo de célula a ser escaneada atualmente é:",tipoDeCelula_anterior,)
tipoDeCelula_nova = input("Para qual tipo de célula deseja configurar? ")
print("Houve alteração na variável inserida?",tipoDeCelula_anterior != tipoDeCelula_nova)

print("A faixa de iluminação configurada atualmente é:",faixaDeIlum_anterior,"nanômetros")
faixaDeIlum_nova = int(input("Para qual faixa de iluminação deseja configurar? "))
print("Houve alteração na variável inserida?",faixaDeIlum_anterior != faixaDeIlum_nova)

print("A intensidade configurada atualmente para o laser é:",intensidade_anterior,)
intensidade_nova = float(input("Qual intensidade deseja configurar para o laser? "))
print("Houve alteração na variável inserida?",intensidade_anterior != intensidade_nova)

print("A objetiva configurada atualmente é:",objetiva_anterior,"x")
objetiva_nova = int(input("Para qual objetiva deseja configurar? "))
print("Houve alteração na variável inserida?",objetiva_anterior != objetiva_nova)

print("O diâmetro do ponto de iluminação está configurado atualmente para ",diametroDoPonto_anterior,"micrômetros")
diametroDoPonto_novo = float(input("Para qual valor deseja configurar o diâmetro do ponto de iluminação? "))
print("Houve alteração na variável inserida?",diametroDoPonto_anterior != diametroDoPonto_novo)

print("A velocidade do scanner está configurada atualmente para:",velScanner_anterior)
velScanner_nova = float(input("Para qual velocidade deseja configurar o scanner? "))
print("Houve alteração na variável inserida? ", velScanner_anterior != velScanner_nova)

print("O 'detector gain' está configurado atualmente para o valor",detectorGain_anterior)
detectorGain_novo = float(input("Para qual valor deseja configurar o 'detector gain'? "))
print("Houve alteração na variável inserida?",detectorGain_anterior != detectorGain_novo)

print("O 'amplifier offset' está configurado atualmente para o valor",amplifierOffset_anterior)
amplifierOffset_novo = float(input("Para qual valor deseja configurar o 'amplifier offset'? "))
print("Houve alteração na variável inserida?",amplifierOffset_anterior != amplifierOffset_novo)

print("A resolução configurada atualmente é:",resolucao_anterior)
resolucao_nova = int(input("Para qual resolução deseja configurar? "))
print("Houve alteração na variável inserida?",resolucao_anterior != resolucao_nova)

print("A pasta de destino atualmente selecionada para exportação é:",pasta_anterior)
pasta_nova = input("Qual a pasta de destino desejada? ")
print("Houve alteração na variável inserida?", pasta_anterior != pasta_nova)

print("O formato de arquivo selecionado atualmente para exportação é:",formato_anterior)
formato_novo = input("Para qual formato de arquivo deseja configurar para exportação? ")
print("Houve alteração na variável inserida?",formato_anterior != formato_novo)

print("As informações de configuração setadas pelo usuário são: ")
print("Resolução:",resolucao_nova)
print("Tipo de célula:",tipoDeCelula_nova)
print("Faixa de iluminação:",faixaDeIlum_nova,"nanômetros")
print("Intensidade do laser:",intensidade_nova)
print("Objetiva:",objetiva_nova,"x")
print("Diâmetro do ponto de iluminação:",diametroDoPonto_novo,"micrômetros")
print("Velocidade do scanner:",velScanner_nova)
print("Detector gain:",detectorGain_novo)
print("Amplifier offset:",amplifierOffset_novo)
print("Resolução:",resolucao_nova)
print("Pasta de destino:",pasta_nova)
print("Formato de arquivo:",formato_novo)

# Calibração horizontal do equipamento

primeiraLetra = input("Agora, vamos calibrar horizontalmente o equipamento. Para isso, por favor, informe a primeira letra do seu nome: ")
primeiraLetraRep = input("Certo, agora digite essa letra uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #1
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #2
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #3
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #4
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #5
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #6
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #7
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #8
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #9
primeiraLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",primeiraLetraRep,"está correto?", primeiraLetra == primeiraLetraRep) #10

ultimaLetra = input("Ainda não finalizamos a calibração horizontal. Então, por favor, informe a última letra do seu nome: ")
ultimaLetraRep = input("Certo, agora digite essa letra uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #1
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #2
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #3
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #4
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #5
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #6
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #7
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #8
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #9
ultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",ultimaLetraRep,"está correto?", ultimaLetra == ultimaLetraRep) #10

# Calibração vertical do equipamento

segundaLetra = input("Agora, vamos calibrar verticalmente o equipamento. Para isso, por favor, informe a segunda letra do seu nome: ")
segundaLetraRep = input("Certo, agora digite essa letra uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #1
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #2
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #3
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #4
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #5
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #6
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #7
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #8
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #9
segundaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",segundaLetraRep,"está correto?", segundaLetra == segundaLetraRep) #10

penultimaLetra = input("Ainda não finalizamos a calibração vertical do equipamento. Então, por favor, informe a penúltima letra do seu nome: ")
penultimaLetraRep = input("Certo, agora digite essa letra uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #1
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #2
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #3
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #4
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #5
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #6
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #7
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #8
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #9
penultimaLetraRep = input("Digite essa letra mais uma vez: ")
print("O dígito",penultimaLetraRep,"está correto?", penultimaLetra == penultimaLetraRep) #10

calibracaoFinal = primeiraLetra == primeiraLetraRep and ultimaLetra == ultimaLetraRep and segundaLetra == segundaLetraRep and penultimaLetra == penultimaLetraRep
print("A calibração do microscópio foi finalizada com sucesso?",calibracaoFinal)
