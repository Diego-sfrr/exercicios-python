"""1. Peca ao usuario para inserir o ano de nascimento dele e, em seguida, calcule e exiba a idade atual
dele (considere somente o ano como base para o calculo).
"""
idade = int(input("Digite o ano de nascimento: "))
ano = int(input("Digite o ano em que deseja calcular a idade: "))

def idades(idade, ano):
    return ano - idade

print(f"Sua idade é {idades(idade, ano)}")

"""2. Crie um programa que permita ao usu´ario realizar opera¸c˜oes de adi¸c˜ao, subtra¸c˜ao, multiplica¸c˜ao e
divis˜ao com dois n´umeros. Pe¸ca ao usu´ario para escolher a opera¸c˜ao desejada e exiba o resultado.
"""

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

"""3. Pe¸ca ao usu´ario para inserir um n´umero e, em seguida, determine se o n´umero ´e par ou ´ımpar.
Exiba uma mensagem correspondente.
"""
def verificar_par_impar(numero):
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")


numb = int(input("Digite o número: "))
verificar_par_impar(numb)

"""4. Crie um programa que solicite ao usu´ario trˆes notas e calcule a m´edia. Com base na m´edia, informe
se o aluno foi aprovado, est´a de recupera¸c˜ao ou reprovado (considerando a m´edia 7 como crit´erio
de aprova¸c˜ao e a m´edia entre 5 e 6.9 como crit´erio de recupera¸c˜ao).
"""
nota = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def medias(nota, nota2, nota3):
    media = (nota + nota2 + nota3) / 3

    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Aluno aprovado")
    elif media >= 5:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")
    
    return media

print(medias(nota, nota2, nota3))


"""5. Pe¸ca ao usu´ario para inserir um n´umero e, em seguida, mostre a tabuada desse n´umero de 1 a 10.
"""
def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


number_1 = int(input("Digite o número que deseja a tabuada: "))
tabuada(number_1)

"""6. Crie um programa que permita ao usu´ario converter temperaturas de Celsius para Fahrenheit. A
f´ormula utilizada deve ser: (temp celsius * 9 / 5) + 32"""
def celsius_para_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit


temp = int(input("Digite a temperatura em Celsius: "))
resultado = celsius_para_fahrenheit(temp)

print(f"Em Fahrenheit é: {resultado}")

"""7. Crie um programa que pe¸ca ao usu´ario para inserir cinco n´umeros em uma lista. Em seguida,
calcule a soma e a m´edia desses n´umeros e exiba os resultados."""
def calcular_media():
    soma = 0
    contador = 0

    while contador < 5:
        num = int(input("Digite um número: "))
        soma += num
        contador += 1

    media = soma / 5
    return media


resultado = calcular_media()
print(f"A média é {resultado}")

"""8. Crie um programa que permita ao usu´ario calcular juros simples. Pe¸ca ao usu´ario para inserir o
valor principal, a taxa de juros anual e o per´ıodo de tempo em anos. Calcule e exiba o valor total
ap´os o per´ıodo especificado."""

def calcular_juros_simples(principal, taxa, tempo):
    juros = principal * (taxa / 100) * tempo
    montante = principal + juros
    return juros, montante


principal = float(input("Digite o valor principal: "))
taxa = float(input("Digite a taxa de juros anual (%): "))
tempo = float(input("Digite o tempo em anos: "))

juros, montante = calcular_juros_simples(principal, taxa, tempo)

print(f"Juros: {juros:.2f}")
print(f"Valor total: {montante:.2f}")

"""9. Pe¸ca ao usu´ario para inserir seu peso (em quilogramas) e sua altura (em metros). Calcule e exiba
o IMC. O IMC ´e calculado usando a f´ormula: IMC = peso / (altura * altura).
"""
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")
