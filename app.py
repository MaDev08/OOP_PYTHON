from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

# Criando instâncias
biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

livro1 = Livro('1984', 'George Doyle', 45.0, '085-9876')
revista1 = Revista('National Geographic', 'John Cuising', 67.0, 'Quinta')
livro2 = Livro('Sapiens', 'Sigmund Lenhardt', 67.90, '123-9845')
revista2 = Revista('Uol web', 'Alexandre Moreira', 15.99, 'Primeira')

biblioteca_cidade.adiconar_item(livro1)
biblioteca_cidade.adiconar_item(revista1)
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
    print(vars(livro2))
    print(vars(revista2))
    biblioteca_cidade.exibir_itens()

if __name__ == "__main__":
    main()