from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Expense
from .serializers import ExpenseSerializer


@api_view(['GET'])
def expense_list(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def expense_add(request):
    serializer = ExpenseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def expense_delete(request, pk):
    expense = Expense.objects.get(id=pk)
    expense.delete()

    return Response("Expense Deleted Successfully!")