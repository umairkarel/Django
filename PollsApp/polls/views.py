from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import CreatePollForm
from .models import Question

def home(request):
	polls = Question.objects.all()

	return render(request, 'polls/home.html', {'polls': polls})

def create(request):
	if request.method == 'POST':
		form = CreatePollForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f"Poll has been created!")
			return redirect('home')
	else:
		form = CreatePollForm()

	return render(request, 'polls/create.html', {'form':form})

def vote(request, poll_id):
	poll = Question.objects.get(pk=poll_id)

	if request.method == 'POST':
		vote = request.POST['poll']
		if vote == "option1":
			poll.option_one_count += 1
		elif vote == "option2":
			poll.option_two_count += 1
		elif vote == "option3":
			poll.option_three_count += 1
		else:
			return HttpResponse(400, 'Invalid Form')

		poll.save()
		return redirect('results', poll_id)
	
	return render(request, 'polls/vote.html', {'poll':poll})

def results(request, poll_id):
	poll = Question.objects.get(pk=poll_id)
	
	return render(request, 'polls/results.html', {'poll':poll})