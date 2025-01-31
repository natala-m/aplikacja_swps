from django.shortcuts import render, redirect
from .forms import ExpensesForm, BudgetForm
from .models import Expenses, Budget
from django.db.models import Sum
from datetime import datetime,timedelta
from django.utils import timezone


def home(request):
    return render(request, 'MojeFinanse/home.html')


def expenses_list(request):
    context = {"expenses_list":Expenses.objects.all()}
    return render(request, "MojeFinanse/expenses/expenses_list.html", context)

def expenses_form(request, id=0):
   if request.method == 'GET':
        if id == 0:
             form = ExpensesForm()
        else:
            expenses = Expenses.objects.get(pk=id)
            form = ExpensesForm(instance=expenses)
        return render(request, "MojeFinanse/expenses/expenses_form.html", {'form':form})
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

#Podsumowanie miesięczne 
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

    return render(request, "MojeFinanse/summary/monthly_summary.html", context)

#Podsumowanie tygodniowe 
def weekly_summary(request):
    current_date = timezone.now().date()
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
    return render(request, "MojeFinanse/summary/weekly_summary.html", context)

#Budżet
def budget_form(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_summary')  # Przekierowanie do podsumowania budżetu
    else:
        form = BudgetForm()

    return render(request, 'MojeFinanse/budget/budget_form.html', {'form': form})

def budget_summary(request):
    current_month = datetime.today().replace(day=1)
    budget = Budget.objects.filter(month__year=current_month.year, month__month=current_month.month).first()
    total_expenses = Expenses.objects.filter(date__year=current_month.year, date__month=current_month.month).aggregate(Sum('price'))['price__sum'] or 0

    budget_left = budget.amount - total_expenses if budget else None  

    context = {
        "budget": budget.amount if budget else "Brak budżetu",
        "total_expenses": total_expenses,
        "budget_left": budget_left if budget else "Brak danych",
    }
    return render(request, "MojeFinanse/summary/budget_summary.html", context)