from django.contrib import admin
from .models import Category, Expenses , PaymentMethod, Budget

admin.site.register(Category)
admin.site.register(Expenses)
admin.site.register(PaymentMethod)
admin.site.register(Budget)