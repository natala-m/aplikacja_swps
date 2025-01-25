from django.shortcuts import render, redirect
from .forms import ExpensesForm
from .models import Expenses

def expenses_list(request):
    context = {"expenses_list":Expenses.objects.all()}
    return render(request, "MojeFinanse/expenses_list.html", context)

def expenses_form(request, id=0):
   if request.method == 'GET':
        if id == 0:
             form = ExpensesForm()
        else:
            expenses = Expenses.objects.get(pk=id)
            form = ExpensesForm(instance=expenses)
        return render(request, "MojeFinanse/expenses_form.html", {'form':form})
   else:
        if id == 0 :
            form = ExpensesForm(request.POST)
        else:
            expenses = Expenses.objects.get(pk=id)
            form = ExpensesForm(request.POST, isinstance=expenses)
        if form.is_valid():
            form.save()
        return redirect('/expenses/list')


def expenses_delete(request, id):
     expenses = Expenses.objects.get(pk=id)
     expenses.delete()
     return redirect('/expenses/list/')

