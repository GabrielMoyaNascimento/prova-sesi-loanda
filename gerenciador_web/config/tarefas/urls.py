from django.urls import path 
from . import views # Importa as views do nosso app 
 
urlpatterns = [ 
    # Quando a URL for vazia (ex: /tarefas/), chame a view 'listar_tarefas' 
    path('', views.listar_tarefas, name='lista_tarefas'), 
] 
