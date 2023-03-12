n = int(input())  # quantidade de espaços de memória disponíveis
m = int(input())  # quantidade de comandos a serem executados
memory = [None] * n  # array de memória
for i in range(m):
    cmd = input().split()
    if cmd[0] == 'ADD':
        x = int(cmd[1])
        idx = x % n  # calcula o índice do slot usando a função hash
        while memory[idx] is not None:  # faz sondagem linear para encontrar um slot livre
            idx = (idx + 1) % n
        memory[idx] = x
        print('E:', idx)
    elif cmd[0] == 'SCH':
        d = int(cmd[1])
        idx = d % n  # calcula o índice do slot usando a função hash
        while memory[idx] is not None and memory[idx] != d:  # faz sondagem linear para encontrar a chave
            idx = (idx + 1) % n
        if memory[idx] == d:
            print('E:', idx)
        else:
            print('NE')
    elif cmd[0] == 'CAP':
        m = int(cmd[1])
        if memory[m] is None:
            print('D')
        else:
            print('A:', memory[m])
    if None not in memory:  # verifica se há espaço livre no array
        print('Toda memoria utilizada')
        break
