import random

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