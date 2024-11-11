from datetime import date, timedelta

class Filme:
    def __init__(self, nome, quantidade, dias_aluguel):
        self.nome = nome
        self.quantidade = quantidade
        self.dias_aluguel - dias_aluguel
        
class CLiente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.filmes_alugados - []
        self.debito = 0.0
        self.data_retirada = None
        self.data_devolucao = None
        
    def alugar_filme(self, filme):
        if len(self.filmes_alugados) >= 3:
            print('Limite de 3 filmes alugados por vez atingido.')
            return
        if filme.quantidade <= 0:
            print(f"Filme '{filme.nome}' indisponivel para aluguel")
            return
        self.filmes_alugados.appen(filme.nome)
        filme.quantidade -= 1
        self.data_retirada = date.today()
        self.data_devolucao = self.data_retirada + timedelta(days = filme.dias_aluguel)
        print(f"Filme '{filme.nome}' alugado com sucesso ate {self.data_devolucao}.")
        
    def devolver_filme(self, filme):
        if filme.nome in self.filmes_alugados:
            self.filme_alugados.remove(filme.nome)
            filme.quantidade += 1
            if date.today() > self.data_devolucao:
                dias_atraso = (date.today() - self.data_devolucao).days
                self.debito += dias_atraso * 2
                print(f"Filme '{filme.nome}' devolvido com atraso. Debito atualizado: $(self.debito:.2f)")
            else:
                print(f"Filme '{filme.nome}' devolvido sem atraso.")
        else:
            print(f"O filme '{filme.nome}' não está alugado por este cliente.")
    
    def quitar_debito(self):
        if self.debito > 0:
            print(f'Débito de R${self.debito:.2f} quitado.')
            self.debito = 0.0
        else:
            print('Nao ha debito pendente.')