from django.urls import path
from to_list.views import VerListaView, CriarTarefaView,EliminarTarefaView, EditarTarefaView

urlpatterns = [
    path("", VerListaView.as_view(), name="ver_lista"),
    path('criar/', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('eliminar/<int:pk>/', EliminarTarefaView.as_view(), name='eliminar_tarefa'),
    path('editar/<int:pk>/', EditarTarefaView.as_view(), name='editar_tarefa')

]
