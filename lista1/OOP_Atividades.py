# Exercícios
# 1 - 

class Nota:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome      
        
    
    def inicializarNota(self, nota1: float, nota2: float, nota3: float):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    
    
    def verificaSituacaoMedia(self, atributo = True):
        media = (self.nota1 + self.nota2 + self.nota3)/3
        if media >= 7:
            print('apvado')
            return True
        elif media <= 7:
            print('repvado')
            return False
        
        else:
            return atributo == False
    
    def imprimeInformacoes(self):
        print(self.nome, self.cpf, self.nota1, self.nota2, self.nota3 )
            
dados = Nota('052.104.304-21','Renata')   
dados.inicializarNota(6, 6, 6)

print(dados.verificaSituacaoMedia)




    # def imprimeInformacoes():