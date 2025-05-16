class Biblioteca:
    bibliotecas = []  # Lista para armazenar todas as bibliotecas
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False  # Encapsulamento usando "_" que é o private
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da Biblioteca'.ljust(25)} | {"Status"}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo  # Alterna entre ativado e desativado

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

