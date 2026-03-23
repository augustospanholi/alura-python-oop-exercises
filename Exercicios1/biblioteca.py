# 5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from Exercicios1.Classes.exercicios1 import Livro

# 6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar
#  e imprima se o livro está disponível ou não após o empréstimo.

livro1 = Livro("Sovando latas", "ET 1155", "2026")
livro1.emprestar()

# 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade
#  para obter a lista de livros disponíveis publicados em um ano específico.
for livro in Livro.verificar_disponibilidade("2026"):
    print(livro)

