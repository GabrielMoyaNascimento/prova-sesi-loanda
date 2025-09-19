from django.shortcuts import render
from .models import Tarefa 


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
