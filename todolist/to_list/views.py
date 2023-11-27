from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from to_list.models import ToDoItem
from to_list.forms import CriarTarefaForm
from django.urls import reverse_lazy

# Create your views here.

class VerListaView(ListView):
    model = ToDoItem
    template_name = 'listar_tarefas.html'
    context_object_name = 'ver_lista'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = ToDoItem.objects.all() 
        return context
    

class CriarTarefaView(CreateView):
    model = ToDoItem
    form_class = CriarTarefaForm
    template_name = 'criar_tarefa.html'
    success_url = reverse_lazy('ver_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarefa'] = ToDoItem.objects.all() 
        return context
    
    
class EliminarTarefaView(DeleteView):
    model = ToDoItem
    template_name = 'delete_task.html'
    success_url = reverse_lazy('Ver_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarefa'] = self.object
        return context


class EditarTarefaView(UpdateView):
    model = ToDoItem
    template_name = 'editar_tarefa.html'
    form_class = CriarTarefaForm
    success_url = reverse_lazy('ver_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object
        return context
    