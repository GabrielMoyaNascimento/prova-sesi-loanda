
# Lista inicial de tarefas
minhas_tarefas = ["Estudar Python", "Fazer exercícios", "Comprar pão", "Revisar matéria"]
print(f"Tarefas pendentes: {minhas_tarefas}")

# Adicionando uma nova tarefa ao final da lista
minhas_tarefas.append("Lavar a louça")
print(f"Tarefa adicionada: {minhas_tarefas}")

# Adicionando uma tarefa em uma posição específica (índice 1)
minhas_tarefas.insert(1, "Responder e-mails")
print(f"Tarefa inserida em posição específica: {minhas_tarefas}")

# Removendo uma tarefa que já foi feita (pelo nome)
minhas_tarefas.remove("Comprar pão")
print(f"Tarefa 'Comprar pão' removida: {minhas_tarefas}")

# Removendo a última tarefa
tarefa_removida = minhas_tarefas.pop() # Remove "Revisar matéria"
print(f"Última tarefa removida ('{tarefa_removida}'): {minhas_tarefas}")

# Removendo uma tarefa por índice (se você souber a posição)
# Cuidado para não tentar remover um índice que não existe!
tarefa_no_indice_0 = minhas_tarefas.pop(0) # Remove "Estudar Python"
print(f"Tarefa no índice 0 removida ('{tarefa_no_indice_0}'): {minhas_tarefas}")

##########################################################################################

# nomes = ["Ana", "Carlos", "Maria"]

# for nome in nomes:
#     print(f"Olá, {nome}!")

# ##########################################################################################

# numeros = [1, 2, 3, 4, 5]
# soma = sum(numeros)
# print("Soma:", soma)

# ##########################################################################################


# produtos_em_estoque = ["teclado", "mouse", "monitor", "teclado", "webcam", "teclado"]
# print(f"Produtos no estoque: {produtos_em_estoque}")

# # Verificar se um item está na lista (resposta True ou False)
# tem_mouse = "mouse" in produtos_em_estoque
# print(f"Tem mouse em estoque? {tem_mouse}")

# tem_headset = "headset" in produtos_em_estoque
# print(f"Tem headset em estoque? {tem_headset}")

# # Contar quantas vezes um item aparece na lista
# quantidade_teclados = produtos_em_estoque.count("teclado")
# print(f"Quantidade de teclados em estoque: {quantidade_teclados}")

# # Encontrar o índice da primeira ocorrência de um item
# indice_monitor = produtos_em_estoque.index("monitor")
# print(f"Monitor está no índice: {indice_monitor}")