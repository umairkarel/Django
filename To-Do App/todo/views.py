from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def index(request):
	context = {
		'posts': Todo.objects.all()
	}

	return render(request, 'todo/home.html', context)

def addTodo(request):
	new_item = Todo(content=request.POST['content'])
	new_item.save()

	return redirect('index')

def deleteTodo(request, item_id):
	item_to_delete = Todo.objects.get(id=item_id)
	item_to_delete.delete()

	return redirect('index')