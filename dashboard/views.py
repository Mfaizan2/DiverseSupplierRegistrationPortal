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
    GeneralContactInfoT = GeneralContactInfo.objects.filter(company_name='fnmnm').first()


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



    totalOemsIds = ProductionCapabilities.objects.values('oems_id').order_by('oems_id')


    totalOemsIdsArray = []
    
    for r in range(0,len(totalOemsIds)):
        totalOemsIdsArray.append(totalOemsIds[r]['oems_id'])

    totalOems = OEMS.objects.filter(id__in=totalOemsIdsArray)


    doughnutDataOemForRecordPerOem = []

    for r in range(0,len(totalOems)):
        doughnutDataOemForRecordPerOem.append(totalOems[r].name)

    doughnutDataOemForRecordPerOemData = []

    if doughnutDataOemForRecordPerOem:
        for r in range(0,len(doughnutDataOemForRecordPerOem)):
            temp = OEMS.objects.filter(name=doughnutDataOemForRecordPerOem[r]).count()
            doughnutDataOemForRecordPerOemData.append(temp)




    # ProductionCapabilities.objects.values('oems_id').order_by('oems_id')
    temp = ProductAndService.objects.values('npm_value').order_by('npm_value')

    doughnutDataOemForNPMArray = []
    
    for m in range(0,len(temp)):
        doughnutDataOemForNPMArray.append(temp[m]['npm_value'])

    doughnutDataOemForNPM = doughnutDataOemForNPMArray

    doughnutDataForNPM = []


    if doughnutDataOemForNPM:
        for r in range(0,len(doughnutDataOemForNPM)):
            totalCount = ProductAndService.objects.filter(npm_value=doughnutDataOemForNPM[r]).count()
            doughnutDataForNPM.append(totalCount)




    temp = ProductAndService.objects.values('pm_value').order_by('pm_value')

    doughnutDataOemForPMArray = []

    for m in range(0,len(temp)):
        doughnutDataOemForPMArray.append(temp[m]['pm_value'])

    doughnutDataOemForPM = doughnutDataOemForPMArray

    doughnutDataForPM = []


    if doughnutDataOemForPM:
        for r in range(0,len(doughnutDataOemForPM)):
            # temp = ProductAndService.objects.filter(npmValue=doughnutDataOemForNPM[r]).count()
            # query = "SELECT count(*) FROM registration_productandservice where npm_value='{}'".format(doughnutDataOemForPM[r])
            # cursor.execute(query)
            # temp = cursor.fetchone()
            # temp = list(temp)
            totalCount = ProductAndService.objects.filter(pm_value=doughnutDataOemForPM[r]).count()
            doughnutDataForPM.append(totalCount)




    
    
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


