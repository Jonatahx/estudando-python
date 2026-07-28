'''4. Produto com desconto
Crie uma classe chamada Produto com os atributos nome, preco e
percentual_desconto.
Implemente os métodos:
● calcular_desconto()
● calcular_preco_final()
● exibir_resumo()
O programa deve mostrar o preço original, o valor do desconto e o preço final.
'''

class Produto:
    def __init__(self, nome, preco, percentual_desconto):
        self.nome = nome
        self.preco =  preco
        self.percentual =  percentual_desconto

    def calcular_desconto(self):
        divisão = self.percentual / 100
        return self.preco * divisão

    def calcular_preco_final(self):
        return self.preco - self.calcular_desconto()

    def exibir_resumo(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Preço original: R$ {self.preco:,.2f}")
        print(f"Desconto adquirido: R$ {self.calcular_desconto():,.2f}")
        print(f"Preço final: R$ {self.calcular_preco_final():,.2f}")

nome_produto = input("Digite o nome do produto: ")
preço_produto = float(input("Digite o preço do produto: "))
desconto = int(input("Digite a porcentagem do desconto: "))

produto1 = Produto(nome_produto, preço_produto, desconto)
produto1.exibir_resumo()