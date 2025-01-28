from django.shortcuts import render, redirect
from .forms import ExpensesForm
from .models import Expenses
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncWeek
from datetime import datetime,timedelta


def home(request):
    return render(request, 'MojeFinanse/home.html')


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
            form = ExpensesForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
        return redirect('expenses_list')


def expenses_delete(request, id):
     expenses = Expenses.objects.get(pk=id)
     expenses.delete()
     return redirect('expenses_list')

def monthly_summary(request):
    current_month = datetime.now().month
    expenses_by_month = Expenses.objects.filter(date__month=current_month).values('date')\
                                        .annotate(total=Sum('price'))\
                                        .order_by('date')
    total_expenses_month = sum(expense['total'] for expense in expenses_by_month)
    summary_month_text = f"Całkowite wydatki w tym miesiącu wynoszą: {total_expenses_month} PLN."

    context = {
        'summary_month_text': summary_month_text,
        'month_expenses': expenses_by_month,
    }

    return render(request, "MojeFinanse/monthly_summary.html", context)


def weekly_summary(request):
    current_date = datetime.today()
    start_of_week = current_date - timedelta(days=current_date.weekday())  
    end_of_week = start_of_week + timedelta(days=6) 
    weekly_expenses = Expenses.objects.filter(date__gte=start_of_week, date__lte=end_of_week)
    total_weekly_expenses = weekly_expenses.aggregate(Sum('price'))['price__sum'] or 0
    weekly_summary_text = f"Całkowite wydatki w tym tygodniu: {total_weekly_expenses} PLN."
    context = {
        'weekly_summary_text': weekly_summary_text,
        'weekly_expenses': weekly_expenses,
        'total_weekly_expenses': total_weekly_expenses,
    }
    return render(request, "MojeFinanse/weekly_summary.html", context)
