from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

# Criando instâncias
biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

livro1 = Livro('1984', 'George Doyle', 45.0, '085-9876')
revista1 = Revista('National Geographic', 'John Cuising', 67.0, 'Quinta')

# Alternando estados
# biblioteca_cidade.alterna_estado()
# biblioteca_shopping.alterna_estado()

# Mostrando as avaliações
# biblioteca_cidade.receber_avaliacao('Jonas', 9.0)
# biblioteca_shopping.receber_avaliacao('Andrei', 10.0)

def main():
    #Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))

if __name__ == "__main__":
    main()