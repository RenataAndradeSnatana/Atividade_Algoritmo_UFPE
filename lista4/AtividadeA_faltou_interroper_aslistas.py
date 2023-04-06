# Implementação do algoritmo de ordenação "Bubble Sort" 
# Compara elementos adjacentes e trocando-os se estiverem na ordem errada(ordena os valores na forma decrescente)
def bubble_sort(livros): 
    quant_livros = len(livros)
    comp = 0  # Número Número de comparações 
    trocas = 0 # Número de trocas de elementos realizados pelo algoritmo de ordenação
    
    for i in range(quant_livros): # Enquanto a quantidade de livros existirem.
        for j in range(quant_livros-i-1): # Percorre os elementos que ainda não foram ordenados.
            comp += 1
            if livros[j] > livros[j+1]: # Caso seja a troca é realizada
                livros[j], livros[j+1] = livros[j+1], livros[j]
                trocas += 1
                
    return comp, trocas, livros
# _________________________________________________________________________________________________
# Função que busca o menor elemento da lista colocando na posição correta de forma crescente
def selection_sort(livros):
    quant_livros = len(livros)
    comp = 0
    trocas = 0
    
    for i in range(quant_livros-1): # Intera do primeiro ao penúltimo elemento
        indice_menor = i # Variável que armazena o índice do menor valor encontrado em cada interação
        for j in range(i+1, quant_livros): # Busca pelo menor elemento restante da lista
            comp += 1
            if livros[j] < livros[indice_menor]:
                indice_menor = j
        if indice_menor!= i:
            livros[i], livros[indice_menor] = livros[indice_menor], livros[i]
            trocas += 1
            
    return comp, trocas, livros
# _________________________________________________________________________________________________
# Percorre a lista a partir do segundo elemento até o final, selecionando um elemento por vez e colocando-o em sua posição correta na lista ordenada à esquerda
def insertion_sort(livros): # Função que vai receber os elementos livros como parâmetro e a ordenada
    quant_livros = len(livros)
    comp = 0
    trocas = 0
    
    for i in range(1, quant_livros):
        chave = livros[i]  # Variável chave que armazena o menor valor do elemento selecionado
        j = i - 1 # Variável que vai garantir a próxima posição depois da atual sendo analisada (i).
        
        while j >= 0 and livros[j] > chave: # Se o valor na posição "j" de "livros" é maior do que a chave "chave"
            comp += 1
            livros[j+1] = livros[j]
            trocas += 1 # Todas vês que ocorre a troca onde o elemento chave é armazenado na nova posição
            j -= 1 # Garante que a lista livros é pecorrida da direita para a esquerda para inserir a chave atual na posição correta
        if j >= 0 and livros[j] != chave:
            comp +=1
        livros[j+1] = chave
       
        
    return comp, trocas, livros
# _________________________________________________________________________________________________
# Algoritmo Shellsort - Dividir para conquistar
def shell_sort(livros): # recebe a lista 'livros' como entrada
    quant_livros = len(livros)
    comp = 0
    trocas = 0
    gap = quant_livros // 2
    
    while gap > 0: # Enquanto o gap for diferente de zero repetir até gap zera, isso implica que a lista foi ordenada.
        
        for i in range(gap, quant_livros): # Interação os elementos da lista de 'livros' a partir do índice gap até o final da lista
            temp = livros[i] # Armazena o valor atual durante a troca de elementos da lista, para que não haja perda de dados ou sobreposição de valores.
            j = i # Garante que a sublista a ser percorrida começa na posição i.
            
            while j >= gap and livros[j-gap] > temp: # Verifica se o elemento anterior no intervalo de gap posições é maior do que o elemento atual temp.
                comp += 1
                livros[j] = livros[j-gap]
                trocas += 1
                j -= gap
            if j >= gap and livros[j-gap] != temp:
                comp += 1
            livros[j] = temp
        gap //= 2 # O gap é reduzido pela metade
        
    return comp, trocas, livros # Retorno das variáveis atualizadas

# _________________________________________________________________________________________________
# Algoritmo Quicksort utiliza a estratégia de dividir e conquistar, onde a lista é dividida em sub-listas menores, ordenadas individualmente e combinadas para formar a lista final ordenada.
def quick_sort(livros, ind_esq, ind_dir):
    comp = 0 
    trocas = 0
  
    def partition(livros, ind_esq, ind_dir):
        nonlocal comp, trocas 
        pivot = livros[(ind_dir + ind_esq) // 2]
        i = ind_esq
        j = ind_dir
        while True:
            if i >= j:
                return j
            while livros[i] < pivot:
                i += 1
                comp += 1 
            while livros[j] > pivot:
                j -= 1
                comp += 1 
            livros[i], livros[j] = livros[j], livros[i]
            trocas += 1 

    if ind_esq >= 0 and ind_dir >= 0 and ind_esq < ind_dir:
        p = partition(livros, ind_esq, ind_dir)
        comp_esq, trocas_esq, livros_esq = quick_sort(livros, ind_esq, p)
        comp_dir, trocas_dir, livros_dir = quick_sort(livros, p + 1, ind_dir)
        comp += comp_esq + comp_dir
        trocas += trocas_esq + trocas_dir
        livros = livros_esq + livros[p:p+1] + livros_dir

    return comp, trocas, livros



#_________________________________________________________________________________________________
# Entrada dos livros
livros = []
for item in input().split():
    livros.append(int(item))

# Classificando os personagens usando cada algoritmo e imprime os resultados
comp_bubble, trocas_bubble, livros_bubble = bubble_sort(livros.copy()) # As variáveis recebem o número de comparações e de trocas e a lista ordenada dos livros.
print(f'Caça-Rato ordena a lista com {comp_bubble} comparações e {trocas_bubble} trocas.')

comp_selection, trocas_selection, livros_selection = selection_sort(livros.copy())
print(f'Grafite ordena a lista com {comp_selection} comparações e {trocas_selection} trocas.')

comp_insertion, trocas_insertion, livros_insertion = insertion_sort(livros.copy())
print(f'Lacraia ordena a lista com {comp_insertion} comparações e {trocas_insertion} trocas.')

comp_shell, trocas_shell, livros_shell = shell_sort(livros.copy())
print(f'Rivaldo ordena a lista com {comp_shell} comparações e {trocas_shell} trocas.')

comp_quick, trocas_quick, livros_quick = quick_sort(livros.copy(), 0, len(livros) - 1)
print(f'Toninho ordena a lista com {comp_quick} comparações e {trocas_quick} trocas.')

# Determinando o vencedor
acao_bubble = comp_bubble + trocas_bubble
acao_selection = comp_selection + trocas_selection
acao_insertion = comp_insertion + trocas_insertion
acao_shell = comp_shell + trocas_shell
acao_quick = comp_quick + trocas_quick

acao = [acao_bubble, acao_selection, acao_insertion, acao_shell, acao_quick]
names = ['Caça-Rato', 'Grafite', 'Lacraia', 'Rivaldo', 'Toninho']

ganhador = (acao[0], names[0])  # Inicia o vencedor com o primeiro elemento da lista
for i in range(1, len(acao)):
    if acao[i] < ganhador[0]:
        ganhador = (acao[i], names[i])


# Print ganhador
print('-VENCEDOR FINAL-')
print(f'O vencedor final é {ganhador[1]}, com {ganhador[0]} ações.')


# Executando a segunda rodada
for estagiario in [('Caça-Rato', livros_bubble), ('Grafite', livros_selection),
('Lacraia', livros_insertion), ('Rivaldo', livros_shell)]:
    
    if estagiario[0] != ganhador:
        comp, trocas, livros_interrup = quick_sort(estagiario[1], 0, len(estagiario[1]) - 1)

        print(f'Com {comp_quick+trocas_quick} ações {estagiario[0]} ordena a lista assim: {livros_interrup}.')
    else:
        print('-Toninho está a dormir...-')


