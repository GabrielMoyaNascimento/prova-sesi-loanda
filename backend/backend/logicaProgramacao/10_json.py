import json

def cadastrar_aluno_em_json():
    """
    Coleta dados de um aluno e os salva em um arquivo JSON.
    """
    print("--- Cadastro de Aluno ---")
    
    # 1. Coletando os dados do usuário.
    # Usamos variáveis para armazenar cada pedaço de informação.
    nome_aluno = input("Digite o nome do aluno: ")
    try:
        idade_aluno = int(input("Digite a idade do aluno: "))
    except ValueError:
        idade_aluno = 0  # Valor padrão em caso de erro na entrada
    curso_aluno = input("Digite o curso do aluno: ")

    # Pede as notas e as armazena em uma lista.
    notas_aluno = []
    print("Digite as notas do aluno (digite 'fim' para parar):")
    while True:
        nota_str = input("Nota: ")
        if nota_str.lower() == 'fim':
            break
        try:
            nota = float(nota_str)
            notas_aluno.append(nota)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # 2. Montando o dicionário Python.
    # A estrutura do dicionário se alinha perfeitamente com o formato JSON.
    dados_aluno = {
        "nome": nome_aluno,
        "idade": idade_aluno,
        "curso": curso_aluno,
        "notas": notas_aluno
    }

    # 3. Serialização e gravação em arquivo JSON.
    # O 'with open' garante que o arquivo será fechado corretamente, mesmo se houver um erro.
    with open('aluno.json', 'w', encoding='utf-8') as arquivo_json:
        # json.dump() converte o dicionário Python para uma string JSON e a escreve no arquivo.
        # 'indent=4' formata o JSON com recuo para fácil leitura.
        # 'ensure_ascii=False' permite salvar caracteres especiais (como acentos).
        json.dump(dados_aluno, arquivo_json, indent=4, ensure_ascii=False)
    
    print("\nDados do aluno salvos com sucesso em 'aluno.json'!")

# Executa a função para iniciar o programa
cadastrar_aluno_em_json()

import json

def ler_dados_aluno():
    """
    Lê o arquivo 'aluno.json', exibe os dados e calcula a média das notas.
    """
    try:
        # 1. Tentativa de leitura do arquivo JSON.
        # O 'try' é usado aqui para capturar o erro caso o arquivo não exista.
        with open('aluno.json', 'r', encoding='utf-8') as arquivo_json:
            # json.load() lê o conteúdo do arquivo e o transforma em um dicionário Python.
            dados_aluno = json.load(arquivo_json)

        print("\n--- Dados do Aluno ---")
        
        # 2. Processamento dos dados.
        # Acessamos os dados do dicionário 'dados_aluno' usando suas chaves.
        nome = dados_aluno['nome']
        idade = dados_aluno['idade']
        curso = dados_aluno['curso']
        notas = dados_aluno['notas']

        # Calculamos a média.
        # Verificamos se a lista de notas não está vazia para evitar um 'ZeroDivisionError'.
        if notas:
            media = sum(notas) / len(notas)
        else:
            media = 0

        # 3. Impressão das informações.
        # Usamos f-strings para formatar a saída de forma clara.
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Curso: {curso}")
        print(f"Notas: {notas}")
        print(f"Média das notas: {media:.2f}")

    except FileNotFoundError:
        # Este bloco 'except' é executado se o arquivo 'aluno.json' não for encontrado.
        print("Erro: O arquivo 'aluno.json' não foi encontrado.")
        print("Certifique-se de que o arquivo existe ou execute o Exercício 1 primeiro.")

# Executa a função para ler e exibir os dados
ler_dados_aluno()


import json
import os # Módulo para interagir com o sistema operacional

def gerenciar_contatos():
    """
    Permite adicionar, listar e salvar contatos em um arquivo JSON.
    """
    nome_arquivo = 'contatos.json'
    contatos = [] # A lista que armazenará todos os contatos

    # 1. Leitura inicial do arquivo de contatos (se ele existir).
    try:
        # Tenta abrir o arquivo no modo de leitura ('r').
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            # Se o arquivo existe, carrega o conteúdo para a lista 'contatos'.
            contatos = json.load(arquivo_json)
            print(f"Contatos carregados com sucesso de '{nome_arquivo}'.")
    except FileNotFoundError:
        # Se o arquivo não existe, a lista de contatos permanece vazia.
        print(f"O arquivo '{nome_arquivo}' não foi encontrado. Iniciando com a lista vazia.")

    # 2. Laço de repetição principal para o menu.
    while True:
        print("\n--- Menu de Contatos ---")
        print("1. Adicionar novo contato")
        print("2. Listar todos os contatos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        # 3. Usando 'match case' para processar a escolha do usuário.
        match opcao:
            case "1":
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                email = input("E-mail: ")
                
                # Cria um novo dicionário para o contato.
                novo_contato = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email
                }
                # Adiciona o novo dicionário à lista de contatos.
                contatos.append(novo_contato)
                print("Contato adicionado com sucesso!")
            
            case "2":
                if contatos:
                    print("\n--- Lista de Contatos ---")
                    # Itera sobre a lista de dicionários para exibir cada contato.
                    for i, contato in enumerate(contatos, 1):
                        print(f"Contato {i}:")
                        print(f"  Nome: {contato['nome']}")
                        print(f"  Telefone: {contato['telefone']}")
                        print(f"  E-mail: {contato['email']}")
                        print("-" * 20)
                else:
                    print("Nenhum contato cadastrado.")

            case "3":
                # 4. Gravação dos contatos no arquivo antes de sair.
                with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
                    # Salva a lista de dicionários atualizada.
                    json.dump(contatos, arquivo_json, indent=4, ensure_ascii=False)
                print("\nContatos salvos e programa encerrado.")
                break # Sai do laço de repetição.
            
            case _:
                print("Opção inválida. Por favor, tente novamente.")

gerenciar_contatos()