'''OBSERVAÇÕES: Total de Pontos = 10 pontos com peso 7. A atividade avaliativa deve ser realizada em
uma folha de papel e submetida na sua respectiva pasta. Organize seus cálculos e/ou algoritmos de modo
claro (letra legível) e sequenciado para permitir a correção. Qualquer ambiguidade será desconsiderada.
Boa Avaliação!

A técnica de microscopia confocal de varredura à laser se tornou uma ferramenta devido a atributos não
disponíveis em microscopia óptica tradicional, em particular, o modo de contraste. O conceito básico de
microscopia confocal foi desenvolvido originalmente por Marvin Minsky nos anos 50 durante o seu pós-
doutorado na Universidade de Harvard. Minsky tentava observar células neurais in vivo. # A invenção de
Minsky permaneceu décadas sem aplicação, provavelmente pela falta de fontes intensas de luz, detectores
eficientes e computadores com capacidade de processar a grande quantidade de dados gerados #. Após o
trabalho de Minsky, David Egger e Mojmir Petran (1967) construíram, nos anos de 1960, um microscópio
confocal para examinar seções de células cerebrais. Este utilizava um #disco giratório# contendo várias
aberturas circulares (disco de Nipkow). Em 1973, Egger desenvolveu o primeiro microscópio confocal
laser e publicou as primeiras imagens reconhecíveis de células. No fim da década de 1970, o físico
holandês G. J. Brakenhoff e colaboradores (1979) desenvolveram o primeiro microscópio confocal com
sistema de varredura. Simultaneamente, Colin Sheppard contribuiu para a técnica com a teoria de
formações de imagens. Durante os anos 1980, os avanços dos computadores, da tecnologia dos lasers e
dos novos algoritmos de manipulação digital de imagens promoveram o interesse em microscopia
confocal. Brad Amos e John White demonstraram a utilidade de imagens construídas por microscópio
confocal em exame de espécimes biológicos fluorescentes. Segundo Hanlon e colaboradores (2001) os
primeiros instrumentos comerciais apareceram em 1987 e evoluíram durante os anos 1990, com avanços
dos componentes ópticos, da eletrônica, das fontes lasers e dos detectores. A redução dos custos de
produção, o aumento da velocidade de processamento e a evolução da capacidade de armazenamento de
dados dos microcomputadores também contribuíram para a expansão do número de aplicações da
microscopia confocal. Atualmente, estes microscópios são empregados em pesquisas em diversas áreas:
semicondutores, metais, polímeros, contágem de células. A microscopia confocal oferece várias
vantagens com relação aos microscópios de campo amplo convencionais. Ela possui a capacidade de
controlar profundidade de campo, reduzindo a informação periférica ao plano focal, aumentando o
contraste e, consequentemente, a qualidade da imagem. O microscópio confocal possibilita uma maior
resolução em ambos os componentes axiais (lateral e vertical), desta forma, a tecnologia confocal prova
ser um dos avanços mais importantes alcançados em microscopia óptica nos últimos anos. Texto
disponível de forma integral em: https://repositorio.ufu.br/bitstream/123456789/14904/1/d.pdf

O texto apresenta algumas informações de um tipo de microscópio disponível no IIN-ELS. A partir desse
contexto, será criado um cenário de forma que as habilidades que devem ser desenvolvidas para atingir os
objetivos de aprendizagem da Aula 3 sejam atingidas.
Obs: É sabido que o background dos alunos é diverso, o princi
pal objetivo do exercício é ser capaz de
organizar as informações de forma estruturada e que auxilie na execução de tarefas listadas.

A técnica de microscopia confocal de varredura à laser é realizada a partir de um equipamento que lê
informações ópticas e devolve uma imagem. Porém, o equipamento em si é desenvolvido de forma a
interagir com usuários que inserem informações e recebem informações a partir do dispositivo.'''


"""1. Considerando este cenário, crie um projeto organizado no git contendo:
    a. Milestones
    b. Issues
    c. Quadro Kanban (Aba projetos)
    d. Wiki

Obs: tire as fotos do seu projeto organizado e insira num documento word juntamente com o programa a
ser desenvolvido na questão 2.
Obs 2: Esse projeto deve ser organizado com base nos requisitos solicitados na questão 2.


2. Elabore um programa em python que atenda aos seguintes requisitos: 
(LINK PARA AJUDAR: https://www.youtube.com/watch?v=4-gKI5go0y4)
(https://repositorio.ufu.br/bitstream/123456789/14904/1/d.pdf)
(https://www.ufjf.br/pgcbio/files/2018/10/Apostila.pdf)
(https://slideplayer.com.br/slide/361158/)
Obs: Não devem ser utilizadas estruturas de programação que não estejam na aula 3.
    a. Crie as variáveis necessárias para que o programa funcione corretamente.
            - Base e estrutura do microscópio;
            - Fonte laser;
            - Filtro óptico de intensidade;
            - Sistema de iluminação da amostra;
            - Lentes convergentes;
            - Objetiva;
            - Posicionadores dos eixos x,y e z;
            - Divisor de feixe;
            - Abertura circular;
            - detector;
            - Processador e software.
    b. Inicialize as variáveis com valores padrão adequados.
    c. Crie uma pequena mensagem de apresentação do programa para realizar uma interface
    com o usuário. Ex.: “Esse programa tem como objetivo receber dados para ...”
    d. Solicite algumas informações necessárias para a configuração de um microscópio dessa
    natureza. Buscar pelo menos 10 itens para essas informações de entrada. Ex.: resolução
    da imagem desejada, tipo de célula a ser escaneada, faixa de iluminação necessária.
    e. Para cada informação digitada, apresente na tela a seguinte mensagem: “Houve
    alteração na variável inserida? ”. Após a mensagem, apresentar verdadeiro ou falso com
    base no que foi digitado pelo usuário e o que estava armazenado na variável. Obs.: Não
    deve ser utilizado if aqui.
    f. Retorne ao usuário de forma organizada as informações que foram digitadas. Ex.: “As
    informações de configurações setadas pelo usuário são: ...”
    g. Após setada as configurações iniciais o usuário deve utilizar dois caracteres para a
    calibração do equipamento no sentido horizontal. Para isso, ele deve apertar a tecla
    correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.
    h. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
    foi corretamente digitada e mostrar o caractere pressionado.
    i. Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento
    no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda letra do
    seu nome 10x e à penúltima letra do seu nome 10x.
    j. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
    foi corretamente digitada e mostrar o caractere pressionado.
    k. Finalmente, o programa deverá apresentar na tela que houve o término da calibração do
    sistema.
    l. Para verificar que o programa está funcionando corretamente, execute-o colocando um
    breakpoint na linha 15. Tire um print da tela mostrando a linha parada e as informações
    armazenadas nas variáveis até então."""



Número_de_Superfícies = input("digite o número de superfícies a serem construídas")
print(Número_de_Superfícies)

Valor_do_Passo_no_Eixo_Y = input("digite o valor da distância entre as superfícies superfcícies")
print(Valor_do_Passo_no_Eixo_Y)

Arquivos_imagens_Superfícies = input("gerar arquivos de imagens das superfícies")
print(Arquivos_imagens_Superfícies)

Número_de_Colunas_da_Matriz= input("gerar arquivos de imagens das superfícies")
print(Número_de_Colunas_da_Matriz)




