# # Função que busca todos os amigos de cada pessoa, e todos os amigos de amigos que ouviram a fofoca.
# def busca_profundidade_dfs(fofoqueiro, ja_sabe, lista_fofoqueiro, noticia_velha):
#     ja_sabe[fofoqueiro] = True # Indica que a pessoa já sabe da fofoca
#     noticia_velha[fofoqueiro] = True # Já ouviu a fofoca
#     for fofoca in lista_fofoqueiro[fofoqueiro]:
#         if ja_sabe[fofoca] == False:
#             dfs(fofoca, ja_sabe, lista_fofoqueiro, noticia_velha) # Chama a função dfs
# # _________________________________________________________________________________________________
# # Entrada
# usuários, conex_amizade = input().split()
# usuários = int(usuários)
# conex_amizade = int(conex_amizade)

# #__________________________________________________________________________________________________
# #Corpo do programa
# lista_fofoqueiro = [] # Criando uma lista vazia conforme a quantidade de usuários(vérices)
# for i in range(usuários):
#     lista_fofoqueiro.append([]*usuários)
    
# for _ in range(conex_amizade): # Loop que será executado conforme a variável conex_amizade
#     '''obs.: quando se usa '_' é porque precisamos da variável, mas não precisa do valor que ela armazena.'''
#     fofoca, fofoqueiro  = input().split()
#     fofoca = int(fofoca)
#     fofoqueiro = int(fofoqueiro )
#     lista_fofoqueiro[fofoca-1].append(fofoqueiro-1)
#     lista_fofoqueiro[fofoqueiro-1].append(fofoca-1)
    
# resultado_fofoca = [] # Lista que será utilizada para armazenar o resultado do número de usuários que saberiam a notícia se cada usuário começasse a contar a fofoca
# print('resultado_fofoca',resultado_fofoca)
# for i in range(usuários): # Interação de usuários vezes 
#     resultado_fofoca.append(0)
    
# for i in range(usuários):
#     ja_sabe = [False] * usuários
#     noticia_velha = [False] * usuários
#     dfs(i, ja_sabe, lista_fofoqueiro, noticia_velha)
#     resultado_fofoca[i] = sum(noticia_velha)

# print(' '.join(str(x) for x in resultado_fofoca))
# #__________________________________________________________________________________________________
# #Fim

#_____________________________________________________________________________
# 
def busca_profundidade_dfs(usuarios, lista_conx, vetor): # Usuarios-> nó inicial, lista_conx-> lista de adjacências e vetor-> usado para controlar quais nó(s) já foram visitados.
    vetor[usuarios] = True # Marca o nó usuarios como visitado
    contador = 1 # Usado para contar quantos nós foram visitados
    for amigo in lista_conx[usuarios]: # Itera sobre cada nó adjacente ao nó usuarios na lista de adjacências lista_conx.               
        if vetor[amigo] == False: # Se o nó adjacente amigo ainda não foi visitado
            temp = busca_profundidade_dfs(amigo, lista_conx, vetor) # Armazena o número de nós visitados a partir do nó amigo
            contador += temp
    return contador
#_____________________________________________________________________________
# Entrada
num_usuario, num_conexoes = input().split()
num_usuario = int(num_usuario)
num_conexoes = int(num_conexoes)

#______________________________________________________________________________
#Corpo do programa
lista_conx = []
for i in range(num_usuario + 1):
    lista_conx.append(list()) # Adiciona uma nova lista vazia a lista_conx

# Ler as conexões entre os nós do grafo e preenche a lista adjacências, lista_conx.   
for variavel in range(num_conexoes):
    entrada = input()
    valores = entrada.split()
    par1 = int(valores[0])
    par2 = int(valores[1])
    lista_conx[par1].append(par2)
    lista_conx[par2].append(par1)

resultado_compartilhamento = []
for prim_elem in range(1, num_usuario + 1):
    vetor = [False] * (num_usuario + 1)
    resultado_compartilhamento.append(busca_profundidade_dfs(prim_elem, lista_conx, vetor)) # A busca é um número inteiro que representa a quantidade de usuários que estão diretamente ou indiretamente conectados ao usuário

print(' '.join(str(x) for x in resultado_compartilhamento))
#_______________________________________________________________________________
#Fim