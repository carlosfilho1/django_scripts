from django.urls import path
from to_list.views import VerListaView, CriarTarefaView

urlpatterns = [
    path("", VerListaView.as_view(), name="ver_lista"),
    path('criar/', CriarTarefaView.as_View(), name='criar_tarefa'),
]
