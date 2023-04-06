# Leitura da entrada
livros = list(map(int, input().split()))

# Bubble Sort
def bubbleSort(livros):
    n = len(livros)
    comp = 0
    trocas = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comp += 1
            if livros[j] > livros[j+1] :
                livros[j], livros[j+1] = livros[j+1], livros[j]
                trocas += 1
    return comp, trocas

# Selection Sort
def selectionSort(livros):
    n = len(livros)
    comp = 0
    trocas = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comp += 1
            if livros[min_idx] > livros[j]:
                min_idx = j
        if min_idx != i:
            livros[i], livros[min_idx] = livros[min_idx], livros[i]
            trocas += 1
    return comp, trocas

# Insertion Sort
def insertionSort(livros):
    n = len(livros)
    comp = 0
    trocas = 0
    for i in range(1, n):
        key = livros[i]
        j = i-1
        while j >= 0 and key < livros[j]:
            comp += 1
            livros[j+1] = livros[j]
            j -= 1
            trocas += 1
        livros[j+1] = key
        trocas += 1
    return comp, trocas

# Shell Sort
def shellSort(livros):
    n = len(livros)
    comp = 0
    trocas = 0
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = livros[i]
            j = i
            while j >= gap and livros[j-gap] > temp:
                comp += 1
                livros[j] = livros[j-gap]
                j -= gap
                trocas += 1
            livros[j] = temp
            trocas += 1
        gap //= 2
    return comp, trocas

# Quicksort
def partition(livros, low, high):
    i = (low-1)
    pivot = livros[high]
    for j in range(low, high):
        if livros[j] <= pivot:
            i = i+1
            livros[i], livros[j] = livros[j], livros[i]
    livros[i+1], livros[high] = livros[high], livros[i+1]
    return (i+1)

def quickSort(livros, low, high):
    comp = 0
    trocas = 0
    if low < high:
        pi = partition(livros, low, high)
        compL, trocasL = quickSort(livros, low, pi-1)
        compR, trocasR = quickSort(livros, pi+1, high)
        comp = compL + compR + high - low
        trocas = trocasL + trocasR + high - low
    return comp, trocas


# Execução
comp_bubble, trocas_bubble = bubbleSort(livros.copy())
comp_selection, trocas_selection = selectionSort(livros.copy())
comp_insertion, trocas_insertion = insertionSort(livros.copy())
comp_shell, trocas_shell = shellSort(livros.copy())
comp_quick, trocas_quick = quickSort(livros.copy(), 0, len(livros)-1)

# Saída

print(f"Caça-Rato ordena a lista com {comp_bubble} comparacoes e {trocas_bubble} trocas.")
print(f"Grafite ordena a lista com {comp_selection} comparacoes e {trocas_selection} trocas.")
print(f"Lacraia ordena a lista com {comp_insertion} comparacoes e {trocas_insertion} trocas.")
print(f"Rivaldo ordena a lista com {comp_shell} comparacoes e {trocas_shell} trocas.")
print(f"Toninho ordena a lista com {comp_quick} comparacoes e {trocas_quick} trocas.")

# aplicar os algoritmos de ordenação
quick_sort_helper(lista, 0, len(lista)-1)
merge_sort(lista)
selection_sort(lista)

# comparar os resultados e determinar o vencedor
if lista == sorted(lista):
    print("Os algoritmos foram aplicados corretamente e todos produziram a mesma lista ordenada.")
else:
    print("Os resultados dos algoritmos são diferentes.")
    
# aplicar novamente os algoritmos dos estagiários que perderam, com a quantidade de ações do vencedor
if lista == sorted(lista):
    num_actions = len(lista) * math.log(len(lista))
    print(f"O vencedor gastou {num_actions} ações para ordenar a lista.")
    for estagiario in estagiarios_perdedores:
        estagiario(num_actions)