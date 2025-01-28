
from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from MojeFinanse import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('expenses/', include('MojeFinanse.urls'))
] + debug_toolbar_urls()
