class Progressão:
    def __init__(self, n, a1, r):
        self.n = n
        self.a1 = a1
        self.r = r
        self.ultimotermo = self.a1 + self.r * (self.n - 1)

    def exibirDados(self):
        print(f"Dados:\n"
            f"1. {self.n}\n"
            f"2. {self.a1}\n"
            f"3. {self.r}\n"
            )
        
    def calcularUltimoTermo(self):
        print(f"Último termo: {self.ultimotermo}")

    def calcularSoma(self):
        soma2 = self.n * (self.a1 + self.ultimotermo) / 2
        print(f"Soma dos termos: {soma2:.0f}")

    def exibirTermos(self):
        termo = self.a1
        print("Termos: ")
        for _ in range(self.n):
            print(termo)
            termo += self.r

print("CALCULE A PROGRESSÃO ARITMÉTICA")

n = int(input("1. Digite o número de termos: "))
a1 = int(input("2. Digite o primeiro termo: "))
r = int(input("3. Digite a razão: "))
print()

c1 = Progressão(n, a1, r)
c1.exibirDados()
c1.calcularUltimoTermo()
c1.calcularSoma()
c1.exibirTermos()
