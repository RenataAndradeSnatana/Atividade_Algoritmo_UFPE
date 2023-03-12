def pilhaImaculada(pilha): # Verificar se a pilha está ordenada
    for i in range(len(pilha) - 1):
        if pilha[i] >= pilha[i + 1]:
            return False
    return True

def novaLocacao(pilha, novo_codigo): # função percorre a pilha e inserir o novo_código na posição correta
    for i in range(len(pilha)):
        if novo_codigo < int(pilha[i]):
            pilha.insert(i, str(novo_codigo))
            return pilha
    pilha.append(str(novo_codigo))
    return pilha

pilha = input().split(",")
novo_codigo = input()

if pilhaImaculada(pilha):
    nova_pilha = novaLocacao(pilha, int(novo_codigo))
    print(nova_pilha)
else:
    print("A pilha está um caos.")
