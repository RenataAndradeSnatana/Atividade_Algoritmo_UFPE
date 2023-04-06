
#-------------------------------------------------------------------------------------

def busca_em_largura(grafo_usuarios, id_usuario, orcamento): # Função que busca os usuários conectados dentro de um limite de orçamento
    usuarios_alcancados = []
    visitados = set() # Visitados na busca em largura sem duplicação
    fila = [] # Fila de nós para visitar
    fila.append((id_usuario, 1)) # É adicionado na fila o usuario e o (1) nível do nó, na busca em largura.
    visitados.add(id_usuario) # Adiciona os id_usuario em visitados
    custo_boost = 0 # Variavél que armazena o valor inicial do custo do 'boost'
    filhos = grafo_usuarios[id_usuario] # Essa variável vai ter os vértices adjacentes ao vértice id_usuario no grafo grafo_usuarios
    usuarios_gratuitos = len(filhos)
    
    while len(fila) > 0: # Enquanto a fila não estiver vazia
        no_usuario_visitado, nivel = fila.pop(0) # retira da fila o primeiro nó a ser visitado na busca em largura e armazenar seus valores nas variáveis no_usuario_visitado e nivel.
        
        if custo_boost < orcamento: # Garanti que o custo do "boost" não ultrapasse o orçamento
           
            if nivel == 1 or custo_boost + 5.25 <= orcamento: # Se um determinado nó pode ser adicionado à lista de usuários alcancados, ou se é necessário parar a busca
                
                if no_usuario_visitado != id_usuario and no_usuario_visitado not in usuarios_alcancados: # Se o usuário visitado é diferente do usuário inicial (id_usuario) e se ele ainda não foi adicionado à lista de usuários alcançados 
                    
                    # Adiciona o usuário alcançado na lista
                    if nivel > 1: # Verifica se o nó visitado na busca em largura não é o nó inicial (nível 1)
                        usuarios_alcancados.append(str(no_usuario_visitado)) # Adiciona o usuário alcançado na lista
                    
                    # Verifica se o usuário é gratuito ou não
                    if usuarios_gratuitos > 0: # Se ainda existem seguidores que podem ser visitados sem a necessidade de usar o "boost
                        usuarios_gratuitos -= 1
                    else:
                        custo_boost += 5.25
            else:
                break
        
        # Realiza a visita aos vizinhos do nó atualmente sendo visitado na busca em largura e adiciona esses vizinhos na fila para serem visitados posteriormente.
        for vizinho in grafo_usuarios[no_usuario_visitado]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, nivel + 1))
                
    return usuarios_alcancados

#-------------------------------------------------------------------------------------
# Leitura da entrada
numero_usuario = int(input())
id_usuario = int(input())
valor_investido_boost = int(input())
grafo_usuarios = {}
for i in range(numero_usuario):
    linha = input().split(":")
    usuario = int(linha[0])
    seguidores = [int(x) for x in linha[1].split() if x != ""]
    grafo_usuarios[usuario] = seguidores
    
# Executa a busca em largura a partir do usuário que fez a publicação
usuarios_alcancados = busca_em_largura(grafo_usuarios, id_usuario, valor_investido_boost)

# Imprime os usuários alcançados
print(usuarios_alcancados)
#-------------------------------------------------------------------------------------