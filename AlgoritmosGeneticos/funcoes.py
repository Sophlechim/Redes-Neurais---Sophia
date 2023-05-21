import random
import copy

###################
#     SUPORTE     #
###################

def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist

def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades

def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
        
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    valor_total = 0
    peso_total = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]
            
            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item
    
    return valor_total, peso_total


###################
#      GENES      #
###################

def gene_cb():
    """Gera um gene válido para o problema das caixas binárias
    
    Returns:
        Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias.
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir
    
    Returns:
        Um valor de 0 até o valor máximo da caixa
    """
    gene = random.randint(0, valor_max_caixa)
    return gene

def gene_letra(letras):
    """Sorteia uma letra.
    
    Args:
      letras: letras possíveis de serem sorteadas.
      
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra

#####################
#     INDIVÍDUOS    #
#####################
    
def individuo_cb(n):
    """Gera um indivíduo para o problema das caixas binárias.
    
    Args:
        n: número de genes do indivíduo.
    
    Return:
        Uma lista com n genes. Cada é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
        
    return individuo

def individuo_cnb(numero_genes, valor_max_caixa):
    """Gera um individuo válido para o problema das caixas não-binárias.
    
    Args:
        número de genes: lista que representa o indivíduo
        valor_max_caixas: valor máximo que a caixa pode assumir
        
    Returns:
        Uma lista que representa um individuo válido para o problema
    """
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
        
    return individuo

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
      
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato

def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes

###################
#    POPULAÇÃO    #
###################

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Args:
        tamanho: tamanho da população
        n: numero de genes de um individuo
    
    Returns:
        Uma lista onde item é um indivíduo. Um individuo é uma lista com n genes
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
        
    return populacao

def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    """Cria um conjunto de indivíduos para o problema das caixas não-binárias.
    
    Args:
        tamanho: número de individuos da população
        genes: numero de genes do individuo
        valor máximo: valor máximo assumido pela caixa
        
    Returns:
        Lista em que cada item representa um individuo
    """
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
        
    return populacao

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema de senha
    
    Args
      tamanho: tamanho da população
      tamanho_senha: inteiro representando o tamanho de senha
      letras: letras possíveis de serem sorteadas
      
    Returns:
      Lista com todos os indivíduos da população no problema de senha
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao

def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao

#################
#    SELEÇÃO    #
#################

def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
        populacao: lista com todos os individuos da população
        fitness: lista com o valor da funcao objetivo da população
      
    Return:
        Um valor representando a soma dos genes do individuo.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    
    Args:
      populacao: população do problema
      fun_objetivo: função objetivo
      tamanho_torneio: quantidade de invidiuos que batalham entre si
      
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # associando cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # como queremos o individuo de menor fitness, então:
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

# FUNÇAO PARA DESAFIO CAIXEIRO INCONSCIENTE
def selecao_torneio_max(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    
    Nota: da forma que está implementada, essa função servirá para maximização.
    
    Args:
      populacao: população do problema
      fun_objetivo: função objetivo
      tamanho_torneio: quantidade de invidiuos que batalham entre si
      
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # associando cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        maximo_fitness = -float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # como queremos o individuo de menor fitness, então:
            if fit > maximo_fitness:
                selecionado = individuo
                maximo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

##################
#   CRUZAMENTO   #
##################

def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de pontos simples.
    
    Args:
        pai: uma lista representando um individuo
        mae: uma lista represebtando um individuo
    
    Return:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    
    Ver pág. 37 do livro do Wirsansky.
    
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) -2)
    corte2 = random.randint(corte1 + 1, len(pai) -1)
    
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
    
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
            
    return filho1, filho2

#################
#    MUTAÇÃO    #
#################

def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias
    
    Args:
        individuo: uma lista representando um individuo no problema das caixas binárias
    
    Return:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo

def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação do individuo
    
    Args:
        individuo: individuo que deve sofrer mutação
        valor_max_caixa: valor máximo assumido pela caixa
    
    Returns:
        Um individuo que sofreu mutação
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    
    return individuo

def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
      
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo

def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    
    Args:
      individuo: uma lista representado um individuo.
    
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    return individuo


###########################
#    FUNÇÕES OBJETIVO     #
###########################

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias
    
    Return:
        Um valor rapresentando a soma dos genes do indivíduo.
    """
    return sum(individuo)

def func_obj_cnb(individuo):
    """Calcula o fitness do individuo para o problema das caixas não-binarias.
    
    Args:
        individuo: lista que representa um individuo dentro do problema
        
    Retunrs:
        Um valor que representando o fitness de cada individuo
    """
    fitness = sum (individuo)
    return fitness

def func_obj_senha(individuo, senha_verdadeira):
    """Computa a função objetivo de uma indivíduo no problema da senha
    
    Args:
        individuo: lista contendo as letras da senha
        senha_verdadeira: a senha que você está tentando descobrir
        
    Returns:
        A "distância" entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra. 
        Quanto mais distante uma letra for da que deveria ser, maior é essa distância.
    """
    diferenca = 0
    
    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))
        
    return diferenca

def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    
    Args:
      individiuo: lista contendo a ordem das cidades que serão visitadas
      cidades: dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    for posicao in range(len(individuo) -1):
        
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
        
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
        
    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso

    return distancia

def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    
    Args:
      individiuo: lista binária contendo a informação de quais objetos serão selecionados.
      objetos: dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite: número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes: lista contendo a ordem dos nomes dos objetos.
        
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila

def func_obj_palindromo(individuo):
    """Computa a função objetivo de uma indivíduo no problema da senha
    
    Args:
        individuo: lista contendo as letras
        
    Returns:
        A "distância" que a palavra encontrada está de um palíndromo. Essa distância é medido letra por letra. 
        Quanto mais distante uma letra for da que deveria ser, maior é essa distância.
    """
    objetivo = 10000
    
    VOGAIS = "aeiou"
    
    for vogal in VOGAIS:
        if vogal in individuo:
            objetivo = 0
            break
    
    if objetivo != 0:
        return objetivo
    
    inverso = copy.deepcopy(individuo)
    inverso.reverse()
    
    for letra_individuo, letra_inverso in zip(individuo, inverso):
        objetivo = objetivo + abs(ord(letra_individuo) - ord(letra_inverso))
        
    return objetivo

#######################################
#    FUNÇÕES OBJETIVO - população     #
#######################################

def funcao_objetivo_pop_cb(populacao):
    """Calcula a funcao objetivo para todos os membres de uma população.
    
    Args:
      populacao: lista com todos os individuos da população
    
    Return:
      Lista de valores representando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fun_ob = funcao_objetivo_cb(individuo)
        fitness.append(fun_ob)
    return fitness

def func_obj_pop_cnb(populacao):
    """Calcula a função objetivo da população inteira.
    
    Args:
        população: lista com todos os individuos da população
        
    Returns:
        Lista de valores representando o fitness de cada individuo da população
    """
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = func_obj_cnb(individuo)
        fitness_pop.append(fitness_ind)
    
    return fitness_pop

def func_obj_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha
    
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
      
    Returns:
      Lista contendo os valores da métrica de distância entre senhas
    """
    resultado = []

    for individuo in populacao:
        resultado.append(func_obj_senha(individuo, senha_verdadeira))

    return resultado

def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado

def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:     # navegue a funçao objetivo dos indivíduos
        resultado.append(           # adicione 
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado

def func_obj_pop_palindromo(populacao):
    """Computa a funcao objetivo de uma populaçao no problema da senha
    
    Args:
      populacao: lista com todos os individuos da população
      
    Returns:
      Lista contendo os valores da métrica de distância entre as palavras.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(func_obj_palindromo(individuo))

    return resultado