from Filme_locadora import Filme, Cliente
import random
from datetime import date, timedelta

def main():
    catalogo_filme = [
        Filme('Avatar', 1, 7),
        Filme('Avatar 2', 2, 3),
        Filme('Avatar 3', 3, 5),
        Filme('Avatar 4', 4, 2),
        Filme('Avatar 5', 1, 1)
    ]
    
    #criacao de um cliente.
    cliente = Cliente('Pedrinho', 123456789)
    
    #se houver, quitar debitos.
    cliente.quitar_debito()
    
    #alugar Filmes.
    filmes_para_alugar = random.sample(catalogo_filme, 3) #escolha de 3 filmes.
    for filme in filmes_para_alugar:
        cliente.alugar_filme(filme)
        
    #Tenta devolver um filme com atraso.        
    cliente.data_devolucao = date.today() - timedelta(days = 1) #simulacao de dias de atraso.
    cliente.devolver_filme(filmes_para_alugar[0])
    
    
if __name__ == '__main__':
    main()