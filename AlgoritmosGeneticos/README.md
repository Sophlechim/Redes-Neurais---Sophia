<h2 align="center"> 🧬Experimentos de otimização e algoritmos genéticos🧪 </h2>

<img src="https://user-images.githubusercontent.com/107013536/225460843-633e8f40-683f-4d8f-a420-c627d1d0a459.png" width="100" hight="100">

<p align="justify">
Essa pasta reservada para experimentos de algoritmos genéticos realizados durante as aulas da disciplina. Nela é possível ver que há diferentes arquivos .ipynb os quais dizem respeito ao notebooks do JupyterLab. Ao todo se encontram atualizados dois experimentos, uma lista de experimentos de algoritmo genético e um "caderno" de anotações para consulta.
</p>

<summary><b>"Algumas coisas que valem a pena aprender ou relembrar"</b></summary>
<p align="justify">
Como o próprio nome já esclarece, esse notebook nada mais é que uma lista de diferentes informações de código que podem ser consultados para relembrar como usá-los e para que servem, sendo uma ótima ferramenta de aprendizado, principalmente para quem tem dificuldade em programação. Diferentes módulos podem ser encontrados nessa lista, como <b>random</b> e <b>itertools</b>, por exemplo.
</p>

<summary><b>"funcoes.py"</b></summary>
<p align="justify">
Esse arquivo foi criado com o intuito de armazenar programas de funções globais que podem ser usadas em diferentes notebooks importando-as pelo comando <b>"from funcoes import [nome da funcao]"</b>, de maneira a deixar o código principal mais organizado e facilitar a utilização das funções definidas apenas importando do arquivo quando necessário usar qualquer uma chamando por seu respectivo nome definido.
</p>

<summary><b>"Lista de experimentos - algoritmos geneticos"</b></summary>
<p align="justify">
Estes são alguns exercícios extras para prática com algoritmos genéticos, os arquivos desses experimentos resolvidos devem receber o padrão de nome <b>"experimento GA.xx - [nome do experimento]"</b>.
</p>
<details><b>Experimentos já feitos</b>
<summary>"experimento GA.03 - caixeiro com gasolina infinita"</summary>
<p align="justify">
Este desafio passado para resolução, foi proposto com o intuito de utilizar dos aprendizados das aulas para resolver um problema presente na lista de experimentos, presente nesta mesma pasta. Da mesma forma que o experimento A.06 foi resolvido na aula anterior, este aqui se utiliza das mesmas ideias, porém com leves modificações que fazem bastante diferença. Os módulos requeridos para o experimento eram: <i><b>permutations</b></i> de <i><b>itertools</b></i> e <i><b>random</b></i>.
</p>
</details>

<h3> Experimentos de aula - descrição </h3>
<p align="justify">
Aqui está a lista dos experimentos de algoritmos genéticos trabalhados durante as aulas.
</p>
<details><summary><b>"experimento A.01 - busca aleatoria.ipynb"</b></summary>
<p align="justify">
O primeiro experimento realizado na primeira aula da disciplina de Redes Neurais e Algoritmos Genéticos se resumia em uma das formas de solucionar um problema de otimização, nesse caso, por busca aleatória. Com essa aula, nós aprendemos a resolver problemas de otimização com caixas binárias usando a bibloteca <i><b>random</b></i> do python, observando assim, que esse algoritmo é probabilístico. Isso pode ser visto também através da diferença dada em cada resultado obtido quando o código é rodade várias vezes.
</p>
</details>

<details><summary><b>"experimento A.02 - busca em grade.ipynb"</b></summary>
<p align="justify">
O segundo experimento, também feito na primeira aula, para resolver um problema de otimização de 4 caixas binárias foi pelo método de <i><b>busca em grade</b></i>, ou seja, o objetivo que temos com ele é testar todas as cominações possíveis de acordo com o conjunto de parâmetros dados até encontrar a melhor combinação. Como esse é um problema de análise combinatória, foi possível utilizar o módulo <i><b>itertools</b></i> para encontrar a combinação das caixas.
</p>
</details>

<details><summary><b>"experimento A.03 - algoritmo genetico.ipynb"</b></summary>
<p align="justify">
Na segunda aula, conseguimos finalmente montar o nosso primeiro algoritmo genético, a partir do qual, ainda trabalhando com as caixas binárias, pôde-se encontrar a combinação de caixas que somam o máximo de valores possíveis para as quatro caixas, utilizando as funções necessárias do arquivo <i><b>"funcoes.py"</b></i> e a biblioteca <i><b>random</b></i> para selecionar, cruzar e mutar os genes.
</p>
</details>

<details><summary><b>"experimento A.04 - caixas nao-binarias.ipynb"</b></summary>
<p align="justify">
Nesse Notebook, vemos um algoritmo genético construido para resulver um problema de caixas não-binárias, considerando valores inteiros que podem ser de um conjunto definido de valores, como de 0 à 100. Isso significa que a quantidade de genes possíveis a serem combinados em cada indíviduo de 4 genes, ou caixas, são de 101 valores diferentes. Assim como antes, o objetivo encontrar a melhor combinação possível, que os genes somem o valor máximo a se alcançar.
</p>
</details>

<details><summary><b>"experimento A.05 - descobrindo a senha.ipynb"</b></summary>
<p align="justify">
No quinto experimento realizado, foi proposta a construção de um código de algoritmo genético para descobrir uma senha, a qual é dada pela função objetiva presente no arquivo <i><b>"funcoes.py"</b></i> para computar dentro da população do problema, ou seja, essa senha já é sabida por essa função, que tem como papel quantificar a semelhança dos palpites retornados pelo algoritmo, até que a senha seja descoberta. utilizamos a mesma ideia de seleção, cruzamento e mutação com o módulo <i><b>random</b></i>, porém com uma <i><b>string</b></i>.
</p>
</details>

<details><summary><b>"experimento A.06 - o caixeiro viajante.ipynb"</b></summary>
<p align="justify">
Depois de solucionar alguns problemas utilizando algoritmos genéticos, nesse sexto experimento foi necessário resolver o problema caixeiro viajante, o qual consiste em descobrir uma rota pela qual ele passe por todas as cidades apenas uma vez para chegar de volta em sua cidade de partida. O objetivo é encontrar a distância mais curta possível que deve ser percorrida pelo caixeiro. Foi considerada uma lista de 5 cidades, das quais qualquer uma pode ser seu ponto de partida, sendo essa a única por onde ele pode passar duas vezes.
</p>
</details>

<details><summary><b>"experimento A.07 - aplicando restricoes.ipynb"</b></summary>
<p align="justify">
O problema que foi resolvido neste sétimo experimento consistia em otimizar uma busca, em que procuramos maximizar a quantidade de itens dentro de uma mochila para obter o maior valor em dinheiros possíveis, porém sem exceder a capacidade de peso, ou então a mochila irá rasgar e não poderá mais ser usada. Para isso, foi aplicada uma penalidade, limitanado o peso máximo na função objetiva do problema. O objetivo final é, então, solucionar o problema da mochila utilizando um algoritmo genético. Para isso, importou-se as funções do "script" <i><b>funcoes.py</b></i> e a biblioteca <i><b>random</b></i>.
</p>
</details>

⚠️Status do segmento: Em andamento⚠️
