def gerar_lista_compras():
    print("Vamos criar sua lista de compras! Digite os itens, um por um.")
    print("Quando terminar, digite 'fim'.")
    
    # Abertura do arquivo no modo de escrita ('w'). 
    # O 'with' garante que o arquivo será fechado automaticamente.
    with open('lista_compras.txt', 'w') as arquivo:

        while True:
            item = input("Item: ").strip()
            
            if item.lower() == 'fim':
                break
            
            arquivo.write(item + '\n')
            
    print("\nLista de compras salva com sucesso no arquivo 'lista_compras.txt'!")

# gerar_lista_compras()


def ler_tarefas_do_dia():

    print("Lendo tarefas do arquivo 'tarefas.txt'...")

    # Abertura do arquivo no modo de leitura ('r')
    # O 'with' garante que o arquivo será fechado automaticamente.
    with open('lista_compras.txt', 'r') as arquivo:
        print("\n--- Suas Tarefas ---")
        
        for i, linha in enumerate(arquivo, 1):
            tarefa = linha.strip()
            print(f"{i}. {tarefa}")
    
# ler_tarefas_do_dia()



def exercicio_lista_convidados():
    """
    Executa o exercício da lista de convidados VIP.
    1. Pede para o usuário criar uma lista de convidados e salva em 'convidados.txt'.
    2. Pede um nome para verificar se ele está na lista.
    """
    print("\n--- Exercício 1: Lista de Convidados VIP ---\n")
    
    print(">> Cadastro de Convidados <<")
    print("Digite os nomes dos convidados. Para finalizar, digite 'fim'.")

    with open('convidados.txt', 'w', encoding='utf-8') as arquivo:
        while True:
            nome = input("Nome do convidado: ")
            if nome.lower() == 'fim':
                break
            arquivo.write(nome + '\n')
            
    print("\nLista de convidados salva com sucesso!\n")

    print(">> Verificação na Entrada da Festa <<")

    with open('convidados.txt', 'r', encoding='utf-8') as arquivo:
        # Lê todas as linhas e remove os espaços/quebras de linha extras de cada nome
        lista_convidados = [nome.strip() for nome in arquivo.readlines()]

    nome_para_verificar = input("Por favor, digite seu nome para verificação: ")

    if nome_para_verificar in lista_convidados:
        print("\nSeja bem-vindo(a)!")
    else:
        print("\nDesculpe, seu nome não está na lista.")

# exercicio_lista_convidados()

def exercicio_jogo_adivinhacao():
    """
    Executa o exercício do jogo de adivinhação.
    1. Pede para um "mestre" inserir palavras secretas em 'palavras_secretas.txt'.
    2. Inicia um jogo onde o jogador tenta adivinhar uma das palavras.
    """
    print("\n--- Exercício 2: Jogo de Adivinhação de Palavras ---\n")

    print(">> Preparação do Jogo <<")
    print("Mestre do jogo, por favor, insira 5 palavras secretas.")

    with open('palavras_secretas.txt', 'w', encoding='utf-8') as arquivo:
        for i in range(5):
            palavra = input(f"Digite a {i+1}ª palavra: ")
            arquivo.write(palavra.lower() + '\n')
    
    print("\nPalavras secretas salvas! O jogo vai começar.\n")

    print(">> Jogo de Adivinhação <<")
    print("Tente adivinhar uma das 5 palavras secretas. Digite 'sair' para desistir.")

    with open('palavras_secretas.txt', 'r', encoding='utf-8') as arquivo:
        palavras_secretas = [linha.strip() for linha in arquivo.readlines()]

    while True:
        palpite = input("\nQual o seu palpite? ")

        if palpite.lower() == 'sair':
            print("Obrigado por jogar!")
            break
        
        if palpite.lower() in palavras_secretas:
            print("=> Parabéns, você acertou uma das palavras secretas!")
        else:
            print("=> Que pena, essa palavra não está na lista. Tente novamente!")
            
# exercicio_jogo_adivinhacao()