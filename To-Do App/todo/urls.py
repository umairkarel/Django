from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('addTodo/', views.addTodo, name='add'),
	path('deleteTodo/<int:item_id>/', views.deleteTodo, name='delete')
]