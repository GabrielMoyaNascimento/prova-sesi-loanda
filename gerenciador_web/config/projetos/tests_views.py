from django.test import TestCase
from django.urls import reverse

from projetos.models import Projeto
from tarefas.models import Tarefa


class CasosDeBordaViewsTest(TestCase): 
    def setUp(self): 
        self.projeto = Projeto.objects.create(nome='Projeto para Exclusão') 
        self.tarefa_para_excluir = Tarefa.objects.create(titulo='Excluir esta', projeto=self.projeto) 
 
    def test_excluir_tarefa_remove_objeto_do_banco(self): 
        url = reverse('excluir_tarefa', args=[self.tarefa_para_excluir.id]) 
        tarefas_antes = Tarefa.objects.count() 
 
        response = self.client.post(url) 
 
        self.assertEqual(Tarefa.objects.count(), tarefas_antes - 1) 
        self.assertRedirects(response, reverse('lista_tarefas')) 
        with self.assertRaises(Tarefa.DoesNotExist): 
            Tarefa.objects.get(pk=self.tarefa_para_excluir.id) 
 
    def test_tentar_criar_tarefa_sem_titulo_nao_cria_objeto(self): 
        url = reverse('adicionar_tarefa') 
        dados_invalidos = { 
            'titulo': '', # Título vazio 
            'descricao': 'Tentativa com erro.', 
            'projeto': self.projeto.id 
        } 
        tarefas_antes = Tarefa.objects.count() 
 
        response = self.client.post(url, data=dados_invalidos) 
 
        self.assertEqual(Tarefa.objects.count(), tarefas_antes) 
        self.assertEqual(response.status_code, 400)  

 