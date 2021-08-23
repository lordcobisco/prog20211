Algoritmo "a Caminho do IIN-ELS"
// Disciplina   : [Fundamentos de Programação e
//Desenvolvimento de Projetos aplicados à Neuroengenharia]
// Professor   : André Felipe Oliveira de Azevedo Dantas
// Descrição   : Descreve que tenho de casa até o IIN-ELS
// Autor(a)    : Kellisson Kayonário de Lima
// Data atual  : 10/08/2021
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

// Relógio norteador de tomada de decisao
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
      escreval("Ação: Permanecer deitado e olhar agenda de compromissos!")
   fimse
fimse
//condicoes que configura a tomada de decisao
se (hora = 5) e (minutos > 30) entao
   levantar <- 1
   pressao <- 1
   limpatela
   escreval("Ação: Me levanto e saio da cama")
   estado <- 1
   senao
   se (hora >= 6) e (hora < 8)entao
   levantar <- 1
   pressao <- 2
   limpatela
   escreval("Ação: Me levanto e saio da cama rapidamente")
   estado <- 1
   fimse
fimse
se (hora >= 8) entao
   levantar <- 1
   limpatela
   escreval("Ação: Me levanto, mas não vou para ISD, porque estou doente ou não tenho aula.")
   estado <- 0
fimse
limpatela
ate levantar = 1


se pressao = 1 entao
   limpatela
   escreval("Ação: Tomar banho, escovar os dentes e depois preparar o café.")
fimse

se pressao = 2 entao
   limpatela
   escreval("Ação: Tomar banho, trocar de roupa e correr pra parada de ônibus")
fimse
//captador do estado que me encontro
Repita
se estado <> 0 entao
   escreval ("1. Está na parada esperando o busão do ISD")
   escreval ("2. Ocorreu imprevisto e não conseguiu chegar a tempo na parada")
   escreval ("3. Peguei carona até o ISD")
   escreval ("Escolha uma opção de 1 a 3 ): ")
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
   escreval ("Opção invalida")
   FIMESCOLHA
senao
se estado = 0 entao
escreval("Resolver outras atividades diárias")
condicao <- 1
fimse
fimse

ATE (condicao = 1)
   
Fimalgoritmo

