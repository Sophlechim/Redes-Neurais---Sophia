<h2 align='center'> 🧠Experimentos de redes neurais artificiais💻 </h2>

<img src="https://user-images.githubusercontent.com/107013536/225460843-633e8f40-683f-4d8f-a420-c627d1d0a459.png" width="100" hight="100">

Redes neurais são algoritmos extremamente importantes para a tecnologia atual. Altamente utilizados em Aprendizado de Máquina, uma vez que são capazes de identificar padrões de comportamentos, permitindo o desenvolvimento desses sistemas de aprendizagem própria, dado um conjunto de dados.

Essa pasta reservada para experimentos de redes neurais realizados durante as aulas da disciplina. Nela é possível ver que há diferentes arquivos .ipynb os quais dizem respeito ao notebooks do JupyterLab. Ao todo se encontram atualizados dois experimentos completos e um arquivo para armazenar funções.

<hr>

<summary><b> "funcoes.py" </b></summary>
<p align='justify'>
Esse arquivo foi criado com o intuito de armazenar programas de funções globais que podem ser usadas em diferentes notebooks importando-as pelo comando <b>"from funcoes import [nome da funcao]"</b>, de maneira a deixar o código principal mais organizado e facilitar a utilização das funções definidas apenas importando do arquivo quando necessário usar qualquer uma chamando por seu respectivo nome definido.
</p>

<summary><b> "classes.py" </b></summary>
<p align='justify'>
Esse arquivo foi criado com o intuito de armazenar as classes usadas na aula de Redes Neurais, permitindo que a classe seja usada em diferentes notebooks de experimentos sem que ela precise ser escrita dentro dos arquivos toda vez que precisar ser usada. Tudo o que é preciso para usá-la é importar através do comando <b>"from classes import [nome da classe]"</b>. Isso permite, também que a formatação de escrita e organização do notebook esteja muito mais bonita e clara. 
</p>

<h3> Experimentos de aula </h3>
<p align='justify'>
Essa é uma lista para descrever os experimentos de redes neurais trabalhados durante as aulas. Para ver as descrições, basta clicar no triângulo ao lado dos nomes dos experimentos. Caso queria acessar os algoritmos, clique nos hiperlinks em azul de cada um dos experimentos.
</p>

<details><summary><b><a href='https://github.com/Sophlechim/Redes-Neurais---Sophia/blob/main/RedesNeurais/experimento%20R.02%20-%20classes.ipynb'> "experimento R.02 - classes.ipynb" </a></b></summary>
<p align='justify'>
Estamos finalmente fazendo o nosso primeiro expeirmento do segmento de Redes Neurais, o qual nos introduz um novo modelo de código classes. Vale ressaltar que este e o terceiro experimento foram feitos antes do R.01, pois não iremos trabalhar com ele, portanto considere que ele não exista.
</p>
<p align='justify'>
Mas o que são classes??? Elas são um modelo de código que serve para criar objetos, quaisquer coisas, pois em <b><i>Python</i></b>, quase tudo pode ser classificado como objeto. É uma forma muito útil de organizar dados e funções, de maneira que elas podem ser armazenadas em secções diferentes para cada tipo de objeto que queremos criar. A estrutura que exige o uso das classes é complexa de uma forma que apenas listas, funções, dicionários e conjuntos não conseguem realizar.
</p>
</details>

<details><summary><b><a href='https://github.com/Sophlechim/Redes-Neurais---Sophia/blob/main/RedesNeurais/experimento%20R.03%20-%20construindo%20um%20grafo%20automaticamente.ipynb'> "experimento R.03 - construindo um grafos automaticamente.ipynb" </a></b></summary>
<p align='justify'>
 Seguindo o assunto sobre classes em <b><i>Python</i></b>, esse experimento três, feito na mesma aula que o experimento dois, utilizamos da modelo de classes para construir o primeiro passo de uma rede neural artificial usando um grafo que trabalhamos em sala de aula, fora do JupyterLab Notebook. Podemos ver esse grafo construído na secção <b><u>Refazendo o grafo que fizemos na aula anterior`</u><b>. 
</p>
<p align='justify'>
<b>Nota:</b> Por enquanto, qualquer grafo plotado neste Notebook não pode ser visualizado, pois meu computador não possui o software necessário para retornar a imagem dentro do JupyterLab. Caso não tenha o software em seu computador e queria ver sem precisar baixá-lo, primeiramente, certifique-se de que tenha instalado o pacote <b><i>graphviz</i></b> (pode baixá-lo usando o código presente na célula 'raw' do notebook). Depois, acesse o seguinte link <a href="https://dreampuf.github.io/GraphvizOnline/"> GraphvizOnline </a> e copie cada um dos URL's retornados pelos códigos acima e substitua o que está no script em preto pelo grafo que deseja ver.
</p>
</details>

<details><summary><b><a href='https://github.com/Sophlechim/Redes-Neurais---Sophia/blob/main/RedesNeurais/experimento%20R.04%20-%20computando%20gradientes%20locais.ipynb'> "experimento R.04 - computando gradiente locais.ipynb" </a></b></summary>
<p align='justify'>
Partimos agora para a parte matemática da construção de um grafo computacional para uma rede neural artificial. Essa construção utilizou-se do mesmo conceito de classe trabalhado nos experimentos anteriores, para construir nossos grafos. Sendo assim, continuamos a trabalhar com a nossa classe criada no notebook anterior, R.03, para gerar o grafo computacional, de forma que atualizamos ele com novas informações com o intuito de calcular os gradientes locais através do processo chamado <b><i>backpropagation</i></b>. Este processo é uma base muito importante para a construção de uma rede neural, usando a <b><i>regra de cadeia</i></b> para treinar o modelo de rede, ajustando o peso das ligações da rede para minimizar a diferença entre o vetor de saída real e o esperado, como dito pelos autores do do artigo <a href='https://www.nature.com/articles/323533a0'>"Learning representation by back-propagation errors"</a>. A qualidade desse ajuste é medida pelo gradiente local de cada vértice numérico.
</p>
<p align='justify'>
Com isso, nós buscamos computar os gradientes locais e treinar uma rede neural manualmente, ou seja, definimos uma equação para calculá-los e alteramos parâmetros de maneira não muito prática. Por isso, aprendemos também à calcular o gradiente de maneira automática.
</p>
</details>

<details><summary><b><a href='https://github.com/Sophlechim/Redes-Neurais---Sophia/blob/main/RedesNeurais/experimento%20R.05%20-%20finalizando%20a%20classe%20Valor.ipynb'> "experimento R.05 - finalizando a classe Valor.ipynb" </a></b></summary>
<p align='justify'>
Chegamos agora em um momento final para que nossa classe que trabalhamos nas últimas aulas possa ser treinada, pois aqui, nesse quinto experimento de redes neurais artificiais, vamos finalizar a classe <b><u>Valor</u></b>, de forma que ela esteja aprimorada da melhor maneira possível. Portanto, aqui, o que procuramos é tornar possível que ela possa realizar diferentes tipos de operações que vão muito além daquelas já existentes, acompanhando o funcionamento na nossa rede neural artificial.
Sendo assim, pudemos observar a forma que as operações se comportavam conforme rodamos cada uma delas antes e depois de definir as funções necessárias para que as operações escritas pudessem ser entendidas pelo Python.
</p>
</details>

<details><summary><b><a href='https://github.com/Sophlechim/Redes-Neurais---Sophia/blob/main/RedesNeurais/experimento%20R.06%20-%20redes%20neurais%20artificiais.ipynb'> "experimento R.06 - redes neurais artificiais" </a></b></summary>
<p align='justify'>
 Após concluir a classe <b><u>Valor</u></b>, a qual agora já faz tudo o que precisaremos para funcionar e sustentar nossa rede neural, o que procuramos agora é construir a nossa rede neural completa. Para isso, estamos aqui, neste notebook R.06, montando uma rede neural parte por parte, de forma que cada parte criada é uma classe que armazena informações que seão responsáveis por criar e fazer funcionar os elementos que compõem uma rede artificial: o neurônio, a camada e uma rede de multicamadas. Essa construção serve também para entendermos como funciona uma rede neural artificial, de maneira pausada e aos poucos.
</p>
</details>

⚠️Status do segmento: Em andamento 🔄
