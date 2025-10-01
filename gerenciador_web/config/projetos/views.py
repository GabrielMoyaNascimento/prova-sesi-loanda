from django.shortcuts import render, get_object_or_404 
from .models import Projeto 
 
def detalhe_projeto(request, projeto_id): 
    projeto = get_object_or_404(Projeto, pk=projeto_id) 
    # Graças ao ForeignKey, o Django nos dá acesso às tarefas relacionadas 
    # O padrão é `nomedomodel_set`, mas podemos definir um `related_name` no ForeignKey 
    tarefas_do_projeto = projeto.tarefa_set.all() 
 
    contexto = { 
        'projeto': projeto, 
        'tarefas': tarefas_do_projeto 
    } 
    return render(request, 'projetos/detalhe_projeto.html', contexto)