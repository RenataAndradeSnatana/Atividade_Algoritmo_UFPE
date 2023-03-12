caderno = input().strip()

posicoesF = []
posicoesV = []

# Essa interação é para alimentar as listas posicoesF e posicoesV conforme a entrada caderno
for i in range(len(caderno)): # Esse for adiciona a string 'F' na lista posicoesF e 'V' na lista posicoesV.
    if caderno[i] == 'F':
        posicoesF.append(i)
    elif caderno[i] == 'V':
        posicoesV.append(i)

tudocerto = True # Variável para verificar se a resposta está correta ou não

# Essa loop será executado conforme a lista posicoesF.
while posicoesF: 
    posicao_f = posicoesF.pop(0) # A posição da página frente(posicao_f) será dada pela eliminação de cada elementos de lista posicoesF
    if posicoesV == []:
        print(f"Incorreto, devido a capa na posição {posicao_f+1}.")
        tudocerto = False # Caso haja erro, muda a variável para "False"
        break
    posicao_v = posicoesV.pop(0) # A posição da página frente(posicao_v) será dada pela eliminação de cada elementos de lista posicoesV
    if posicao_f > posicao_v: # Verificação de posição das páginas frente é maior que as de versos
        print(f"Incorreto, devido a capa na posição {posicao_f}.")
        tudocerto = False # Caso haja erro, muda a variável para "False"
        break


if not posicoesF and posicoesV:
  print(f"Incorreto, devido a capa na posição {posicoesV[0]+1}.")

elif tudocerto == True:
  print("Correto.")
  

