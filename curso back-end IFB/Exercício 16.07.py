'''Implemente uma calculadora simples em Python
que ofereça um menu para o usuário escolher entre
as operações: (1) soma, (2) subtração,
(3) multiplicação, (4) divisão e (5) sair.
Para cada operação, o programa deve pedir dois
números ao usuário e mostrar o resultado. Use blocos
try/except para garantir que o programa não quebre
caso o usuário digite valores inválidos (ex: letras
em vez de números) ou tente dividir por zero. O programa
deve continuar funcionando normalmente após qualquer erro,
permitindo novas operações até o usuário escolher sair.
'''

print("Escolha uma operação a seguir: ")
while True:
    try:
        op = int(input(
        "(1) soma\n"
        "(2) subtração\n"
        "(3) multiplicação\n"
        "(4) divisão\n"
        "(5) sair\n"))

        while op not in (1, 2, 3, 4, 5):
            op = int(input("Erro! Digite o número das opções disponíveis: "))

        if op == 1:
            s1 = float(input("Digite o primeiro número: "))
            s2 = float(input("Digite o segundo número: "))
            s3 = s1 + s2
            print(f"Resultado: {s3}") 

        elif op == 2:
            su1 = float(input("Digite o primeiro número: "))
            su2 = float(input("Digite o segundo número: "))
            su3 = su1 - su2
            print(f"Resultado: {su3:.2f}") 

        elif op == 3:
            m1 = float(input("Digite o primeiro número: "))
            m2 = float(input("Digite o segundo número: "))
            m3 = m1 * m2
            print(f"Resultado: {m3}") 

        elif op == 4:
            d1 = float(input("Digite o primeiro número: "))
            d2 = float(input("Digite o segundo número: "))
            d3 = d1 / d2
            print(f"Resultado: {d3:.2f}")

        else:
            print("Encerrando programa...")
            break

    except ValueError:
          print("Erro! Digite apenas números.")

    except ZeroDivisionError:
        print("Erro! Não é possível dividir por zero.")