def gerar_lista_compras_segura():
    """
    Solicita itens de uma lista de compras e os salva em um arquivo de texto,
    com tratamento de erro para a operação de escrita.
    """
    print("--- Gerador de Lista de Compras Segura ---")
    
    nome_arquivo = 'lista_compras.txt'

    # O bloco 'try' tenta abrir e escrever no arquivo.
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            print("Digite os itens da sua lista. Digite 'fim' para sair.")
            
            while True:
                item = input("Item: ").strip()
                
                if item.lower() == 'fim':
                    break
                
                # A escrita do item no arquivo.
                arquivo.write(item + '\n')
            
        print(f"\nLista de compras salva com sucesso em '{nome_arquivo}'!")
        
    # O 'except' captura possíveis erros de entrada/saída.
    # Por exemplo, se o diretório não existir ou se não houver permissão de escrita.
    except IOError as e:
        print(f"\nErro de gravação: Não foi possível salvar o arquivo '{nome_arquivo}'.")
        print(f"Detalhes do erro: {e}")
    
# Executa a função
gerar_lista_compras_segura()



def ler_tarefas_do_dia_seguro():
    """
    Lê uma lista de tarefas de um arquivo de texto, com tratamento de erro
    para o caso de o arquivo não existir.
    """
    print("--- Leitor de Tarefas do Dia ---")
    nome_arquivo = 'tarefas.txt'

    # O bloco 'try' tenta abrir e ler o arquivo.
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print("\n--- Suas Tarefas ---")
            
            # Laço para iterar sobre cada linha do arquivo.
            for i, linha in enumerate(arquivo, 1):
                tarefa = linha.strip()  # Remove espaços e quebras de linha
                print(f"{i}. {tarefa}")
        
    # O 'except' captura a exceção específica que ocorre quando um arquivo não é encontrado.
    except FileNotFoundError:
        print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Certifique-se de que o arquivo existe no mesmo diretório do script.")
    
# Executa a função
ler_tarefas_do_dia_seguro()

def contar_palavras_em_arquivo_seguro():
    """
    Lê um arquivo de texto e conta o número de palavras, com tratamento de erro.
    """
    print("--- Contador de Palavras em Arquivo ---")
    nome_arquivo = 'texto.txt'

    # O bloco 'try' tenta realizar todas as operações de arquivo.
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê todo o conteúdo do arquivo.
            conteudo = arquivo.read()
            
            # Divide a string em uma lista de palavras.
            palavras = conteudo.split()
            
            # Obtém o número total de palavras.
            numero_de_palavras = len(palavras)
            
            print(f"\nO arquivo '{nome_arquivo}' contém {numero_de_palavras} palavras.")
            
    # Captura a exceção específica se o arquivo não existir.
    except FileNotFoundError:
        print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Certifique-se de que o arquivo existe no mesmo diretório do script.")
    
    # Captura qualquer outro erro de I/O, como permissão negada.
    except IOError:
        print(f"\nErro: Não foi possível ler o arquivo '{nome_arquivo}'.")
        print("Verifique se você tem permissão de leitura.")
        
# Executa a função
# contar_palavras_em_arquivo_seguro()


def alterar_nome():
    """
    Solicita os nomes ao usuário e altera um nome no arquivo 'nomes.txt'
    sem usar a função enumerate().
    """
    try:
        # Pede ao usuário para digitar os nomes
        nome_antigo = input("Digite o nome que você quer alterar: ")
        nome_novo = input("Digite o novo nome: ")

        with open('nomes.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
    except FileNotFoundError:
        print("Erro: O arquivo 'nomes.txt' não foi encontrado.")
        print("Por favor, crie um arquivo chamado 'nomes.txt' e adicione alguns nomes.")
        return

    nome_encontrado = False
    i = 0  # Inicia o índice da lista em 0
    
    # Percorre a lista de linhas usando um laço while
    while i < len(linhas):
        linha = linhas[i]
        nome_na_linha = linha.strip()

        if nome_na_linha == nome_antigo:
            # Altera a linha na posição 'i'
            linhas[i] = nome_novo + '\n'
            nome_encontrado = True
            break
        
        i += 1  # Incrementa o índice manualmente
    
    if not nome_encontrado:
        print(f'Erro: O nome "{nome_antigo}" não foi encontrado.')
        return

    # Reescreve o arquivo com a lista de linhas modificada.
    with open('nomes.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    
    print(f'Nome "{nome_antigo}" alterado para "{nome_novo}".')

# --- Execução do Programa ---
print("--- Alterar Nome ---")
alterar_nome()