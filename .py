produtos = [] 
def inicializar_p():
    global produtos
    produtos = []

def encontrar_indice_produto(nome_produto):
    try:
        return produtos.index(nome_produto)
    except ValueError:
        return -1
    
def cadastrar_produtos(produtos):
    
