# UNIVERSIDADE CATÓLICA DE PERNAMBUCO
<p align="center">
   <img src="http://www1.unicap.br/icam/wp-content/uploads/2019/06/marca_nova.svg" />
  </p>

# MÉTODOS NUMÉRICOS
### PROBLEMÁTICA
Distribuição Gaussiana & valor Crítico <br>
<p align="justify">
A distribuição Gaussiana decorre de eventos aleatórios. Eventos aleatórios, por sua vez, são fenômenos que, repetidos inúmeras vezes, geram resultados distintos - Por exemplo, o lançamento de um dado ou uma moeda. No entanto, à medida de vezes em que se repete o fenômeno, gera-se um padrão de comportamento. Esse padrão é conhecido como Distribuição Gaussiana ou distribuição normal.<br>
</p>
<p align="justify">
<img src="static/MÉTODOS NUMÉRICOS - PROJETO 01.png" width="700">
</p>

### APLICAÇÃO PRÁTICA
#### Encontrar o valor crítico de uma distribuição normal
Supondo que estamos trabalhando com uma distribuição normal padrão N(0,1) e desejamos calcular o valor crítico z para um intervalo de confiança. Quais os métodos numéricos poderíamos aplicar para chegar a uma solução suficientemente exata, sendo f(x) = 0? Existem alguns métodos numéricos, que serão utilizados para solucionar a equação que não possuí solução analítica. Estes métodos são:
- Método da Bissecção
- Método da Falsa-Posição
- Método de Newton-Rapson
  
### Método da Bissecção
O método da bissecção pode ser definido como uma técnica numérica para encontrar raízes de uma função contínua. Baseia-se no Teorema do Valor Intermediário, que garante que, se uma função muda de sinal em um intervalo [a, b], ela tem pelo menos uma raiz nesse intervalo. Básicamente, podemos analisar o processo que faremos através do fluxorama disponível abaixo.
<p align="justify">
<img src="static/ITERAÇÕES DA BISSECÇÃO.png" width="700">
</p>
Ou seja, através de dados iniciais, como a função requerida, o intervalo e a precisão, iniciaremos o processo de iterações para chegar a uma solução aproximada. Caso se chegue a uma quantidade x de iterações e uma aproximação suficientemente exata de acordo com os dados iniciais, faremos os cálculos finais que o método requer e chegaremos nas raízes que queremos encontrar. Caso não se encontre uma aproximação exata, faremos novas aproximações através de dados que obtivemos das iterações anteriores, até chegarmos a um resultado aproximadamente exato.
