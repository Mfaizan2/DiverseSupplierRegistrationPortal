from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_attempt, name='login'),

]