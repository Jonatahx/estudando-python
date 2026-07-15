class Pessoa:

    def __init__(self, nome, idade, estado_civil):
        self.nome = nome
        self.idade = idade
        self.estado_civil = estado_civil

    def exibir(self):
        print(f"Seja bem-vindo(a), {self.nome}! Vimos que você tem {self.idade} anos e está {self.estado_civil}.")

    def exibir2(self):
         print(f"{self.nome} foi cadastrado(a)! A pessoa cadastrada possui {self.idade} anos e está {self.estado_civil}.")

cadastro = input("Deseja se cadastrar? y/N\n(y para SIM e N para NÃO)\n")
while cadastro not in ["y","N"]:
        cadastro = input("Erro! Digite y ou N\n")

if cadastro == "y":
     pass
else:
    print("Fim da sessão.")
    exit()

#daqui pra baixo é quem apertou "y"

nome = input("Digite o seu nome completo: ")
idade = int(input("Digite a sua idade: "))
estado = int(input("Qual seu estado-civil?\nDigite 1 para SOLTEIRO(A), 2 para CASADO(A) ou 3 para VIÚVO(A)\n"))

while estado not in [1,2,3]:
    estado = int(input("Erro! Digite 1, 2 ou 3"))

if estado == 1:
    estado_civil = "solteiro(a)"

elif estado == 2:
    estado_civil ="casado(a)"

else:
    estado_civil = "viúvo(a)"

pessoa1 = Pessoa(nome, idade, estado_civil)

pessoa1.exibir()

#cadastro de outra pessoa

cadastro2 = input("Cadastrar outra pessoa? y/N\n")
while cadastro2 not in ["y","N"]:
        cadastro2 = input("Erro! Digite y ou N\n")

if cadastro2 == "y":
     pass
else:
    print("Fim da sessão.")
    exit()

pessoas = []

while True:
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    estado = int(input("Qual seu estado-civil?\nDigite 1 para SOLTEIRO(A), 2 para CASADO(A) ou 3 para VIÚVO(A)\n"))

    while estado not in [1,2,3]:
        estado = int(input("Erro! Digite 1, 2 ou 3"))

    if estado == 1:
        estado_civil = "solteiro(a)"

    elif estado == 2:
        estado_civil ="casado(a)"

    else:
        estado_civil = "viúvo(a)"

    pessoa = Pessoa(nome, idade, estado_civil)

    pessoas.append(pessoa)

    pessoa.exibir2()

    cadastro2 = input("Cadastrar outra pessoa? y/N\n")
    while cadastro2 not in ["y","N"]:
            cadastro2 = input("Erro! Digite y ou N\n")

    if cadastro2 == "y":
         pass
    
    else:
        print("Fim da sessão.")
        exit()