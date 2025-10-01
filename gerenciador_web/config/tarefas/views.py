from django.shortcuts import get_object_or_404, redirect, render
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
    if request.method == 'POST': 
        # Se o método for POST, o formulário foi enviado. 
        titulo = request.POST.get('titulo') 
        descricao = request.POST.get('descricao') 
        Tarefa.objects.create(titulo=titulo, descricao=descricao) 
        # Redireciona para a lista de tarefas após salvar. 
        return redirect('lista_tarefas') 
 
    return render(request, 'tarefas/form_tarefa.html') 

def alterar_tarefa(request, tarefa_id): 
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id) 
 
    if request.method == 'POST': 
        tarefa.titulo = request.POST.get('titulo') 
        tarefa.descricao = request.POST.get('descricao') 
        tarefa.concluida = request.POST.get('concluida') == 'on' 
        tarefa.save() # Salva as alterações no objeto existente. 
        return redirect('lista_tarefas') 
 
    # No método GET, envia a tarefa para o template para preencher o formulário. 
    return render(request, 'tarefas/form_tarefa.html', {'tarefa': tarefa}) 

def excluir_tarefa(request, tarefa_id): 
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id) 
    if request.method == 'POST': 
        tarefa.delete() # Deleta o objeto do banco. 
        return redirect('lista_tarefas') 
 
    # No método GET, mostra a página de confirmação. 
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa}) 


