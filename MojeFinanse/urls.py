
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.expenses_form, name='expenses_insert'),
    path('<int:id>/',views.expenses_form, name='expenses_update'),
    path('delete/<int:id>/', views.expenses_delete, name='expenses_delete'),
    path('list/', views.expenses_list, name='expenses_list')
] 

