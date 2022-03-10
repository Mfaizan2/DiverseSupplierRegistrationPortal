from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')


def diverseCertificationData(request):
    print("Hhhh")
    labels = [ 'Minority-Owned Business', 'Women-Owned Business', 'Veteran-Owned Business', 'Other Certification' ]
    return JsonResponse({'email_error': labels}, status=200)
