from modelos.biblioteca import Biblioteca


# Criando instâncias
biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

# Alternando estados
biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()