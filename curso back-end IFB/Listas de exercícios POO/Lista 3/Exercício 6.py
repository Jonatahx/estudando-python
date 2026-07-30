'''6. Conta de energia elétrica
Crie uma classe chamada ContaEnergia com os atributos nome_cliente,
consumo_kwh e valor_kwh.
Implemente um método para calcular o valor da conta e outro para exibir os dados do
cliente e o total a pagar.
Não permita que o consumo seja negativo.
Conceitos trabalhados: validação simples e métodos.
'''

class ContaEnergia:
    def __init__(self, nome_cliente, consumo_kwh, valor_kwh):
        self.nome_cliente = nome_cliente
        self.consumo_kwh = consumo_kwh
        self.valor_kwh = valor_kwh

    def calcular_valor(self):
        return self.consumo_kwh * self.valor_kwh

    def exibir_dados(self):
        print(f"Senhor(a) {self.nome_cliente}:")
        print(f"Consumo mensal: {self.consumo_kwh}")
        print(f"Valor fixo: {self.valor_kwh}")
        print(f"Valor total a ser pago: R$ {self.calcular_valor():,.2f}")

nome = input("Digite o seu nome: ")
consumo = float(input(f"Seja bem vindo(a), {nome}! Digite o seu consumo: "))
while consumo <0:
    consumo = float(input("Número inválido! Digite um número positivo: "))

valor = float(input("Digite o valor: "))

cliente1 = ContaEnergia(nome, consumo, valor)
cliente1.exibir_dados()