from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from registration.models import *
from django.db.models import Q


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')


def diverseCertificationData(request):
    print("Hhhh")
    labels = [ 'Minority-Owned Business', 'Women-Owned Business', 'Veteran-Owned Business', 'Other Certification' ]
    
    BusinessAndCertificationYes = BusinessAndCertification.objects.filter(Business='yes').count()
    BusinessAndCertificationNo = BusinessAndCertification.objects.filter(Business='no').count()
    BusinessAndCertificationInProgress = BusinessAndCertification.objects.filter(Business='In Progress').count()

    WomenOwnedBusinessYes = WomenOwnedBusiness.objects.filter(Business='yes').count()
    WomenOwnedBusinessNo = WomenOwnedBusiness.objects.filter(Business='no').count()
    WomenOwnedBusinessInProgress = WomenOwnedBusiness.objects.filter(Business='In Progress').count()

    VeteranOwnedBusinessYes = VeteranOwnedBusiness.objects.filter(Business='yes').count()
    VeteranOwnedBusinessNo = VeteranOwnedBusiness.objects.filter(Business='no').count()
    VeteranOwnedBusinessInProgress = VeteranOwnedBusiness.objects.filter(Business='In Progress').count()

    OtherCertificationYes = OtherCertification.objects.filter(Business='yes').count()
    OtherCertificationNo = OtherCertification.objects.filter(Business='no').count()
    OtherCertificationInProgress = OtherCertification.objects.filter(Business='In Progress').count()
    
    ApplicationReceived = ABCCorporation.objects.all().count()

    ApplicationsResponse = ABCCorporation.objects.filter(~Q(response=0)).count()

    ApplicationsEmailed = ABCCorporation.objects.filter(~Q(emailed=0)).count()


    
    
    return JsonResponse({'email_error': labels, 
                         'BusinessAndCertificationYes': BusinessAndCertificationYes, 'BusinessAndCertificationInProgress': BusinessAndCertificationInProgress,'BusinessAndCertificationNo': BusinessAndCertificationNo,
                          'WomenOwnedBusinessYes': WomenOwnedBusinessYes, 'WomenOwnedBusinessNo': WomenOwnedBusinessNo, 'WomenOwnedBusinessInProgress': WomenOwnedBusinessInProgress,
                         'VeteranOwnedBusinessYes': VeteranOwnedBusinessYes, 'VeteranOwnedBusinessNo': VeteranOwnedBusinessNo, 'VeteranOwnedBusinessInProgress': VeteranOwnedBusinessInProgress,
                         'OtherCertificationYes': OtherCertificationYes, 'OtherCertificationNo': OtherCertificationNo, 'OtherCertificationInProgress': OtherCertificationInProgress,
                         'ApplicationReceived': ApplicationReceived,
                         'ApplicationsResponse': ApplicationsResponse, 'ApplicationsEmailed': ApplicationsEmailed
                         
                         },
                          status=200)


