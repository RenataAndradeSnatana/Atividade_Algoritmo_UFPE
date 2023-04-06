

import random   # importação da biblioteca random para trabalharmos com números aleatórios

def retorno_numero_magico(): # Função para gerar número aletório 
    return random.randint(30, 990) # entre 30 e 990 através o randint


def processamento_CPF(cpf): # Função recebe o cpf e realiza o processamento dele
    digitos = []
    for digito in cpf:
        digitos.append(int(digito) * 10)  # Multiplica cada dígito por 10 e adiciona à lista
    if len(set(digitos)) != len(digitos): # Verifica se existe números repetidos comparando e usando a função set()
        digitos_sem_repeticao = []  # Cria uma nova lista para os dígitos sem repetição
        for digito in set(digitos):  # Para cada dígito, soma os dígitos iguais na lista original
           soma = 0
           for digito_repet in digitos:
                if digito_repet == digito:
                    soma += digito_repet
           digitos_sem_repeticao.append(soma)
                
        digitos = digitos_sem_repeticao  # Substitui a lista original pela nova lista de dígitos sem repetição
    return digitos

def permissao(cpf, numero_magico, tabela_CPF): # Função que verificar se um CPF possui permissão recebendo como argumentos o CPF do usuário (cpf), um número mágico (numero_magico) e uma tabela hash (tabela_CPF). 
    digitos = []
    for item in tabela_CPF:
        if item[0] == cpf:
            digitos = item[1]
            break
        else:  # CPF não encontrado na tabela hash
            digitos = processamento_CPF(cpf)
            tabela_CPF.append((cpf, digitos))  # Adiciona entrada na tabela hash
        
    if digitos == 0: # CPF inválido
        return False
    else:
        for i in range(len(digitos)):
            for j in range(i+1, len(digitos)):
                if digitos[i] + digitos[j] == numero_magico:
                    return True
        return False

n = int(input()) # Número de entrada de CPFs
tabela_CPF = []  # Cria tabela hash vazia
for i in range(n):  # for que irá ser processado n vezes a quantidade de CPFs que será informado
    entrada_CPF_Nmag = input().split() # Entrada do CPF e número mágico que serão armazenado como lista tupla
    cpf = entrada_CPF_Nmag[0]
    numero_magico = int(entrada_CPF_Nmag[1])
    
    if permissao(cpf, numero_magico, tabela_CPF): # Chamando a função permissao que verificará se o CPF possui permissão com base no número mágico
            print("UP Permission")
    else:
        print("NOT Permission")
