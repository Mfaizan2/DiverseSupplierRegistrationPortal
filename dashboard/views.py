from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from registration.models import *
from django.db.models import Q
from django.db import connection
from django.db.models import Count


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def mapCountryNameById(id):
    if id==2:
        return "Canada"
    elif id == 1:
        return "United States"
    elif id == 3:
        return "Maxico"

def mapNaLocation(id):
    if id==1:
        return "CAN"
    elif id == 2:
        return "Global"
    elif id == 3:
        return "MX"
    elif id == 4:
        return "US"

def mapOems(id):
    if id==1:
        return "BMW"
    elif id == 2:
        return "Cummins"
    elif id == 3:
        return "FCA"
    elif id == 4:
        return "Ford"
    elif id == 5:
        return "Fuji"
    elif id == 6:
        return "GM"
    elif id == 7:
        return "Honda"
    elif id == 8:
        return "Hyundai/ Kia"
    elif id == 9:
        return "Mazda"
    elif id == 10:
        return "Mercedes/ Daimler"
    elif id == 11:
        return "Mitsubishi"
    elif id == 12:
        return "Navistar"
    elif id == 13:
        return "Nissan"
    elif id == 14:
        return "Toyota"
    elif id == 15:
        return "VW"


def diverseCertificationData(request):


    labels = [ 'Minority-Owned Business', 'Women-Owned Business', 'Veteran-Owned Business', 'Other Certification' ]
    
    BusinessAndCertificationYes = BusinessAndCertification.objects.filter(business='yes').count()
    BusinessAndCertificationNo = BusinessAndCertification.objects.filter(business='no').count()
    BusinessAndCertificationInProgress = BusinessAndCertification.objects.filter(business='In Progress').count()

    WomenOwnedBusinessYes = WomenOwnedBusiness.objects.filter(business='yes').count()
    WomenOwnedBusinessNo = WomenOwnedBusiness.objects.filter(business='no').count()
    WomenOwnedBusinessInProgress = WomenOwnedBusiness.objects.filter(business='In Progress').count()

    VeteranOwnedBusinessYes = VeteranOwnedBusiness.objects.filter(business='yes').count()
    VeteranOwnedBusinessNo = VeteranOwnedBusiness.objects.filter(business='no').count()
    VeteranOwnedBusinessInProgress = VeteranOwnedBusiness.objects.filter(business='In Progress').count()

    OtherCertificationYes = OtherCertification.objects.filter(business='yes').count()
    OtherCertificationNo = OtherCertification.objects.filter(business='no').count()
    OtherCertificationInProgress = OtherCertification.objects.filter(business='In Progress').count()
    
    ApplicationReceived = ABCCorporation.objects.all().count()

    ApplicationsResponse = ABCCorporation.objects.filter(~Q(response=0)).count()

    ApplicationsEmailed = ABCCorporation.objects.filter(~Q(emailed=0)).count()

    totalCountries = GeneralContactInfo.objects.values('country').annotate(count=Count('country')).order_by('country')

    totalCountriesArray = []
    totalCountriesCount = []

    for r in range(0,len(totalCountries)):
        totalCountriesArray.append(mapCountryNameById(totalCountries[r]['country']))
        totalCountriesCount.append(totalCountries[r]['count'])


    totalNaLocation = ProductionCapabilities.objects.values('record_per_naLocation').annotate(count=Count('record_per_naLocation')).order_by('record_per_naLocation')

    totalNaLocationArray = []
    totalNaLocationCount = []

    for r in range(0,len(totalNaLocation)):
        totalNaLocationArray.append(mapNaLocation(totalNaLocation[r]['record_per_naLocation']))
        totalNaLocationCount.append(totalNaLocation[r]['count'])


    totalOemsIds = ProductionCapabilities.objects.values('oems_id').annotate(count=Count('oems_id')).order_by('oems_id')

    totalOemsArray = []
    totalOemsArrayCount = []

    for r in range(0,len(totalOemsIds)):
        totalOemsArray.append(mapOems(totalOemsIds[r]['oems_id']))
        totalOemsArrayCount.append(totalOemsIds[r]['count'])

    

    


    # ProductionCapabilities.objects.values('oems_id').order_by('oems_id')
    totalNpmValues = ProductAndService.objects.values('npm_value').annotate(count=Count('npm_value')).order_by('npm_value')

    totalNpmValuesArray = []
    totalNpmValuesCount = []

    for r in range(0,len(totalNpmValues)):
        totalNpmValuesArray.append(totalNpmValues[r]['npm_value'])
        totalNpmValuesCount.append(totalNpmValues[r]['count'])




    totalPmValues = ProductAndService.objects.values('pm_value').annotate(count=Count('pm_value')).order_by('pm_value')

    totalPmValuesArray = []
    totalPmValuesCount = []
    
    for r in range(0,len(totalPmValues)):
        totalPmValuesArray.append(totalPmValues[r]['pm_value'])
        totalPmValuesCount.append(totalPmValues[r]['count'])



    
    
    return JsonResponse({'email_error': labels, 
                         'BusinessAndCertificationYes': BusinessAndCertificationYes, 'BusinessAndCertificationInProgress': BusinessAndCertificationInProgress,'BusinessAndCertificationNo': BusinessAndCertificationNo,
                          'WomenOwnedBusinessYes': WomenOwnedBusinessYes, 'WomenOwnedBusinessNo': WomenOwnedBusinessNo, 'WomenOwnedBusinessInProgress': WomenOwnedBusinessInProgress,
                         'VeteranOwnedBusinessYes': VeteranOwnedBusinessYes, 'VeteranOwnedBusinessNo': VeteranOwnedBusinessNo, 'VeteranOwnedBusinessInProgress': VeteranOwnedBusinessInProgress,
                         'OtherCertificationYes': OtherCertificationYes, 'OtherCertificationNo': OtherCertificationNo, 'OtherCertificationInProgress': OtherCertificationInProgress,
                         'totalCountriesArray': totalCountriesArray, 'totalCountriesCount': totalCountriesCount,
                         'totalNaLocationArray': totalNaLocationArray, 'totalNaLocationCount': totalNaLocationCount,
                         'ApplicationReceived': ApplicationReceived,
                         'ApplicationsResponse': ApplicationsResponse, 'ApplicationsEmailed': ApplicationsEmailed,
                         'totalOemsArray':totalOemsArray, 'totalOemsArrayCount':totalOemsArrayCount,

                         
                         'totalNpmValuesArray':totalNpmValuesArray, 'totalNpmValuesCount':totalNpmValuesCount,
                         'totalPmValuesArray': totalPmValuesArray, 'totalPmValuesCount': totalPmValuesCount
                         
                         },
                          status=200)


