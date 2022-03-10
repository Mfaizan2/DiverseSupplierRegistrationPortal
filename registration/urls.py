from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('Registration', views.Registration, name='Registration'),
    path('allRecords', views.AllRecords, name='allRecords'),
    path('detailRecord/<int:id>', views.DetailRecord, name='detailRecord'),

]