'''Crie um programa em Python utilizando herança para
representar um sistema simples de funcionários. Implemente
uma classe base chamada Funcionario, com os atributos nome
(String) e salarioBase (double), além de um método
calcularSalario() que retorna o salário base e um método
exibirDados() que imprime o nome e o salário. Em seguida, crie
uma subclasse chamada FuncionarioComissionado, que herda
de Funcionario e possui o atributo adicional comissao (double).
Essa subclasse deve sobrescrever o método calcularSalario()
para retornar a soma do salário base com a comissão, e
também sobrescrever exibirDados() para incluir a comissão nas
informações exibidas. Por fim, instancie um objeto de cada
classe e utilize os métodos definidos para mostrar os dados
dos funcionários.
s'''

class Funcionario:
    def __init__(self, nome, salarioBase):
        self.nome = nome
        self.salario = salarioBase

    def calcularSalario(self):      
        return self.salario
    
    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario}")

class FuncionarioComissionado(Funcionario):
        def __init__(self, nome, salarioBase, comissao):
             super().__init__(nome, salarioBase)
             self.comissao = comissao
        
        def calcularSalario(self):
            return self.salario + self.comissao
        
        def exibirDados(self):
             print(f"Nome do funcionário: {self.nome}")
             print(f"Salário base: R${self.salario}")
             print(f"Comissão: R${self.comissao}")
             print(f"Salario com comissão: {self.calcularSalario()}")


func1 = FuncionarioComissionado("Jônatas", 5000, 1500)
func1.exibirDados()

func2 = Funcionario("Mateus", 5000)
func2.exibirDados()