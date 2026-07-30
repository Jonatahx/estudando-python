'''7. Agenda de contatos
Crie uma classe chamada Contato com os atributos nome, telefone e email.
Crie também uma classe chamada Agenda, responsável por armazenar uma lista de
contatos.
A agenda deve permitir:
1. adicionar contato;
2. listar contatos;
3. buscar contato pelo nome;
4. sair.
Conceitos trabalhados: objetos armazenados em listas e associação entre classes.
'''

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self):
        self.contatos = []

    def menu(self):
        while True:
            servico = int(input("Solicite o serviço: \n"
                "1. adicionar contato;\n"
                "2. listar contatos;\n"
                "3. buscar contato;\n"
                "4. sair.\n"))

#            if servico == 1:
#                nome = input("Digite o nome: ")
#                telefone = input("Digite o telefone: ")
#                email = input("Digite o email: ")
#                novo = Contato(nome, telefone, email)
#                self.contatos.append(novo)
#
#            elif servico == 2:
#                for i in 
#
#            elif servico == 3:
#
#            elif servico == 4:
#                print("Encerrando Agenda...")
#                break
#
#           else:
#               ("Opção inválida! Digite novamente: ")


cliente1 = Agenda()
cliente1.menu()