# Cálculo dos movimentos da cabeça (velocidade, ADM em planos de guinada, inclinação e rotação); e número de repetições de um determinado padrão:

Input: timeinterval # Entrada: Imputando a variável intervalo de tempo em milissegundos.
Output: movement events # Saída: referir os dados resultantes dos eventos de movimentos.
events = []; # criando uma lista dos eventos.
while exercise-performed == True do # enquanto o exercício for realizado,
  [yaw{p} (t), pitch{p} (t), roll{p} (t)] = # comentário contextualizado abaixo.
  collectdata(timeinterval); # colete os dados no intervalo de tempo dos ângulos (Euler) de guinada, inclinação e rotação de cabeça e cintura (p).
  for plane in [yaw, pitch, roll] do # para o plano em ângulos de guinada, inclinação e rotação de cabeça e cintura (p):
    plane{p} (t) = eliminateFullCircles(plane{p} (t)); # aplique a função de eliminação de “círculo completo” para corrigir a descontinuidade que aparece nos dados dos ângulos de Euler ao ultrapassar 360º,
    plane{p} (t) = lowPassFilter(plane{p} (t)); # aplique o filtro passa-baixa de 2ª ordem, com f c = 50 Hz e
    mins, maxs = localExtremaYaw(plane{p} (t)); # cálcule os extremos (mins e maxs) locais da série de dados.
  end # fim do pré-processsamento.
  for each min in mins do # comentário contextualizado abaixo.
    events.apend(getMaxPair(maxs)); # aplique a função de pareamento de distância mínima para estimar os pares mín – máx para todos os eventos dentro deste conjunto.
  end # fim do processamento de estimativa dos pares de dados.
  getRepetitions(events); # localize o conteúdo de uma repetição específica em um campo de repetição dos eventos.
  for each event in events do # para todos os eventos dentro deste conjunto:
    getSpeed(event); # calcule as métricas de velocidade e
    getRange(event); # calcule as métricas de faixa.
  end # fim do processamento de cálculo das métricas.
end # fim da coleta de dados no intervalo de tempo.
return; # finalizar a execução do bloco de instrução da função, retornado os valores.


22