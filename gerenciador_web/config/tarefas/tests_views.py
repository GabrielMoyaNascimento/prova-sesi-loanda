# tarefas/tests.py ou tarefas/test_views.py
from django.test import TestCase
from django.urls import reverse
from .models import Tarefa
from projetos.models import Projeto

class TarefaEProjetoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.projeto1 = Projeto.objects.create(nome='Website Cliente X')
        cls.tarefa1 = Tarefa.objects.create(titulo='Criar layout', projeto=cls.projeto1)
        cls.tarefa2 = Tarefa.objects.create(titulo='Desenvolver backend', projeto=cls.projeto1)
        cls.projeto2 = Projeto.objects.create(nome='App Interno')
        cls.tarefa3 = Tarefa.objects.create(titulo='Configurar banco de dados', projeto=cls.projeto2)

    def test_adicionar_tarefa_com_sucesso(self):
        url = reverse('adicionar_tarefa')
        dados = {'titulo': 'Nova Tarefa', 'projeto': self.projeto1.id}
        self.client.post(url, data=dados)
        self.assertTrue(Tarefa.objects.filter(titulo='Nova Tarefa').exists())

    def test_detalhe_projeto_view_mostra_apenas_tarefas_corretas(self):
        url = reverse('detalhe_projeto', args=[self.projeto1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Criar layout')
        self.assertNotContains(response, 'Configurar banco de dados')