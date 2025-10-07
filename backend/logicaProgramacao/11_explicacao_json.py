# Parte 1: A Ideia por Trás do JSON (Por que precisamos dele?)
# Vamos começar com uma analogia simples.

# Pense no arquivo .txt que usamos na aula da "Lista de Convidados" como uma lista de compras:

# - Leite
# - Pão
# - Ovos



# Agora, imagine o JSON como o cardápio de um restaurante:

# [{
#   "nome_do_prato": "X-Burger Especial",
#   "preco": 25.50,
#   "ingredientes": ["Pão", "Hambúrguer", "Queijo", "Alface"],
#   "serve_duas_pessoas": false
# },

# {
#   "nome_do_prato": "X-Burger Especial",
#   "preco": 25.50,
#   "ingredientes": ["Pão", "Hambúrguer", "Queijo", "Alface"],
#   "serve_duas_pessoas": false
# },

# ]
# A diferença é clara! No cardápio, cada informação tem uma "etiqueta" (que chamamos de chave) que descreve o que ela é. É organizado, legível e cheio de detalhes. É essa organização que o JSON traz para os nossos programas.


# Parte 2: As Regras do Jogo (A Sintaxe do JSON)
# Antes de programar, precisamos conhecer a "gramática" do JSON. É bem simples:

# { } Chaves: Representam um objeto. Pense nisso como uma "ficha cadastral" de um único item (um produto, um usuário, um carro).

# [ ] Colchetes: Representam uma lista (ou array). É uma coleção de itens, que podem ser objetos, textos, números, etc.

# "chave": valor: O coração do JSON. A chave é sempre um texto entre aspas que descreve o valor.

# , Vírgula: Usada para separar os pares "chave": valor" dentro de um objeto ou os itens dentro de uma lista.

# Parte 3: O Ciclo de Vida dos Dados (O Processo Fundamental)
# Agora, vamos para a prática! Quando criamos um programa que salva informações (como um sistema de cadastro), ele sempre segue um ciclo de 3 etapas fundamentais:

# LER: Carregar os dados que já existem no arquivo .json para a memória do computador.

# MODIFICAR: Adicionar, remover ou alterar os dados enquanto o programa está rodando.

# ESCREVER: Salvar a versão atualizada dos dados de volta no arquivo .json, substituindo a versão antiga.

# Vamos implementar esse ciclo com um exemplo completo: um programa que cadastra novos produtos em um inventário da loja.

# Parte 4: A Implementação em Python (Mão na Massa!)
# Vamos criar um único script Python que executa todo o ciclo.

# Passo 4.1: LER - Carregando os Dados Existentes de Forma Segura
# Primeiro, nosso programa precisa carregar o inventário que já existe. Mas e se o arquivo loja.json ainda não existir ou estiver vazio? Nosso código precisa ser inteligente para não quebrar. Para isso, usamos o try...except.

import json

# Inicializamos nosso inventário como uma lista vazia.
# Se a leitura falhar, teremos um ponto de partida seguro.
inventario = []

try:
    # 1. Tentamos abrir o arquivo para leitura ('r').
    with open('loja.json', 'r') as arquivo:
        # 2. Se funcionar, carregamos seu conteúdo para a variável 'inventario'.
        inventario = json.load(arquivo)
    print("✔️ Inventário existente carregado com sucesso!")

except FileNotFoundError:
    # 3. Se o arquivo não existe, este bloco é executado.
    #    Informamos o usuário e continuamos com a lista vazia.
    print("⚠️ Arquivo 'loja.json' não encontrado. Um novo será criado ao final.")

except json.JSONDecodeError:
    # 4. Se o arquivo existe mas está em branco ou corrompido, evitamos o erro.
    print("⚠️ O arquivo existe, mas está vazio. Um novo inventário será iniciado.")
# Ao final deste passo, a variável inventario contém os produtos antigos ou é uma lista vazia, pronta para receber novos itens.



# Passo 4.2: MODIFICAR - Coletando Novos Dados do Usuário
# Agora, vamos interagir com o usuário para obter as informações do novo produto. É crucial validar as entradas para garantir que números sejam tratados como números.


print("\n--- Cadastro de Novo Produto ---")

# Pedimos o nome do produto.
nome = input("Digite o nome do produto: ")

# Usamos um loop 'while' para garantir que o usuário digite um número válido para o preço.
while True:
    try:
        preco = float(input("Digite o preço do produto (ex: 199.99): "))
        break # Se a conversão para float funcionar, o loop é interrompido.
    except ValueError:
        print("❌ Erro: Por favor, digite um número válido para o preço.")

# Fazemos o mesmo para a quantidade, garantindo que seja um número inteiro.
while True:
    try:
        quantidade = int(input("Digite a quantidade em estoque: "))
        break # Sai do loop se a entrada for válida.
    except ValueError:
        print("❌ Erro: Por favor, digite um número inteiro válido para a quantidade.")

# Criamos um dicionário Python para o novo produto com os dados coletados.
novo_produto = {
    "nome_produto": nome,
    "preco_unitario": preco,
    "em_estoque": quantidade > 0, # Uma expressão booleana: True se qtd > 0
    "quantidade": quantidade
}


# Passo 4.3: ESCREVER - Adicionando e Salvando o Inventário Atualizado
# Com os dados antigos na lista inventario e o novo_produto criado, só falta juntar tudo e salvar de volta no arquivo.

# 1. Adicionamos o dicionário do novo produto à nossa lista em memória.
inventario.append(novo_produto)

# 2. Abrimos o arquivo no modo de escrita ('w').
#    ATENÇÃO: O modo 'w' SOBRESCREVE completamente o arquivo antigo.
#    É por isso que precisamos ler tudo primeiro!
with open('loja.json', 'w', encoding='utf-8') as arquivo:
    # 3. Usamos json.dump() para "despejar" a lista COMPLETA E ATUALIZADA
    #    de volta no arquivo, no formato JSON.
    #    O 'indent=4' é um truque para deixar o arquivo bem formatado e legível!
    json.dump(inventario, arquivo, indent=4)

print(f"\n✅ Produto '{nome}' foi adicionado com sucesso ao inventário!")


# O ID do produto que queremos modificar e o novo valor para a quantidade
id_produto_para_modificar = 1
nova_quantidade = 45

# --- ETAPA 1: LER O ARQUIVO ---
try:
    with open('loja.json', 'r') as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado. Nada para modificar.")
    exit() # Encerra o script se o arquivo não existir

# --- ETAPA 2: MODIFICAR OS DADOS EM MEMÓRIA ---
produto_encontrado = False
# Percorremos cada dicionário ('produto') dentro da nossa lista 'inventario'
for produto in inventario:
    # Verificamos se o valor da chave 'id' corresponde ao que procuramos
    if produto['id'] == id_produto_para_modificar:
        print(f"Produto encontrado: {produto['nome_produto']}")
        print(f"Quantidade antiga: {produto['quantidade']}")
        
        # Modificamos o valor da chave 'quantidade' neste dicionário
        produto['quantidade'] = nova_quantidade
        # Também atualizamos se está em estoque, para manter a consistência
        produto['em_estoque'] = nova_quantidade > 0
        
        print(f"Nova quantidade: {produto['quantidade']}")
        
        produto_encontrado = True
        break # Otimização: se já encontramos o ID, não precisamos continuar o loop

# Se o loop terminar e não encontrarmos o produto
if not produto_encontrado:
    print(f"Produto com ID {id_produto_para_modificar} não foi encontrado.")
else:
    # --- ETAPA 3: ESCREVER OS DADOS ATUALIZADOS NO ARQUIVO ---
    with open('produtos.json', 'w') as arquivo:
        json.dump(inventario, arquivo, indent=4)
    print("O arquivo 'produtos.json' foi atualizado com sucesso!")


# O ID do produto que queremos excluir do nosso inventário
id_produto_para_excluir = 201

# --- ETAPA 1: LER O ARQUIVO ---
try:
    with open('produtos.json', 'r', encoding='utf-8') as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado. Nada para excluir.")
    exit()

# --- ETAPA 2: MODIFICAR OS DADOS (CRIANDO UMA NOVA LISTA) ---

# Criamos uma nova lista vazia que conterá apenas os produtos que queremos manter
novo_inventario = []
produto_excluido = False

# Percorremos cada produto na lista original
for produto in inventario:
    # Verificamos se o ID do produto atual é DIFERENTE do que queremos excluir
    if produto['id'] != id_produto_para_excluir:
        # Se for diferente, nós o adicionamos à nossa nova lista
        novo_inventario.append(produto)
    else:
        # Se for igual, apenas registramos que o encontramos para exclusão
        produto_excluido = True
        print(f"Produto '{produto['nome_produto']}' (ID: {id_produto_para_excluir}) será removido.")


# Se o loop terminar e o produto não tiver sido encontrado na lista
if not produto_excluido:
    print(f"Produto com ID {id_produto_para_excluir} não foi encontrado para exclusão.")
else:
    # --- ETAPA 3: ESCREVER A NOVA LISTA NO ARQUIVO ---
    with open('produtos.json', 'w', encoding='utf-8') as arquivo:
        # Salvamos a nova lista (sem o item excluído) de volta no arquivo
        json.dump(novo_inventario, arquivo, indent=4)
    print("O arquivo 'produtos.json' foi atualizado com o item removido!")


#  LISTAR - Exibindo o Inventário Atualizado de Forma Organizada
try:
    with open('loja.json', 'r', encoding='utf-8') as arquivo:
        inventario = json.load(arquivo)
    
    if not inventario:
        print("⚠️ O inventário está vazio. Adicione um produto primeiro.")
    else:
        print("🗒️ Lista de Produtos no Inventário:")
        
        # O loop 'for' continua percorrendo cada item da lista normalmente.
        for produto in inventario:
            # Imprimimos os detalhes do produto usando nossa variável de contagem.
            print(f"\n--- Produto {produto.get('id')} ---")
            print(f"  Nome: {produto.get('nome_produto', 'N/A')}")
            print(f"  Preço: R$ {produto.get('preco_unitario', 0):.2f}")
            print(f"  Quantidade: {produto.get('quantidade', 0)} unidades")
            print(f"  Disponível em Estoque: {produto.get('em_estoque')}")
except FileNotFoundError:
    print("❌ Arquivo 'loja.json' não encontrado. O inventário parece estar vazio.")

print("\n--- Fim da Listagem ---")
