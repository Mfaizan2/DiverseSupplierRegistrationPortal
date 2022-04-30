from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    

]