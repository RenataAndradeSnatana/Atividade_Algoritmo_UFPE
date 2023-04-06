quant_espaco_mem = int(input())  # Entrada para a quantidade de espaços de memória disponíveis.
comandos = int(input())  # Entrada para a quantidade de comandos a serem executados.
memoria = [None] * quant_espaco_mem  # Variável que representa uma lista inicialmente vazia conforme quantidade de memória

for i in range(comandos): # For que itera conforme a qunatidade de (comandos) informado
    cmd = input().split() # Entrada dos comandos no formato de lista
    
    #-------------------------- Inicio de verificação dos comandos de entrada
    if cmd[0] == 'ADD': 
        valor = int(cmd[1])  # Variável que armazenará o valor da posição 1 da entrada cmd a ser adicionado na memória da entrada cmd
        posicao = valor % quant_espaco_mem  # Calculo da (posição) da memória em que o dado será armazenado para diminuir colisões
        
        while memoria[posicao] != None:  # Verificação de espaço livre
            posicao = (posicao + 1) % quant_espaco_mem # Caso a posição já esteja ocupado o cáculo busca a próxima posição livre na memória
        memoria[posicao] = valor
        print('E:', posicao)
        
    elif cmd[0] == 'SCH':
        busca = int(cmd[1]) # Variável que armazena o valor do segundo argumento passado no comando
        posicao = busca % quant_espaco_mem  # Calculo que busca a posição usando a função hash
        
        while (memoria[posicao] != None) and (memoria[posicao] != busca): # Faz a verificação para encontrar o valor desejado
            posicao = (posicao + 1) % quant_espaco_mem # Pecorrendo toda a lista caso com base nesse cálulo
        if memoria[posicao] == busca:
            print('E:', posicao)
        else:
            print('NE')
            
    elif cmd[0] == 'CAP': # Verifica se o comando é para alterar a capacidade da tabela de dispersão.
        comandos = int(cmd[1])
        if memoria[comandos] == None:
            print('D')
        else:
            print('A:', memoria[comandos])
    #-------------------------- Fim de verificação dos comandos de entrada   
         
    if memoria.count(None) == 0:  # Verifica se há espaço livre na mémoria
        print('Toda memoria utilizada')
        break
