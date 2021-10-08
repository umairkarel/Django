from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    day = models.DateTimeField()
    reminder = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"Task: {self.title}"
