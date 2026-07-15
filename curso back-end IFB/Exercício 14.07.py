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