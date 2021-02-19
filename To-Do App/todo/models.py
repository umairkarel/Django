from django.db import models

class Todo(models.Model):
	content = models.CharField(max_length=150, unique=True)

	def __str__(self):
		return self.content
