'''1. Cadastro de pessoa
Crie uma classe chamada Pessoa com os atributos nome, idade e cidade. Implemente
um método chamado apresentar() que exiba uma mensagem com todos os dados da
pessoa.
No programa principal, crie dois objetos da classe Pessoa e execute o método
apresentar().
Conceitos trabalhados: classe, objeto, atributos, construtor e método.
'''

class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentar(self):
        print(f"Nome: {self.nome}\n")
        print(f"idade: {self.idade}\n")
        print(f"Cidade:  {self.cidade}\n")

pessoa1 = Pessoa("Roberto", 49, "New Jersey")
pessoa1.apresentar()

pessoa2 = Pessoa("Frida", 29, "Los Angeles")
pessoa2.apresentar()

