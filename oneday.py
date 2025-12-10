from InquirerPy import inquirer

produtos = []

def inicializar_p():
    global produtos
    produtos = []


def encontrar_indice_produto(nome_produto):
    try:
        return produtos.index(nome_produto)
    except ValueError:
        return -1


def cadastrar_produtos(produto):
    pass


def buscar_produto():
    pass


def remove_produto():
    pass


def menu():
    global opcao_menu
    opcao_menu = inquirer.select(
        message="\nBem Vindo\n",
        choices=[
            "1 - Cadastrar produto",
            "2 - Listar produtos",
            "3 - Buscar produto",
            "4 - Remover produto",
            "5 - Sair"
        ]
    ).execute()
