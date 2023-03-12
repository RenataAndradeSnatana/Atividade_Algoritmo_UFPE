class No: # Classe que representa um nó da árvore.
    
    def __init__(self, valor):
        self.valor = valor  # Valor do nó.
        self.esquerda = None # Filho a esquerdo do nó
        self.direita = None # Filho a direita do nó.
        self.avô_do_no = None # O nó pai do pai do nó

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None # função que armazenar o nó raiz da árvore

  
    def Rotacionar_esquerda(self, no=None, pai_do_no=None): # A função recebe dois argumentos no=None e pai_do_no=None
                                                            # no ->  será rotacionado
                                                            # pai_do_no ->  o pai desse nó (no)
                                                            
        if pai_do_no == self.raiz: # Se o pai do nó for igual a raiz
            no_a_esquerda = no.esquerda  # o nó à esquerda do nó (no) é atribuido à variável no_a_esquerda
                                            
            no.esquerda = pai_do_no # - Processo de rotação
            no.avô_do_no = pai_do_no.avô_do_no      #
            pai_do_no.avô_do_no = no                #
            pai_do_no.direita = no_a_esquerda # - Processo de rotação
               
            if no_a_esquerda:  # Atualização dos no(s)
                no_a_esquerda.avô_do_no = pai_do_no
                self.raiz = no

        else:
            no_a_esquerda = no.esquerda      
            no.esquerda = pai_do_no  # - Processo de rotação
            no.avô_do_no = pai_do_no.avô_do_no       #
            pai_do_no.avô_do_no = no                 #
            pai_do_no.direita = no_a_esquerda # - Processo de rotação

            if no_a_esquerda:  # no_a_esquerda exitir ele é definido como o pai do nó
                no_a_esquerda.avô_do_no = pai_do_no
                
            if no.avô_do_no.valor > no.valor: # - Verificação do lado em que o nó está em relação ao seu novo pai
                no.avô_do_no.esquerda = no                              #
                self.rotacionar_direita(no, no.avô_do_no)               #
            else:                                                       #
                no.avô_do_no.direita = no                               #
                self.Rotacionar_esquerda(no, no.avô_do_no) # - Verificação do lado em que o nó está em relação ao seu novo pai

    def rotacionar_direita(self, no=None, pai_do_no=None): # A função recebe dois argumentos no=None e pai_do_no=None
                                                           # - no ->  será rotacionado
                                                           # - pai_do_no ->  o pai desse nó (no)
        if pai_do_no == self.raiz:
            no_a_esquerda = no.direita
            no.direita = pai_do_no  # - Processo de rotação
            no.avô_do_no = pai_do_no.avô_do_no     #
            pai_do_no.avô_do_no = no               #
            pai_do_no.esquerda = no_a_esquerda # - Processo de rotação

            if no_a_esquerda:  # # Atualização dos no(s)
                no_a_esquerda.avô_do_no = pai_do_no
                self.raiz = no

        else:
            no_a_esquerda = no.direita
            no.direita = pai_do_no # - Processo de rotação
            no.avô_do_no = pai_do_no.avô_do_no     #
            pai_do_no.avô_do_no = no               #
            pai_do_no.esquerda = no_a_esquerda # - Processo de rotação

            if no_a_esquerda: # no_a_esquerda exitir ele é definido como o pai do nó
                no_a_esquerda.avô_do_no = pai_do_no

            if no.avô_do_no.valor > no.valor:   # - Verificação do lado em que o nó está em relação ao seu novo pai
                no.avô_do_no.esquerda = no                                       #
                self.rotacionar_direita(no, no.avô_do_no)                        #
            else:                                                                #
                no.avô_do_no.direita = no                                        #
                self.Rotacionar_esquerda(no, no.avô_do_no)  # - Verificação do lado em que o nó está em relação ao seu novo pai

    def add(self, valor): # função que adiciona um novo nó na árvore, a partir do valor recebido.
        no_pai = None
        posicao = -1  # Inicia com -1 para que o primeiro nó adicionado na árvore seja posição zero 
        no = self.raiz

        while no != None:
            no_pai = no
            if valor < no.valor: # Se o valor for menor que o valor do nó atual o no ficará ó no a esqueda
                no = no.esquerda
                posicao += 1 # posição incrementada em 1
            elif valor > no.valor: # Caso contrário o no ficará no nó a direita
                no = no.direita
                posicao += 1

        if no_pai == None: # Se no_pai for Nome
            self.raiz = No(valor) # A raiz será o novalor
            return posicao + 1

        elif valor < no_pai.valor: # Se o valor for menor que no_pai.valor o novo nó é adicionado como filho esquerdo do nó pai
            no_pai.esquerda = No(valor)
            no_pai.esquerda.avô_do_no = no_pai
            return posicao + 1

        else:
            no_pai.direita = No(valor) # Caso contrário o novo nó é adicionado como filho direirta do nó pai
            no_pai.direita.avô_do_no = no_pai
            return posicao + 1

    def busca(self, valor): # Essa função busca um valor específico na árvore.
       
        no = self.raiz
        posicao = -1 # Contador
        
        if no != None:
            while no and no.valor != valor: # Enquanto o nó não for o valor desejado ....

                if no.valor > valor: # Entrando na parte esquerda da árvore
                    posicao += 1
                    no = no.esquerda
                
                elif no.valor < valor: # Entrando na parte direita da árvore
                    posicao += 1
                    no = no.direita  
                          
        if no != None: # Caso o nó seja encontrado
            return no, no.avô_do_no, posicao + 1 
        
        else: # Caso o nó não seja encontrado
            return False

abb = ArvoreBuscaBinaria()

try:
    while True:
                               
        entrada = input().split()  # Recebendo os inputs :
        palavra = entrada[0]
        valor = int(entrada[1])
        
        # Checando os comandos :
        if palavra =='ADD':
            print(abb.add(valor))

        elif palavra =='SCH':
            if abb.busca(valor) == False: # Caso não esteja presente na árvore
                print(-1)
            
            else: # Caso o valor esteja na árvore.
                if valor == abb.raiz.valor: # Se o valor buscado for a raiz da árvore (melhor caso possível)
                    print(0)

                else: # Se o valor não for a raiz...

                    no_desejado = abb.busca(valor) # Buscando o valor

                    if no_desejado[0].valor < no_desejado[1].valor: # Se o valor do nó desejado for maior que o valor do nó pai
                     
                        print(no_desejado[2])
                        abb.rotacionar_direita(no_desejado[0],no_desejado[1])

                    else: # Se o valor desejado for menor que o valor do nó pai
                        print(no_desejado[2])
                        abb.Rotacionar_esquerda(no_desejado[0],no_desejado[1])
except:
    pass


