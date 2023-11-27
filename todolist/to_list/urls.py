from django.urls import path
from to_list.views import VerListaView, CriarTarefaView,EliminarTarefaView, EditarTarefaView
from .views import VerListaView

urlpatterns = [
    path('', VerListaView.as_view(), name="ver_lista"),
    path('criar/', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('delete/<int:pk>/', EliminarTarefaView.as_view(), name='delete_task'),
    path('editar/<int:pk>/', EditarTarefaView.as_view(), name='editar_tarefa')

]
