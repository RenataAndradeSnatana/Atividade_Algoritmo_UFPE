
# Função do algoritmo Mergesort
def merge_sort(lista_da_esquerda, lista_da_direita):
    resultado = [] # Lista que receberá o resultado da divisão dos elementos da array de entrada
    indice_esd = 0
    indice_dir = 0

    '''Comparação dos elementos das arrays lista_da_esquerda e lista_da_direita e adiciona o menor deles ao array resultado.'''
    while indice_esd < len(lista_da_esquerda) and indice_dir < len(lista_da_direita): # Dessa forma pecorre todos os elementos da direita e esquerda
        
        if lista_da_esquerda[indice_esd] < lista_da_direita[indice_dir]:
            resultado.append(lista_da_esquerda[indice_esd])
            indice_esd += 1
        
        else:
            resultado.append(lista_da_direita[indice_dir])
            indice_dir += 1

    resultado += lista_da_esquerda[indice_esd:]
    resultado += lista_da_direita[indice_dir:]

    return resultado

# Calcula a mediana dos salários dos jogadores de futebol, a partir de duas listas de salários dos clubes 
def salario_medio(salario_jogadores, salario_futuro):
    lista_ordenada = merge_sort(salario_jogadores, salario_futuro) # Essa variável vai conter todos os elementos das duas arrays originais e ordenados em ordem crescente através da função merge_sor
    tamanho_array= len(lista_ordenada)
    meio = tamanho_array // 2  # Calculo da mediana dessa lista ordenada

    if tamanho_array % 2 == 0:
        mediana = (lista_ordenada[meio-1] + lista_ordenada[meio]) / 2 # A mediana é a média aritmética dos dois elementos do meio da lista
    
    else:
        mediana = lista_ordenada[meio] # A mediana é o valor do elemento central da lista.

    return f"O salário sugerido por Juba na primeira negociação será de {mediana:.2f} mil reais."


# Entradas
salario_jogadores = []
for salario in input().split():
    salario_jogadores.append(int(salario))
    
salario_futuro = []
for salario in input().split():
    salario_futuro.append(int(salario))
    

lista_ordenada = merge_sort(salario_jogadores, salario_futuro)

# Calculo da mediana da lista ordenada e usando a função salario_medio.
mediana_indice = len(lista_ordenada) // 2
mediana = salario_medio(lista_ordenada[:mediana_indice], lista_ordenada[mediana_indice:])

print(mediana)
