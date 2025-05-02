
#É uma boa convenção o nome de uma classe sempre começar com uma letra maiúscula.
class Pessoa(): 
    def __init__(self, nome, idade): #A função __init__ serve para iniciar toda classe que for criada.
        self.nome = nome #o self serve para especificar que o "nome" se refere a esta classe e o self é tipo um $this no PHP
        self.idade = idade 

    def nome_vendedor(self): #Isto é um metódo.
        print(f"Meu nome é {self.nome}")


pessoa1 = Pessoa("Michael", 45) #Realizei uma instância, onde criei o objeto pessoa1 que pega as características da classe Pessoa.

print(pessoa1.nome)
pessoa1.nome_vendedor() #Nome do objeto + metódo que vai ser chamado é a forma como eu chamo um metódo

print(f"o nome da pessoa é {pessoa1.nome}")