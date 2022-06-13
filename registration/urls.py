from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('Registration', views.Registration, name='Registration'),
    path('allRecords', views.AllRecords, name='allRecords'),
    path('allRecords1', csrf_exempt(views.AllRecords1), name='allRecords1'),
    path('allRecords2', csrf_exempt(views.AllRecords2), name='allRecords2'),
    path('favouriteRecode', csrf_exempt(views.favouriteRecode), name='favouriteRecode'),
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
    path('addFavoriteList', csrf_exempt(views.addFavoriteList), name='addFavoriteList'),
    path('getFavoriteLists', csrf_exempt(views.GetFavoriteLists), name='getFavoriteLists'),
    path('addRecordToFavoriteList', csrf_exempt(views.AddRecordToFavoriteList), name='addRecordToFavoriteList'),
    path('favouriteRecodeList/<str:id>', csrf_exempt(views.favouriteRecodeList), name='favouriteRecodeList'),
    path('sendFavoriteList', csrf_exempt(views.SendFavoriteList), name='sendFavoriteList'),
    path('getFavoriteRecordsList', csrf_exempt(views.GetFavoriteRecordsList), name='getFavoriteRecordsList'),
    path('migrateData', views.MigrateData, name='migrateData'),
    
]