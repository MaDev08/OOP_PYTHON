
#É uma boa convenção o nome de uma classe sempre começar com uma letra maiúscula.
class Pessoa(): 
    total_pessoas = 0 #variável de classe
    def __init__(self, nome, idade): #A função __init__ serve para iniciar toda classe que for criada.
        self.nome = nome #o self serve para especificar que o "nome" se refere a esta classe e o self é tipo um $this no PHP
        self.idade = idade 

    def nome_vendedor(self): #Isto é um metódo.
        print(f"Meu nome é {self.nome}")

    def mostrar_resultado(self): # isto aqui é um metódo de instância, que utilizei para não ficar fazendo milhares de print
        return print(f"O nome da pessoa é {self.nome} e ela tem {self.idade}")



#Herança em Python:
class Mateus(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def __str__(self):
        return f"Nome: {self.nome} idade: {self.idade}"

mateus = Mateus("Mateus", 45)
print(mateus)