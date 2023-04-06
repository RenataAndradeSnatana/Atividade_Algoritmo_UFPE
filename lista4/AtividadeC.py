
def remove_maior_valor(entrada): # Função para remover o maior valor da sequência e retornar a nova sequência
    
    maior_valor = entrada[0] # Armazenar o maior valor encontrado na sequência entrada
    maior_indice = 0 # Armazena o índice do maior valor encontrado na sequência
    
    # for que percorre a sequência para encontrar o maior valor
    for i in range(1, len(entrada)): # O range começa com 1 pq porque a variável maior_valor foi inicializada com o valor do primeiro elemento da sequência.
        
        if entrada[i] > maior_valor:
            maior_valor = entrada[i]
            maior_indice = i
    
    # Remove o maior valor encontrado na sequência 'entrada' e atualiza a sequência sem esse valor.        
    valor = entrada[maior_indice]
    entrada[maior_indice] = entrada[-1]
    entrada[-1] = valor
    maior_valor = entrada.pop()
    
    if entrada == []: # Garanti que a lista 'entrada' sempre tenha pelo menos um elemento após a remoção do maior valor evitando o loop infinito
        return entrada, maior_valor
    
    return entrada, maior_valor

# Leitura da entrada
entrada_str = input().split() # Entrada das seuqência de números
entrada = []
for elem in entrada_str:
    entrada.append(int(elem)) 

constante = int(input()) # Entrada da constante

# Criação da Heap máxima e encontra o menor valor
tamanho_lista = len(entrada)
primeiro_elemento = entrada[0]

for i in range(1, tamanho_lista): # Interra com todos os elementos da lista exceto o primeiro
    if entrada[i] < primeiro_elemento:
        primeiro_elemento = entrada[i]
            
for i in range(((tamanho_lista // 2) - 1), -1, -1): 
    ''' Primeira posição a ser verificada é "(n // 2) - 1" que representa posição do último pai na Heap. 
    "-1" representa é primeira posição da lista. E o outro "-1" representa a inversão de funcioanamento do loop, 
    começando de trás para frente''' 
    
    j = i
    
    while 2 * j + 1 < tamanho_lista: # Enquanto o filho da esquerda existe e for menor que o tamanho da lista
        
        k = 2 * j + 1 # # k recebe o índice do filho da esquerda
        
        if k + 1 < tamanho_lista and entrada[k+1] > entrada[k]: # K + 1 é o índice do filho da direita do nó atual "j"
            k += 1  #  k é atualizado e aponta para o filho da direita.
            
        if entrada[k] > entrada[j]: # Verifica se o valor do filho escolhido é maior do que o valor do pai
            entrada[j], entrada[k] = entrada[k], entrada[j] # Se for os valores dos nó(s) são trocados 
            j = k  # j é atualizada e aponta para o índice do nó trocado
            
        else:
            break

# Jogo
rodada = 1

while entrada != []:
    retorno_funcao = remove_maior_valor(entrada)
    entrada = retorno_funcao[0]
    maior_valor = retorno_funcao[1]
    
    quant_pontos = maior_valor - abs(primeiro_elemento * constante)
    
    if quant_pontos > 0:
        entrada.append(quant_pontos)
        
        # Atualização da Heap
        ultima_posicao = len(entrada) - 1
        
        while ultima_posicao > 0:
            posicao_pai = (ultima_posicao - 1) // 2
            
            if entrada[ultima_posicao] > entrada[posicao_pai]:
                entrada[ultima_posicao], entrada[posicao_pai] = entrada[posicao_pai], entrada[ultima_posicao]
                ultima_posicao = posicao_pai
            
            else:
                break
    
    # Atualizando o menor valor
    if entrada != []:
        primeiro_elemento = entrada[0]
        
        for i in range(1, len(entrada)):
            if entrada[i] < primeiro_elemento:
                primeiro_elemento = entrada[i]
                
    rodada += 1

# Saída
print(f"{rodada-1} rodadas, partindo para a próxima!")
