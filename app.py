from modelos.biblioteca import Biblioteca


# Criando instâncias
biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

# Alternando estados
biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()

# Mostrando as avaliações
biblioteca_cidade.receber_avaliacao('Jonas', 9.0)
biblioteca_shopping.receber_avaliacao('Andrei', 10.0)

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()