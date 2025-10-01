from django.shortcuts import get_object_or_404, redirect, render
from gerenciador_web.config.projetos.models import Projeto
from .models import Tarefa 

# Métodos HTTP:
# GET:    Usado para solicitar/buscar dados de um recurso.
# POST:   Usado para criar um novo recurso. Envia dados para o servidor no corpo da requisição.
# PUT:    Usado para atualizar completamente um recurso existente.
# DELETE: Usado para remover um recurso específico.

def listar_tarefas(request): 
    # 1. A busca no banco de dados continua a mesma 
    tarefas_salvas = Tarefa.objects.all() 
 
    # 2. Criamos um "dicionário de contexto" para enviar os dados ao template. 
    # A chave 'minhas_tarefas' será a variável que usaremos no HTML. 
    contexto = { 
        'minhas_tarefas': tarefas_salvas 
    } 
 
    # 3. Renderizamos o template, passando a requisição e o contexto com os dados. 
    return render(request, 'tarefas/lista.html', contexto) 

def detalhe_tarefa(request, tarefa_id): 
    # Busca uma tarefa pelo seu ID (pk=primary key). 
    # Se não encontrar, exibe automaticamente um erro 404 (Página não encontrada). 
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)

    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})

def adicionar_tarefa(request): 
    # Busca todos os projetos para popular o seletor no formulário 
    projetos = Projeto.objects.all() 
 
    if request.method == 'POST': 
        titulo = request.POST.get('titulo') 
        descricao = request.POST.GET('descricao') 
        projeto_id = request.POST.get('projeto') # Pega o ID do projeto selecionado 
 
        # Encontra a instância do projeto e a associa à nova tarefa 
        projeto_selecionado = Projeto.objects.get(pk=projeto_id) 
        Tarefa.objects.create(titulo=titulo, descricao=descricao, projeto=projeto_selecionado) 
 
        return redirect('lista_tarefas') 
 
    # Envia a lista de projetos para o template 
    return render(request, 'tarefas/form_tarefa.html', {'projetos': projetos}) 
 
# A lógica para alterar_tarefa seria similar, passando também a lista de projetos. 

def alterar_tarefa(request, tarefa_id):
    # 1. Busca a tarefa específica que será editada ou retorna um erro 404 se não existir.
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    
    # 2. Busca todos os projetos para popular o campo de seleção no formulário.
    #    Isso é necessário tanto para GET (exibir o form) quanto para POST (caso haja um erro de validação).
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        # 3. Pega os dados enviados pelo formulário.
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto') # Pega o ID do projeto selecionado no <select>.
        concluida = request.POST.get('concluida') == 'on' # Checkbox retorna 'on' se marcado.

        # 4. Busca a instância do projeto selecionado no banco de dados.
        projeto_selecionado = get_object_or_404(Projeto, pk=projeto_id)

        # 5. Atualiza os campos do objeto 'tarefa' que já foi carregado do banco.
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.projeto = projeto_selecionado # Associa a tarefa ao novo projeto.
        tarefa.concluida = concluida
        
        # 6. Salva as alterações no banco de dados.
        tarefa.save()
        
        # 7. Redireciona o usuário para a lista de tarefas após a alteração.
        return redirect('lista_tarefas')

    # 8. Se o método for GET (primeiro acesso à página de edição):
    #    Renderiza o formulário, passando a tarefa para preencher os campos
    #    e a lista de projetos para montar o seletor.
    context = {
        'tarefa': tarefa,
        'projetos': projetos
    }
    return render(request, 'tarefas/form_tarefa.html', context)

def excluir_tarefa(request, tarefa_id): 
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id) 
    if request.method == 'POST': 
        tarefa.delete() # Deleta o objeto do banco. 
        return redirect('lista_tarefas') 
 
    # No método GET, mostra a página de confirmação. 
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa}) 


