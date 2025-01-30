
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', views.expenses_form, name='expenses_insert'),
    path('expenses/<int:id>/', views.expenses_form, name='expenses_update'),
    path('expenses/delete/<int:id>/', views.expenses_delete, name='expenses_delete'),
    path('expenses/list/', views.expenses_list, name='expenses_list'), 
    path('expenses/monthly_summary/', views.monthly_summary, name='monthly_summary'),
    path('expenses/weekly_summary/', views.weekly_summary, name='weekly_summary'),
    path('expenses/budget_summary/', views.budget_summary, name='budget_summary'),
]
