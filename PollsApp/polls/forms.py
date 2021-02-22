from django.forms import ModelForm
from .models import Question

class CreatePollForm(ModelForm):
	class Meta:
		model = Question
		fields = ['question_text', 'option_one', 'option_two', 'option_three']