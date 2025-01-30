from django import forms
from .models import Expenses, Budget

class ExpensesForm(forms.ModelForm):
    date = forms.DateTimeField(
        widget= forms.DateInput(
            attrs = {
                'class':'form-control',
                'type' :'date'
            }
        ),
     )

    class Meta:
        model = Expenses
        fields = ('date', 'price', 'category','description', 'payment_method')
        labels = {
            'date': 'data',
            'price': 'cena',
            'category': 'kategoria',
            'description': 'opis',
            'payment_method': 'płatność'
        }
    

    def __init__ (self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
    

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['month', 'amount']
        widgets = {
            'month': forms.DateInput(attrs={'type': 'month', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }