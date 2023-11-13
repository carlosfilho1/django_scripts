from django import forms
from to_list.models import ToDoItem

class CriarTarefaForm(forms.ModelForm):
    class Meta:
        model = ToDoItem

        fields = ['title', 'description']

        labels = {
            'title': 'Titulo da Tarefa',
            'description': 'Descrição da Tarefa',
        }

        widgets = {
            'title:': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo da Tarefa'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo da Tarefa'}),
        }