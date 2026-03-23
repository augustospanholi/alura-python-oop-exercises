# 1- Crie uma classe chamada Livro com um construtor que aceita os parametros titulo, autor e
# ano_publicacao.
# Inicie um atributo chamado disponivel como True por padrao.

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self._titulo = titulo
#         self._autor = autor
#         self._ano_publicacao = ano_publicacao
#         self._disponivel = True

# 2 - Na classe Livro, adicione um metodo especial str que retorna uma mensagem formatada com o
# titulo, autor e ano de publicacao do livro.
# Crie duas instancias da classe Livro e imprima essas instancias.

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self._titulo = titulo
#         self._autor = autor
#         self._ano_publicacao = ano_publicacao
#         self._disponivel = True
#
#     def __str__(self):
#         return f"Titulo: {self._titulo} | Autor: {self._autor} | Ano de publicacao: {self._ano_publicacao}"
#
# livro1 = Livro("Sovando latas", "ET 1155", "2026")
# livro2 = Livro("Seco Seco", "Et 1155", "2027")
#
# print(livro1)
# print(livro2)

# 3 - Adicione um metodo de instancia chamado emprestar a classe Livro que define o atributo
# disponivel como False.
# Crie uma instancia da classe, chame o metodo emprestar e imprima se o livro esta disponivel ou nao.

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self._titulo = titulo
#         self._autor = autor
#         self._ano_publicacao = ano_publicacao
#         self._disponivel = True
#
#     def __str__(self):
#         return f"Titulo: {self._titulo} | Autor: {self._autor} | Ano de publicacao: {self._ano_publicacao}"
#
#     def emprestar(self):
#         self._disponivel = False
#
#     @property
#     def status_disponivel(self):
#         return "Sim" if self._disponivel else "Nao"
#
# livro1 = Livro("Sovando latas", "ET 1155", "2026")
# livro1.emprestar()
# print(livro1.status_disponivel)

# 4 - Adicione um metodo estatico chamado verificar_disponibilidade a classe Livro que recebe um ano
# como parametro e retorna uma lista dos livros disponiveis publicados nesse ano.


class Livro:
    _livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro._livros.append(self)

    def __str__(self):
        return f"Titulo: {self._titulo} | Autor: {self._autor} | Ano de publicacao: {self._ano_publicacao}"

    def emprestar(self):
        self._disponivel = False

    @property
    def status_disponivel(self):
        return "Sim" if self._disponivel else "Nao"

    @staticmethod
    def verificar_disponibilidade(ano):
        return [
            livro for livro in Livro._livros
            if livro._ano_publicacao == ano and livro._disponivel
        ]

if __name__ == "__main__":
    livro1 = Livro("Sovando latas", "ET 1155", "2026")
    livro2 = Livro("Seco Seco", "ET 1155", "2026")
    livro3 = Livro("Livro Antigo", "Autor X", "2025")

    livro1.emprestar()

    for livro in Livro.verificar_disponibilidade("2026"):
        print(livro)

# 5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.