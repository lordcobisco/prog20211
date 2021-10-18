Algoritmo "a Caminho do IIN-ELS"
// Disciplina   : [Fundamentos de Programa??o e
//Desenvolvimento de Projetos aplicados ? Neuroengenharia]
// Professor   : Andr? Felipe Oliveira de Azevedo Dantas
// Descri??o   : Descreve que tenho de casa at? o IIN-ELS
// Autor(a)    : Ualisson Carlos Ribeiro da Cruz
// Data atual  : 04/09/2021
Var

estado, hora, minutos, levantar, padraohr, padraomn, pressao, op, condicao: inteiro;

Inicio
hora <- 0;
minutos <-0;
levantar <-0;
pressao <-0;
padraohr <-0;
padraomn <-0;
op <- 0;
condicao <- 0;

escreval("_____Time - HH:MM______")

// Rel?gio norteador de tomada de decisao
// para chegar ate o ISD
repita

      escreval("Informe a Hora em | HH |:  ")
      leia(hora)
      escreval("informe os minutos em |MM|: ")
      leia(minutos)

      se (hora < 24) e (hora >= 0) entao
      padraohr <- 1
      senao
      limpatela
      escreval("Digite a hora no formato correto!")
      fimse

      se (minutos < 59) e (minutos >= 0) entao
      padraomn <-1;
      senao
      limpatela
      escreval("Digite os minutos no formato correto!")
      fimse
//verifica se a hora e os minutos esta no padrao correto
se (padraohr = 1) e (padraomn = 1) entao

   se (hora = 5) e (minutos < 30) entao
      levantar <- 0
      pressao <- 0
      limpatela
      escreval("A??o: Permanecer deitado e olhar agenda de compromissos!")
   fimse
fimse
//condicoes que configura a tomada de decisao
se (hora = 5) e (minutos > 30) entao
   levantar <- 1
   pressao <- 1
   limpatela
   escreval("A??o: Me levanto e saio da cama")
   estado <- 1
   senao
   se (hora >= 6) e (hora < 8)entao
   levantar <- 1
   pressao <- 2
   limpatela
   escreval("A??o: Me levanto e saio da cama rapidamente")
   estado <- 1
   fimse
fimse
se (hora >= 8) entao
   levantar <- 1
   limpatela
   escreval("A??o: Me levanto, mas n?o vou para ISD, porque estou doente ou n?o tenho aula.")
   estado <- 0
fimse
limpatela
ate levantar = 1


se pressao = 1 entao
   limpatela
   escreval("A??o: Tomar banho, escovar os dentes e depois preparar o caf?.")
fimse

se pressao = 2 entao
   limpatela
   escreval("A??o: Tomar banho, trocar de roupa e correr pra parada de ?nibus")
fimse
//captador do estado que me encontro
Repita
se estado <> 0 entao
   escreval ("1. Est? na parada esperando o bus?o do ISD")
   escreval ("2. Ocorreu imprevisto e n?o conseguiu chegar a tempo na parada")
   escreval ("3. Peguei carona at? o ISD")
   escreval ("Escolha uma op??o de 1 a 3 ): ")
   leia (op)

   ESCOLHA (op)
   Caso 1
   escreval("Tenho Alta probabilidade de chegar no ISD")
   condicao <- 1
   Caso 2
   escreval("Tenho baixa probabilidade de chegar no ISD")
   estado <-0
   condicao <-1
   Caso 3
   escreval("Tenho Alta probabilidade de chegar no ISD")
   condicao <- 1
   OUTROCASO
   escreval ("Op??o invalida")
   FIMESCOLHA
senao
se estado = 0 entao
escreval("Resolver outras atividades di?rias")
condicao <- 1
fimse
fimse

ATE (condicao = 1)

Fimalgoritmo