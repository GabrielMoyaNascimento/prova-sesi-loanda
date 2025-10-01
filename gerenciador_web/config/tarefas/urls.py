from django.urls import path 
from . import views # Importa as views do nosso app 

urlpatterns = [ 
    # LISTAR TAREFAS
    # Quando a URL for vazia (ex: /tarefas/), chame a view 'listar_tarefas' 
    path('', views.listar_tarefas, name='lista_tarefas'), 

    # DETALHES DA TAREFA
    # <int:tarefa_id> captura um número da URL 
    path('<int:tarefa_id>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    
    # ADICIONAR TAREFA
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),

    # ALTERAR TAREFA
    path('<int:tarefa_id>/alterar/', views.alterar_tarefa, name='alterar_tarefa'),

    # EXCLUIR TAREFA
    path('<int:tarefa_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'), 
]