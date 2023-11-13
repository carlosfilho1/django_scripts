from django.shortcuts import render
from django.views.generic import ListView, CreateView
from to_list.models import ToDoItem
from to_list.forms import CriarTarefaForm
from django.urls import reverse_lazy

# Create your views here.

class VerListaView():
    model = ToDoItem
    template_name = 'listar_tarefas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listar_tarefa'] = ToDoItem.objects.all() 
        return context
    

class CriarTarefaView(CreateView):
    model = ToDoItem
    form_class = CriarTarefaForm
    template_name = 'criar_tarefa.html'
    sucess_url = reverse_lazy('ver_lista')