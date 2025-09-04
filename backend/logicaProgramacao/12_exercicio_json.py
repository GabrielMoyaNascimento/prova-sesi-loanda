import json

# Constante com o nome do arquivo para evitar repetição de texto
NOME_ARQUIVO = 'biblioteca.json'

def carregar_dados():
    """
    Esta função é responsável por ler os dados do arquivo JSON.
    - Se o arquivo existir, mas estiver vazio ou corrompido,  retorna uma lista vazia.
    """

    try:
        # Abre o arquivo no modo de leitura ('r')
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            # json.load() converte o conteúdo JSON do arquivo para um objeto Python
            return json.load(arquivo)
    except json.JSONDecodeError:
        # Se o arquivo estiver em branco, json.load() dará um erro.
        # Neste caso, retornamos uma lista vazia para começar do zero.
        return []

def salvar_dados(dados):
    """
    Esta função recebe uma lista de dados e a salva no arquivo JSON.
    Ela sobrescreve o arquivo com o novo conteúdo.
    """
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        # json.dump() converte o objeto Python para o formato JSON e escreve no arquivo.
        # indent=4 formata o arquivo para ser facilmente legível por humanos.
        json.dump(dados, arquivo, indent=4)

def cadastrar_livro():
    """
    Função principal para o cadastro de um novo livro.
    Ela pede as 10 informações, monta um dicionário e salva os dados.
    """
    print("\n--- Cadastro de Novo Livro ---")

    # Coleta de dados do usuário através do terminal
    novo_livro = {
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "editora": input("Editora: "),
        "ano_publicacao": int(input("Ano de Publicação: ")),
        "genero": input("Gênero: "),
        "isbn": input("ISBN: "),
        "numero_paginas": int(input("Número de Páginas: ")),
        "idioma": input("Idioma: "),
        "formato": input("Formato (Capa Dura, Brochura, etc.): "),
        "prateleira": input("Localização (Prateleira): ")
    }
    
    # 1. LER: Carrega a lista de livros já existentes.
    livros = carregar_dados()
    
    # 2. MODIFICAR: Adiciona o novo livro à lista em memória.
    livros.append(novo_livro)
    
    # 3. ESCREVER: Salva a lista atualizada de volta no arquivo.
    salvar_dados(livros)
    
    print("\n✅ Livro cadastrado com sucesso!")

def listar_livros():
    """
    Lê o arquivo JSON e exibe todos os livros cadastrados de forma organizada.
    """
    livros = carregar_dados()
    
    # Verifica se a lista está vazia
    if not livros:
        print("\nNenhum livro cadastrado ainda.")
        return

    print("\n--- Catálogo Completo da Biblioteca ---")
    # Enumera a lista para exibir um contador (Livro 1, Livro 2, ...)
    for i, livro in enumerate(livros, 1):
        print(f"\n--- Livro {i} ---")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Editora: {livro['editora']} (Ano: {livro['ano_publicacao']})")
        print(f"Gênero: {livro['genero']}")
        print(f"Páginas: {livro['numero_paginas']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Formato: {livro['formato']}")
        print(f"Idioma: {livro['idioma']}")
        print(f"Localização: {livro['prateleira']}")
    print("\n-------------------------------------")

def menu_principal():
    """
    Exibe o menu principal e gerencia a navegação do usuário.
    """
    while True:
        print("\n--- Sistema de Catalogação da Biblioteca ---")
        print("1. Cadastrar Novo Livro")
        print("2. Listar Livros Cadastrados")
        print("3. Sair")
        
        escolha = input(">> Digite o número da opção desejada: ")
        
        if escolha == '1':
            cadastrar_livro()
        elif escolha == '2':
            listar_livros()
        elif escolha == '3':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma das opções do menu.")

menu_principal()