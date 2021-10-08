from django.db import models

EXPENSE_CHOICES = [
     ("Expense","Expense"),
     ("Income","Income")
]

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=200, default='')
    quantity = models.BigIntegerField()
    add_money = models.CharField(max_length=10, choices=EXPENSE_CHOICES)
    Date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"