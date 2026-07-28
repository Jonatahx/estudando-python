'''2. Cálculo da área de um retângulo
Crie uma classe chamada Retangulo com os atributos base e altura. Implemente os
métodos:
● calcular_area()
● calcular_perimetro()
● exibir_dados()
O programa deve solicitar os valores ao usuário e mostrar a área e o perímetro calculados.
Conceitos trabalhados: atributos, métodos e retorno de valores.
'''

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura =  altura

    def calcular_area(self):
#Para calcular a área de um retângulo, basta multiplicar a medida da base pela medida da altura
        return self.base * self.altura

    def calcular_perimetro(self):
#O perímetro de qualquer figura geométrica é a soma do comprimento de todos os seus lados
        return 2 * (self.base + self.altura)

    def exibir_dados(self):
        print(f"A área do seu retângulo é: {self.calcular_area():.0f}")
        print(f"O perímetro do seu retângulo é: {self.calcular_perimetro():.0f}")

entrada_base = float(input("Digite a base do seu retângulo: "))
entrada_altura = float(input("Digite a altura do seu retângulo: "))

retangulo1 = Retangulo(entrada_base, entrada_altura)
retangulo1.exibir_dados()

