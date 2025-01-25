from django import forms
from .models import Expenses

class ExpensesForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = ('date', 'price', 'category','description' )
        labels = {
            'date': 'data',
            'price': 'cena',
            'category': 'kategoria',
            'description': 'opis',
        }
    

    def __init__ (self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Wybierz"
        self.fields['description'].required = False
    
    date = forms.DateTimeField(
        widget= forms.DateInput(
            attrs = {
                'class':'form-control',
                'type' :'date'
            }
        ),
    
    )

