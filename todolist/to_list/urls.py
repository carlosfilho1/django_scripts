from django.urls import path

urlpatterns = [
    path("", VerListaView.as_view(), name="ver_lista"),
    path('criar/', CriarTarefaView.as_View(), name='Criar_Tarefa'),
]
