from django.db import models

class Question(models.Model):
	question_text = models.TextField()
	option_one = models.CharField(max_length=25)
	option_two= models.CharField(max_length=25)
	option_three = models.CharField(max_length=25)
	option_one_count = models.IntegerField(default=0)
	option_two_count = models.IntegerField(default=0)
	option_three_count = models.IntegerField(default=0)

	def __str__(self):
		return self.question_text

	def total(self):
		return self.option_one_count + self.option_two_count + self.option_three_count
