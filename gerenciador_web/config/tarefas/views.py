from django.shortcuts import render
from .models import Tarefa 
from django.http import HttpResponse 

 
# Nossa primeira view! 
def listar_tarefas(request): 
    # Usamos o Model 'Tarefa' para buscar todos os objetos no banco 
    tarefas_salvas = Tarefa.objects.all() 
    
    # O print abaixo é para vermos no terminal que a busca funcionou 
    print(tarefas_salvas)

    # Por enquanto, não vamos renderizar um template, 
    # apenas retornaremos uma resposta simples
    return HttpResponse("View 'listar_tarefas' foi executada! Verifique o terminal para ver os dados.") 
 
    
