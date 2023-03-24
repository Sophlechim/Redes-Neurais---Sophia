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

def func_obj_cnb(individuo):
    """Calcula o fitness do individuo para o problema das caixas não-binarias.
    
    Args:
        individuo: lista que representa um individuo dentro do problema
        
    Retunrs:
        Um valor que representando o fitness de cada individuo
    """
    fitness = sum (individuo)
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