from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from registration.models import *
from django.db.models import Q
from django.db import connection


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')


def diverseCertificationData(request):
    print("Hhhh")
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

    cursor = connection.cursor()
    cursor.execute('''SELECT name FROM registration_oems group by name''')
    row = cursor.fetchone()
    if row:
        row = list(row)
    doughnutDataOemForRecordPerOem = row

    doughnutDataOemForRecordPerOemData = []

    if doughnutDataOemForRecordPerOem:
        for r in range(0,len(doughnutDataOemForRecordPerOem)):
            temp = OEMS.objects.filter(name=doughnutDataOemForRecordPerOem[r]).count()
            doughnutDataOemForRecordPerOemData.append(temp)


    cursor.execute('''SELECT npm_value FROM registration_productandservice group by npm_value''')
    row = cursor.fetchone()
    if row:
        row = list(row)

    doughnutDataOemForNPM = row

    doughnutDataForNPM = []


    if doughnutDataOemForNPM:
        for r in range(0,len(doughnutDataOemForNPM)):
            # temp = ProductAndService.objects.filter(npmValue=doughnutDataOemForNPM[r]).count()
            query = "SELECT count(*) FROM registration_productandservice where npm_value='{}'".format(doughnutDataOemForNPM[r])
            cursor.execute(query)
            temp = cursor.fetchone()
            temp = list(temp)
            doughnutDataForNPM.append(temp[0])


    cursor.execute('''SELECT pm_value FROM registration_productandservice group by pm_value''')
    row = cursor.fetchone()
    if row:
        row = list(row)

    doughnutDataOemForPM = row

    doughnutDataForPM = []


    if doughnutDataOemForPM:
        for r in range(0,len(doughnutDataOemForPM)):
            # temp = ProductAndService.objects.filter(npmValue=doughnutDataOemForNPM[r]).count()
            query = "SELECT count(*) FROM registration_productandservice where npm_value='{}'".format(doughnutDataOemForNPM[r])
            cursor.execute(query)
            temp = cursor.fetchone()
            temp = list(temp)
            doughnutDataForPM.append(temp[0])




    
    
    return JsonResponse({'email_error': labels, 
                         'BusinessAndCertificationYes': BusinessAndCertificationYes, 'BusinessAndCertificationInProgress': BusinessAndCertificationInProgress,'BusinessAndCertificationNo': BusinessAndCertificationNo,
                          'WomenOwnedBusinessYes': WomenOwnedBusinessYes, 'WomenOwnedBusinessNo': WomenOwnedBusinessNo, 'WomenOwnedBusinessInProgress': WomenOwnedBusinessInProgress,
                         'VeteranOwnedBusinessYes': VeteranOwnedBusinessYes, 'VeteranOwnedBusinessNo': VeteranOwnedBusinessNo, 'VeteranOwnedBusinessInProgress': VeteranOwnedBusinessInProgress,
                         'OtherCertificationYes': OtherCertificationYes, 'OtherCertificationNo': OtherCertificationNo, 'OtherCertificationInProgress': OtherCertificationInProgress,
                         'ApplicationReceived': ApplicationReceived,
                         'ApplicationsResponse': ApplicationsResponse, 'ApplicationsEmailed': ApplicationsEmailed,

                         'doughnutDataOemForRecordPerOem':doughnutDataOemForRecordPerOem, 'doughnutDataOemForRecordPerOemData': doughnutDataOemForRecordPerOemData,
                         'doughnutDataOemForNPM':doughnutDataOemForNPM, 'doughnutDataForNPM':doughnutDataForNPM,
                         'doughnutDataOemForPM': doughnutDataOemForPM, 'doughnutDataForPM':doughnutDataForPM
                         
                         },
                          status=200)


