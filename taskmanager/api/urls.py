from django.urls import path
from . import views as apiView

urlpatterns = [
    path('', apiView.overview, name="api-overview"),
    path('task-list/', apiView.task_list, name='task-list'),
    path('task-create/', apiView.create_task, name='task-create'),
    path('task-delete/<int:pk>/', apiView.task_delete, name='task-delete'),
]