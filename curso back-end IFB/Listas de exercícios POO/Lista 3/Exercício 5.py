'''5. Aluno e situação acadêmica
Crie uma classe chamada Aluno com os atributos nome, nota1 e nota2.
Implemente métodos para:
● calcular a média;
● verificar a situação do aluno;
● exibir o resultado.
Considere:
● média maior ou igual a 6: aprovado;
● média maior ou igual a 4 e menor que 6: recuperação;
● média menor que 4: reprovado.
Conceitos trabalhados: métodos, decisões e encapsulamento de regras.
'''
class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def verificar_situacao(self):
        if self.calcular_media() >= 6:
            return "Aluno aprovado!"
        elif self.calcular_media() >= 4:
            return "Alundo de recuperação..."
        else:
            return "Aluno reprovado."

    def exibir_resultado(self):
        print(f"Aluno: {self.nome}")
        print(f"Primeira nota: {self.nota1}")
        print(f"Segunda nota: {self.nota2}")
        print(f"Média: {self.calcular_media()}")
        print(f"Situação: {self.verificar_situacao()}")


nome_aluno = input("Digite o nome do aluno: ")
nota1_aluno = float(input("Digite a primeira nota do aluno: "))
nota2_aluno = float(input("Digite a segunda nota do aluno: "))

aluno1 = Aluno(nome_aluno, nota1_aluno, nota2_aluno)

aluno1.exibir_resultado()