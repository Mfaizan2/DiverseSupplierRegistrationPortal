from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('Registration', views.Registration, name='Registration'),
    path('allRecords', views.AllRecords, name='allRecords'),
    path('favouriteRecode', views.favouriteRecode, name='favouriteRecode'),
    path('detailRecord/<int:id>', views.DetailRecord, name='detailRecord'),
    path('bulkUpload', views.BulkUpload, name='bulkUpload'),
    path('downloadSampleExcelFile', views.DownloadSampleExcelFile, name='downloadSampleExcelFile'),
    path('uploadExcelFile', views.UploadExcelFile, name='uploadExcelFile'),
    path('sendResponseToSubmitter', views.SendResponseToSubmitter, name='sendResponseToSubmitter'),
    path('sendResponseToSomeone/<int:id>', views.SendResponseToSomeone, name='sendResponseToSomeone'),
    path('report/<int:id>/<str:email_address>', views.Report, name='report'),
    path('sendFeedback', views.SendFeedback, name='sendFeedback'),
    path('getFeedbacks', views.GetFeedbacks, name='getFeedbacks'),
    path('removeNote/<int:id>', views.removeNote, name='removeNote'),
    path('addNote', csrf_exempt(views.addNote), name='addNote'),
]