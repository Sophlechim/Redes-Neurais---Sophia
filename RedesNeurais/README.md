<h2 align="center"> 🧠Experimentos de redes neurais artificiais💻 </h2>

<img src="https://user-images.githubusercontent.com/107013536/225460843-633e8f40-683f-4d8f-a420-c627d1d0a459.png" width="100" hight="100">

Redes neurais são algoritmos extremamente importantes para a tecnologia atual. Altamente utilizados em Aprendizado de Máquina, uma vez que são capazes de identificar padrões de comportamentos, permitindo o desenvolvimento desses sistemas de aprendizagem própria, dado um conjunto de dados.

Essa pasta reservada para experimentos de redes neurais realizados durante as aulas da disciplina. Nela é possível ver que há diferentes arquivos .ipynb os quais dizem respeito ao notebooks do JupyterLab. Ao todo se encontram atualizados dois experimentos completos e um arquivo para armazenar funções.

<hr>

<summary><b> "funcoes.py" </b></summary>
<p align='justify'>
Esse arquivo foi criado com o intuito de armazenar programas de funções globais que podem ser usadas em diferentes notebooks importando-as pelo comando <b>"from funcoes import [nome da funcao]"</b>, de maneira a deixar o código principal mais organizado e facilitar a utilização das funções definidas apenas importando do arquivo quando necessário usar qualquer uma chamando por seu respectivo nome definido.
</p>

<h3> Experimentos de aula </h3>
<p align='justify'>
Essa é uma lista para descrever os experimentos de redes neurais trabalhados durante as aulas. Para ver as descrições, basta clicar no triângulo ao lado dos nomes dos experimentos. Caso queria acessar os algoritmos, clique nos hiperlinks em azul de cada um dos experimentos.
</p>

<details><summary><b><a href="https://github.com/Sophlechim/Redes-Neurais---Sophia/blob/main/RedesNeurais/experimento%20R.02%20-%20classes.ipynb"> "experimento R.02 - classes.ipynb" </a></b></summary>
<p align='justify'>
Estamos finalmente fazendo o nosso primeiro expeirmento do segmento de Redes Neurais, o qual nos introduz um novo modelo de código classes. Vale ressaltar que este e o terceiro experimento foram feitos antes do primeiro porque não iremos trabalhar com ele.
</p>
<p align='justify'>
Mas o que são classes??? Elas são um modelo de código que serve para criar objetos, quaisquer coisas, pois em `Python`, quase tudo pode ser classificado como objeto. É uma forma muito útil de organizar dados e funções, de maneira que elas podem ser armazenadas em secções diferentes para cada tipo de objeto que queremos criar. A estrutura que exige o uso das classes é complexa de uma forma que apenas listas, funções, dicionários e conjuntos não conseguem realizar.
</p>
</details>

<details><summary><b><a href="https://github.com/Sophlechim/Redes-Neurais---Sophia/blob/main/RedesNeurais/experimento%20R.03%20-%20construindo%20um%20grafo%20automaticamente.ipynb"> "experimento R.03 - construindo um grafos automaticamente.ipynb" </a></b></summary>
<p align='justify'>
Seguindo o assunto sobre classes em `Python`, esse experimento três, feito na mesma aula que o experimento dois, utilizamos da modelo de classes para construir o primeiro passo de uma rede neural artificial usando um grafo que trabalhamos em sala de aula, fora do JupyterLab Notebook. Podemos ver esse grafo construído na secção `Refazendo o grafo que fizemos na aula anterior`. 
</p>
<p align='justify'>
<b>Nota:</b> Por enquanto, qualquer grafo plotado neste Notebook não pode ser visualizado, pois meu computador não possui o software necessário para retornar a imagem dentro do JupyterLab. Caso não tenha o software em seu computador e queria ver sem precisar baixá-lo, primeiramente, certifique-se de que tenha instalado o pacote `graphviz` (pode baixá-lo usando o código presente na célula 'raw' abaixo). Depois, acesse o seguinte link <a href="https://dreampuf.github.io/GraphvizOnline/"> GraphvizOnline </a> e copie cada um dos URL's retornados pelos códigos acima e substitua o que está no script em preto pelo `digraph` que deseja ver.
</p>
</details>

<details><summary><b><a href=""> "experimento R.04 - computando gradiente locais.ipynb" </a></b></summary>
<p align='justify'>
Partimos agora para a parte matemática da construção de um grafo computacional para uma rede neural artificial. Essa construção utilizou-se do mesmo conceito de classe trabalhado nos experimentos anteriores, para construir nossos grafos. Sendo assim, continuamos a trabalhar com a nossa classe criada no notebook anterior, R.03, para gerar o grafo computacional, de forma que atualizamos ele com novas informações com o intuito de calcular os gradientes locais através do processo chamado <i><b>backpropagation</i></b>. Este processo é uma base muito importante para a construção de uma rede neural, usando a <i><b>regra de cadeia</i></b> para treinar o modelo de rede, ajustando o peso das ligações da rede para minimizar a diferença entre o vetor de saída real e o esperado, como dito pelos autores do do artigo <a href='https://www.nature.com/articles/323533a0'>"Learning representation by back-propagation errors"</a>. A qualidade desse ajuste é medida pelo gradiente local de cada vértice numérico.
</p>
</details>
⚠️Status do segmento: Em andamento 🔄
