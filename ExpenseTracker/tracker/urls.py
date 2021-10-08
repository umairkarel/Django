from django.urls import path
from . import views as apiView

urlpatterns = [
    # path('', apiView.overview, name="api-overview"),
    path('expense-list/', apiView.expense_list, name='expense-list'),
    path('expense-add/', apiView.expense_add, name='expense-add'),
    path('expense-delete/<int:pk>/', apiView.expense_delete, name='expense-delete'),
]