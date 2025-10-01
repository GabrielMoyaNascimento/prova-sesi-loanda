from django.urls import path 
from . import views 
 
urlpatterns = [ 
    # Futuramente, aqui pode ter uma lista de todos os projetos 
    path('<int:projeto_id>/', views.detalhe_projeto, name='detalhe_projeto'), 
]