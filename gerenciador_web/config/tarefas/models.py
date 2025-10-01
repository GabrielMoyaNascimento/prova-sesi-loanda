from django.db import models
from projetos.models import Projeto # Importe o Model do outro app! 
 
class Tarefa(models.Model): 
    titulo = models.CharField(max_length=200) 
    descricao = models.TextField(blank=True, null=True) 
    data_criacao = models.DateTimeField(auto_now_add=True) 
    concluida = models.BooleanField(default=False) 
    # Cada tarefa estará ligada a um único projeto. 
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True, blank=True) 
 
    def __str__(self): 
        return self.titulo 
