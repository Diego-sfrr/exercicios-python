def somar(a, b):
    print(f"Soma: {a + b}")

def subtrair(a, b):
    print(f"Subtração: {a - b}")

def multiplicar(a, b):
    print(f"Multiplicação: {a * b}")

def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero!")
    else:
        print(f"Divisão: {a / b}")


while True:
    try:
        valor_a = float(input("Digite o primeiro valor: "))
        valor_b = float(input("Digite o segundo valor: "))
    except ValueError:
        print("Digite apenas números válidos!")
        continue

    operadores = input(
        "\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n0 - Sair\nEscolha uma opção: "
    )

    if operadores == "1":
        somar(valor_a, valor_b)
    elif operadores == "2":
        subtrair(valor_a, valor_b)
    elif operadores == "3":
        multiplicar(valor_a, valor_b)
    elif operadores == "4":
        dividir(valor_a, valor_b)
    elif operadores == "0":
        print("Saindo da calculadora...")
        break
    else:
        print("Digite um valor válido!")
