from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),

]