import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registration.models import *
from django.contrib import messages
from django.core.paginator import Paginator
import xlwt
from django.http import HttpResponse
import openpyxl
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
import pandas as pd
import csv
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import imaplib, email, getpass
from email import policy


def upload(container_name, file_path, file_name):
    from azure.storage.blob import (
        BlobServiceClient,
        PublicAccess,
        ContainerClient,
    )
    from datetime import datetime, timedelta

    now = str(datetime.now()).split(" ")[1]
    print("now", now)
    file_name = file_name.replace(" ", "")
    file_name = now.replace(" ", "") + file_name
    container_client = ContainerClient.from_connection_string(
        "BlobEndpoint=https://webappmuh.blob.core.windows.net/;QueueEndpoint=https://webappmuh.queue.core.windows.net/;FileEndpoint=https://webappmuh.file.core.windows.net/;TableEndpoint=https://webappmuh.table.core.windows.net/;SharedAccessSignature=sv=2020-08-04&ss=bfqt&srt=co&sp=rwdlacupx&se=2025-04-27T15:10:20Z&st=2022-04-22T07:10:20Z&spr=https&sig=5q1UtBRUUxP23oGBcKiv1c5mXMVDh1M9HYAbYrVPx1E%3D",
        container_name)

    print("Uploading files")

    blob_client = container_client.get_blob_client(file_name)
    blob_client.upload_blob(file_path)
    print("File_uploaded")

    from azure.storage.blob import BlobClient, generate_blob_sas, BlobSasPermissions

    account_name = 'webappmuh'
    account_key = 'Ob9SQssWcPW8hAb6GEOu2xaCHiMv1Q5BV5fdHPoioUW8hktZIQIyTOjvx5gOmv7GYCSy6e9cN+RW+AStbBskSA=='

    sas_blob = generate_blob_sas(account_name=account_name,
                                 container_name=container_name,
                                 blob_name=file_name,
                                 account_key=account_key,
                                 permission=BlobSasPermissions(read=True),
                                 expiry=datetime.utcnow() + timedelta(hours=26280)
                                 )

    url = 'https://' + account_name + '.blob.core.windows.net/' + container_name + '/' + file_name + '?' + sas_blob
    print("url", url)
    return url


# Create your views here.

def Registration(request):
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]

    try:
        if request.method == 'POST':

            # try:
            # General Contact Info
            # print(request.POST['campany_name'])
            feedbackDescription = request.POST.get('feedbackDescription', None)
            campany_name = request.POST.get('campany_name', None)
            # print(request.POST.get('website_url'])
            website_url = request.POST.get('website_url', None)
            company_video_link = request.POST.get('company_video_link', None)
            if request.FILES.get('company_video_file', None):
                company_video_file = request.FILES.get('company_video_file', None)

                company_video_file = upload("company-details", company_video_file, company_video_file.name)
            else:
                company_video_file = ''
            # print(request.POST.get('address1',None))
            address1 = request.POST.get('address1', None)
            # print(request.POST.get('address2',None))
            address2 = request.POST.get('address2', None)
            # print(request.POST.get('country',None))
            country = request.POST.get('country', None)
            # print(request.POST.get('city',None))
            city = request.POST.get('city', None)
            # print(request.POST.get('state',None))
            state = request.POST.get('state', None)
            # print(request.POST.get('zip_code',None))
            zip_code = request.POST.get('zip_code', None)

            # print(request.POST.get('sales_contact_first_name',None))
            sales_contact_first_name = request.POST.get('sales_contact_first_name', None)
            # print(request.POST.get('sales_contact_last_name',None))
            sales_contact_last_name = request.POST.get('sales_contact_last_name', None)
            # print(request.POST.get('sales_contact_email',None))
            sales_contact_email = request.POST.get('sales_contact_email', None)
            # print(request.POST.get('sales_contact_job_title',None))
            sales_contact_job_title = request.POST.get('sales_contact_job_title', None)
            # print(request.POST.get('sales_contact_phone',None))
            sales_contact_phone = request.POST.get('sales_contact_phone', None)
            # print(request.POST.get('sales_contact_mobile',None))
            sales_contact_mobile = request.POST.get('sales_contact_mobile', None)

            # print(request.POST.get('general_contact_first_name',None))
            general_contact_first_name = request.POST.get('general_contact_first_name', None)
            # print(request.POST.get('general_contact_last_name',None))
            general_contact_last_name = request.POST.get('general_contact_last_name', None)
            # print(request.POST.get('general_contact_email',None))
            general_contact_email = request.POST.get('general_contact_email', None)
            # print(request.POST.get('general_contact_job_title',None))
            general_contact_job_title = request.POST.get('general_contact_job_title', None)
            # print(request.POST.get('general_contact_phone',None))
            general_contact_phone = request.POST.get('general_contact_phone', None)
            # print(request.POST.get('general_contact_mobile',None))
            general_contact_mobile = request.POST.get('general_contact_mobile', None)
            # ----------------------------------

            # Diverse Certification

            # print(request.POST.get('mbe_business',None))
            mbe_business = request.POST.get('mbe_business', None)
            # print(request.POST.get('mbe_council',None))
            mbe_council = request.POST.get('mbe_council', None)
            # print(request.POST.get('mbe_ethnicity',None))
            mbe_ethnicity = request.POST.get('mbe_ethnicity', None)
            # print(request.POST.get('mbe_certificationDescription',None))
            mbe_certificationDescription = request.POST.get('mbe_certificationDescription', None)

            if request.FILES.get('MobCertificationFile', None):
                mbe_certification_file = request.FILES.get('MobCertificationFile', None)
                mbe_certification_file = upload("minority-owned-business", mbe_certification_file,
                                                mbe_certification_file.name)
                print("mbe_certification_file", mbe_certification_file)
            else:
                mbe_certification_file = ''
            # print(request.POST.get('mbe_expirationDate',None))
            mbe_expirationDate = str(request.POST.get('mbe_expirationDate', None))

            if mbe_expirationDate:
                mbe_expirationDate = mbe_expirationDate.split('-')

                mbe_expirationDate = datetime.date(int(mbe_expirationDate[0]), int(mbe_expirationDate[1]),
                                                   int(mbe_expirationDate[2]))

            # print(request.POST.get('wbe_business',None))
            wbe_business = request.POST.get('wbe_business', None)
            # print(request.POST.get('wbe_council',None))
            wbe_council = request.POST.get('wbe_council', None)
            # print(request.POST.get('wbe_ethnicity',None))
            # wbe_ethnicity = "xyz"
            # print(request.POST.get('wbe_certificationDescription',None))
            wbe_certificationDescription = request.POST.get('wbe_certificationDescription', None)
            if request.FILES.get('WobCertificationFile', None):
                wbe_certification_file = request.FILES.get('WobCertificationFile', None)
                wbe_certification_file = upload("women-owned-business", wbe_certification_file,
                                                wbe_certification_file.name)
                print("wbe_certification_file", wbe_certification_file)
            else:
                wbe_certification_file = ''
            # print(request.POST.get('wbe_expirationDate',None))
            wbe_expirationDate = str((request.POST.get('wbe_expirationDate', None)))
            if wbe_expirationDate:
                wbe_expirationDate = wbe_expirationDate.split('-')
                wbe_expirationDate = datetime.date(int(wbe_expirationDate[0]), int(wbe_expirationDate[1]),
                                                   int(wbe_expirationDate[2]))

            # print(request.POST.get('vb_business',None))
            vb_business = request.POST.get('vb_business', None)
            # print(request.POST.get('vb_council',None))
            vb_council = request.POST.get('vb_council', None)
            # print(request.POST.get('vb_ethnicity',None))
            # vb_ethnicity = "xyz"
            # print(request.POST.get('vb_certificationDescription',None))
            vb_certificationDescription = request.POST.get('vb_certificationDescription', None)

            if request.FILES.get('VobCertificationFile', None):
                vb_certification_file = request.FILES.get('VobCertificationFile', None)
                vb_certification_file = upload("veteran-owned-business", vb_certification_file,
                                               vb_certification_file.name)

                print("vb_certification_file", vb_certification_file)
            else:
                vb_certification_file = ''

            vb_expirationDate = str(request.POST.get('vb_expirationDate', None))

            if vb_expirationDate:
                vb_expirationDate = vb_expirationDate.split('-')

                vb_expirationDate = datetime.date(int(vb_expirationDate[0]), int(vb_expirationDate[1]),
                                                  int(vb_expirationDate[2]))

            # print(request.POST.get('other_certification_business',None))
            other_certification_business = request.POST.get('other_certification_business', None)
            # print(request.POST.get('other_certification_council',None))
            other_certification_council = request.POST.get('other_certification_council', None)
            # print(request.POST.get('other_certification_ethnicity',None))
            # other_certification_ethnicity = "xyz"
            # print(request.POST.get('other_certification_certificationDescription',None))
            other_certification_certificationDescription = request.POST.get(
                'other_certification_certificationDescription', None)

            if request.FILES.get('CobCertificationFile', None):
                other_certification_file = request.FILES.get('CobCertificationFile', None)
                other_certification_file = upload("other-certification", other_certification_file,
                                                  other_certification_file.name)

                print("other_certification_file", other_certification_file)
            else:
                other_certification_file = ''

            # print(request.POST.get('other_certification_expirationDate',None))
            other_certification_expirationDate = str(
                request.POST.get('other_certification_expirationDate', None))

            if other_certification_expirationDate:
                other_certification_expirationDate = other_certification_expirationDate.split('-')
                other_certification_expirationDate = datetime.date(int(other_certification_expirationDate[0]),
                                                                   int(other_certification_expirationDate[1]),
                                                                   int(other_certification_expirationDate[2]))

            # --------------------------------------

            # Company Details

            # print(request.POST.get('presentationDescription',None))
            presentationDescription = request.POST.get('presentationDescription', None)

            if request.FILES.get('presentationFile', None):
                presentation_file = request.FILES.get('presentationFile', None)
                presentation_file = upload("company-details", presentation_file, presentation_file.name)
            else:
                presentation_file = ''

            # print(request.POST.get('numberOfEmployees',None))
            numberOfEmployees = request.POST.get('numberOfEmployees', None)
            # print(request.POST.get('taxIdVatNumber',None))
            taxIdVatNumber = request.POST.get('taxIdVatNumber', None)
            # print(request.POST.get('totalAnnaulSales',None))
            totalAnnaulSales = request.POST.get('totalAnnaulSales', None)
            # print(request.POST.get('DunsNumber',None))
            DunsNumber = request.POST.get('DunsNumber', None)
            # print(request.POST.get('qualityCertification',None))
            qualityCertification = request.POST.get('qualityCertification', None)
            # print(request.POST.get('certificationExpectedDate',None))
            certificationExpectedDate = str(request.POST.get('certificationExpectedDate', None))
            if certificationExpectedDate:
                certificationExpectedDate = certificationExpectedDate.split('-')

                certificationExpectedDate = datetime.date(int(certificationExpectedDate[0]),
                                                          int(certificationExpectedDate[1]),
                                                          int(certificationExpectedDate[2]))
            # print(request.POST.get('operationOutsideUsa',None))
            operationOutsideUsa = request.POST.get('operationOutsideUsa', None)

            # --------------------------------------

            # Production Capability
            # print(request.POST.get('isOem',None))
            isOem = request.POST.get('isOem', False)
            # print(request.POST.get('oEMS',None))
            oEMS = request.POST.get('oEMS', None)
            if oEMS:
                oEMS = OEMS.objects.filter(name=oEMS).first()
            # print(request.POST.get('JIT',None))
            JIT = request.POST.get('JIT', False)
            # print(request.POST.get('AbcSupplier',None))
            AbcSupplier = request.POST.get('AbcSupplier', False)
            # print(request.POST.get('vendorNumber',None))
            vendorNumber = int(request.POST.get('vendorNumber', None))
            # print(request.POST.get('anyOtherTier1AutomotiveCompany',None))
            anyOtherTier1AutomotiveCompany = request.POST.get('anyOtherTier1AutomotiveCompany', False)
            # print(request.POST.get('vmi',None))
            VMI = request.POST.get('vmi', False)
            print(request.POST.get('percentageSale', None))
            percentageSale = request.POST.get('percentageSale', None)
            if percentageSale:
                percentageSale = int(percentageSale)
            print(request.POST.get('significantAwards', None))
            significantAwards = request.POST.get('significantAwards', None)
            # print(request.POST.get('customerName1',None))
            customerName1 = request.POST.get('customerName1', None)
            # print(request.POST.get('sales1',None))
            sales1 = request.POST.get('sales1', None)
            if sales1:
                sales1 = int(sales1)
            # print(request.POST.get('automotive1',None))
            automotive1 = request.POST.get('automotive1', False)
            # print(request.POST.get('customerName2',None))
            customerName2 = request.POST.get('customerName2', None)
            # print(request.POST.get('sales2',None))
            sales2 = request.POST.get('sales2', None)
            if sales2:
                sales2 = int(sales2)
            # print(request.POST.get('automotive2',None))
            automotive2 = request.POST.get('automotive2', False)
            # print(request.POST.get('customerName3',None))
            customerName3 = request.POST.get('customerName3', None)
            # print(request.POST.get('sales3',None))
            sales3 = request.POST.get('sales3', None)
            if sales3:
                sales3 = int(sales3)
            # print(request.POST.get('automotive3',None))
            automotive3 = request.POST.get('automotive3', False)
            # print(request.POST.get('recordPerNaLocation',None))
            recordPerNaLocation = request.POST.get('recordPerNaLocation', None)
            # print(request.POST.get('manufacturingLocations',None))
            manufacturingLocations = request.POST.get('manufacturingLocations', None)
            # print(request.POST.get('event',None))
            event = request.POST.get('event', None)

            # -----------------------------------------------

            # Production and services
            # print(request.POST.get('npmValue',None))
            npmValue = request.POST.get('npmValue', None)
            # print(request.POST.get('npmValueCategory1',None))
            npmValueCategory1 = request.POST.get('npmValueCategory1', None)
            # print(request.POST.get('npmValueCategory2',None))
            npmValueCategory2 = request.POST.get('npmValueCategory2', None)

            npmSelectedValueFinal = request.POST.get('npmSelectedValueFinal', None)

            # print(request.POST.get('pmValue',None))
            pmValue = request.POST.get('pmValue', None)
            # print(request.POST.get('pmValueCategory1',None))
            pmValueCategory1 = request.POST.get('pmValueCategory1', None)
            # print(request.POST.get('pmValueCategory2',None))
            pmValueCategory2 = request.POST.get('pmValueCategory2', None)
            # print(request.POST.get('additoinalProductAndServices',None))
            additoinalProductAndServices = request.POST.get('additoinalProductAndServices', None)

            pmSelectedValueFinal = request.POST.get('pmSelectedValueFinal', None)

            # ------------------------------------------------

            salesContact = SalesContact()
            if sales_contact_first_name:
                salesContact.first_name = sales_contact_first_name
            if sales_contact_last_name:
                salesContact.last_name = sales_contact_last_name
            if sales_contact_email:
                salesContact.email = sales_contact_email
            if sales_contact_job_title:
                salesContact.job_title = sales_contact_job_title
            if sales_contact_phone:
                salesContact.phone_number = sales_contact_phone
            if sales_contact_mobile:
                salesContact.mobile_number = sales_contact_mobile
            salesContact.save()

            generalContact = GeneralContact()
            if general_contact_first_name:
                generalContact.first_name = general_contact_first_name
            if general_contact_last_name:
                generalContact.last_name = general_contact_last_name
            if general_contact_email:
                generalContact.email = general_contact_email
            if general_contact_job_title:
                generalContact.job_title = general_contact_job_title
            if general_contact_phone:
                generalContact.phone_number = general_contact_phone
            if general_contact_mobile:
                generalContact.mobile_number = general_contact_mobile
            generalContact.save()
            generalContact = GeneralContact.objects.filter(email=general_contact_email).first()

            print("country b", country)
            country = Country.objects.filter(country_name=country).first()

            generalContactInfo = GeneralContactInfo()
            generalContactInfo.company_name = campany_name
            generalContactInfo.website_url = website_url
            generalContactInfo.video_url = company_video_link
            generalContactInfo.company_video_file = company_video_file
            generalContactInfo.address1 = address1
            generalContactInfo.address2 = address2
            generalContactInfo.country = country
            generalContactInfo.city = city
            generalContactInfo.state = state
            generalContactInfo.zip_code = zip_code
            generalContactInfo.sales_contact = salesContact
            generalContactInfo.general_contact = generalContact
            generalContactInfo.save()

            print("mbe_business", mbe_business)
            businessAndCertification = BusinessAndCertification()
            businessAndCertification.business = mbe_business
            businessAndCertification.council = mbe_council
            businessAndCertification.ethnicity = mbe_ethnicity
            businessAndCertification.certification_description = mbe_certificationDescription
            businessAndCertification.certification_file = mbe_certification_file
            if mbe_expirationDate:
                businessAndCertification.expiration_date = mbe_expirationDate
            businessAndCertification.save()

            print("wbe_business", wbe_business)
            womenOwnedBusiness = WomenOwnedBusiness()
            womenOwnedBusiness.business = wbe_business
            womenOwnedBusiness.council = wbe_council
            # womenOwnedBusiness.ethnicity = wbe_ethnicity
            womenOwnedBusiness.certification_description = wbe_certificationDescription
            womenOwnedBusiness.certification_file = wbe_certification_file
            if wbe_expirationDate:
                womenOwnedBusiness.expiration_date = wbe_expirationDate
            womenOwnedBusiness.save()

            print("vb_business", vb_business)
            veteranOwnedBusiness = VeteranOwnedBusiness()
            veteranOwnedBusiness.business = vb_business
            veteranOwnedBusiness.council = vb_council
            # veteranOwnedBusiness.ethnicity = vb_ethnicity
            veteranOwnedBusiness.certification_description = vb_certificationDescription
            veteranOwnedBusiness.certification_file = vb_certification_file
            if vb_expirationDate:
                veteranOwnedBusiness.expiration_date = vb_expirationDate
            veteranOwnedBusiness.save()

            print("other_certification_business", other_certification_business)
            otherCertification = OtherCertification()
            otherCertification.business = other_certification_business
            otherCertification.council = other_certification_council
            # otherCertification.ethnicity = other_certification_ethnicity
            otherCertification.certification_description = other_certification_certificationDescription
            otherCertification.certification_file = other_certification_file
            if other_certification_expirationDate:
                otherCertification.expiration_date = other_certification_expirationDate
            otherCertification.save()

            diverseCertification = DiverseCertification()
            diverseCertification.minority_owned_business = businessAndCertification
            diverseCertification.women_owned_business = womenOwnedBusiness
            diverseCertification.other_certification = otherCertification
            diverseCertification.veteran_owned_business = veteranOwnedBusiness
            diverseCertification.save()

            companyDetails = CompanyDetails()
            companyDetails.presentation_description = presentationDescription
            companyDetails.presentation_file = presentation_file
            companyDetails.number_of_employees = numberOfEmployees
            companyDetails.tax_id_vat_number = taxIdVatNumber
            companyDetails.total_annaul_sales = totalAnnaulSales
            companyDetails.duns_number = DunsNumber
            companyDetails.quality_certification = qualityCertification
            if certificationExpectedDate:
                companyDetails.certification_expected_date = certificationExpectedDate
            companyDetails.operation_outside_usa = operationOutsideUsa
            companyDetails.save()

            naLocation = NaLocation.objects.filter(name=recordPerNaLocation).first()

            productionCapabilities = ProductionCapabilities()
            if isOem == 'Yes':
                isOem = True
            else:
                isOem = False
            if AbcSupplier == 'Yes':
                AbcSupplier = True
            else:
                isOem = False
            if VMI == 'Yes':
                VMI = True
            else:
                VMI = False
            if JIT == 'Yes':
                JIT = True
            else:
                JIT = False
            if automotive1 == 'Yes':
                automotive1 = True
            else:
                automotive1 = False
            if automotive2 == 'Yes':
                automotive2 = True
            else:
                automotive2 = False
            if automotive3 == 'Yes':
                automotive3 = True
            else:
                automotive3 = False
            if anyOtherTier1AutomotiveCompany == 'Yes':
                anyOtherTier1AutomotiveCompany = True
            else:
                anyOtherTier1AutomotiveCompany = False
            # print(isOem, AbcSupplier, VMI, JIT, automotive1, automotive2, automotive3)
            productionCapabilities.isOem = isOem
            if oEMS:
                productionCapabilities.oems = oEMS
            productionCapabilities.abc_supplier = AbcSupplier
            if vendorNumber:
                productionCapabilities.vendor_number = vendorNumber
            productionCapabilities.any_other_tier1_automotive_company = anyOtherTier1AutomotiveCompany
            productionCapabilities.nmi = VMI
            productionCapabilities.jit = JIT
            if percentageSale:
                productionCapabilities.percentage_sale = percentageSale
            productionCapabilities.significant_awards = significantAwards
            productionCapabilities.customer_name1 = customerName1
            productionCapabilities.sales1 = sales1
            productionCapabilities.automotive1 = automotive1
            productionCapabilities.customer_name2 = customerName2
            productionCapabilities.sales2 = sales2
            productionCapabilities.automotive2 = automotive2
            productionCapabilities.customer_name3 = customerName3
            productionCapabilities.sales3 = sales3
            productionCapabilities.automotive3 = automotive3
            productionCapabilities.record_per_naLocation = naLocation
            productionCapabilities.manufacturing_locations = manufacturingLocations
            productionCapabilities.event = event
            productionCapabilities.save()

            aBCCorporation = ABCCorporation()
            aBCCorporation.general_contant_info = generalContactInfo
            aBCCorporation.diverse_certification = diverseCertification
            aBCCorporation.company_details = companyDetails
            aBCCorporation.production_capabilities = productionCapabilities
            # aBCCorporation.product_and_service = productAndService
            aBCCorporation.save()

            if npmSelectedValueFinal:
                print("Faizan", npmSelectedValueFinal)
                npmSelectedValueFinal = npmSelectedValueFinal.split(',')
                for obj in npmSelectedValueFinal:

                    obj = obj.split('>')
                    npmValue = obj[0]
                    npmValueCategory1 = obj[1]
                    if obj[2]:
                        npmValueCategory2 = obj[2]
                    else:
                        npmValueCategory2 = ''
                    npmValues = NpmValues(abc_corporation_id=aBCCorporation.id, npm_value=npmValue,
                                          npm_value_category1=npmValueCategory1, npm_value_category2=npmValueCategory2)
                    npmValues.save()
                    print("Faizan")

            if pmSelectedValueFinal:
                print("zee", pmSelectedValueFinal)
                pmSelectedValueFinal = pmSelectedValueFinal.split(',')
                for obj in pmSelectedValueFinal:

                    obj = obj.split('>')
                    pmValue = obj[0]
                    if obj[1]:
                        pmValueCategory1 = obj[1]
                    else:
                        pmValueCategory1 = ''
                    pmValues = PmValues(abc_corporation_id=aBCCorporation.id, pm_value=pmValue,
                                        pm_value_category1=pmValueCategory1)
                    pmValues.save()
                    print("zee")

                print("Sending email")
                subject = 'New Application at ABC Supplier'

                message = "You have received a new application at ABC Supplier"

                email_from = settings.EMAIL_HOST_USER
                email = "faizanaslam455@gmail.com"
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list, fail_silently=False)

            messages.success(request, 'Application successfully submitted')
            return render(request, 'Registrationform.html')
            # except Exception as e:
            #     messages.error(request, e)
            #     print(e)
    except:
        messages.error(request, 'Error while doing registration')

    return render(request, 'Registrationform.html')


@login_required(login_url='/login')
def AllRecords(request):
    if request.method == 'POST':
        print("Faizan DON")
        last_name = request.POST.get('last_name', None)
        first_name = request.POST.get('first_name', None)
        city = request.POST.get('city', None)
        state = request.POST.get('state', None)
        address = request.POST.getlist('address', None)
        diverse_certification = request.POST.get('diverse_certification', None)
        wbe_certification = request.POST.getlist('wbe_certification', None)
        mbe = request.POST.getlist('mbe', None)
        vob = request.POST.getlist('vob', None)
        other_certification = request.POST.getlist('other_certification', None)
        quality_certification = request.POST.getlist('quality_certification', None)
        operation_outside_usa = request.POST.getlist('operation_outside_usa', None)
        npm = request.POST.getlist('npm', None)
        pm = request.POST.getlist('pm', None)
        print("npm", npm)



        kwargs = {}

        if last_name:
            kwargs['{0}__{1}__{2}'.format('general_contant_info', 'general_contact', 'last_name')] = last_name

        if first_name:
            kwargs['{0}__{1}__{2}'.format('general_contant_info', 'general_contact', 'first_name')] = first_name

        if city:
            kwargs['{0}__{1}'.format('general_contant_info', 'city')] = city

        if state:
            kwargs['{0}__{1}'.format('general_contant_info', 'state')] = state

        if address:
            kwargs['{0}__{1}__{2}__in'.format('general_contant_info', 'country','country_name')] = address

        if diverse_certification:
            
            kwargs['{0}__{1}__{2}__in'.format('diverse_certification', diverse_certification,'business')] = ['Yes', 'In Progress']
        if wbe_certification:
            
            kwargs['{0}__{1}__{2}__in'.format('diverse_certification', 'women_owned_business','council')] = wbe_certification

        if mbe:
            
            kwargs['{0}__{1}__{2}__in'.format('diverse_certification', 'minority_owned_business','council')] = mbe

        if vob:
            
            kwargs['{0}__{1}__{2}__in'.format('diverse_certification', 'veteran_owned_business','council')] = vob

        if other_certification:
            
            kwargs['{0}__{1}__{2}__in'.format('diverse_certification', 'other_certification','council')] = other_certification
        if quality_certification:
            kwargs['{0}__{1}__in'.format('company_details', 'quality_certification')] = quality_certification
        if operation_outside_usa:
            kwargs['{0}__{1}__in'.format('company_details', 'operation_outside_usa')] = operation_outside_usa
        if npm:
            all_objs = NpmValues.objects.filter(npm_value__in=npm)
            ids = []
            for obj in all_objs:
                ids.append(obj.abc_corporation_id)
            kwargs['{0}__in'.format('id')] = ids

        if pm:
            all_objs = PmValues.objects.filter(pm_value__in=pm)
            ids = []
            for obj in all_objs:
                ids.append(obj.abc_corporation_id)
            kwargs['{0}__in'.format('id')] = ids



        all_applications = ABCCorporation.objects.filter(**kwargs)
        print("all_applications", all_applications)


        npmValues = NpmValues.objects.all()
        pmValues = PmValues.objects.all()

        context = {
            'expenses': all_applications,
            'page_obj': all_applications,
            'npmValues': npmValues,
            'pmValues': pmValues
        }
        return render(request, 'allRecords.html', context)

    all_applications = ABCCorporation.objects.all()
    # paginator = Paginator(all_applications, 10)
    # page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, page_number)
    # print("all_applications", page_obj)
    npmValues = NpmValues.objects.all()
    pmValues = PmValues.objects.all()

    context = {
        'expenses': all_applications,
        'page_obj': all_applications,
        'npmValues': npmValues,
        'pmValues': pmValues
    }
    return render(request, 'allRecords.html', context)


def mapCountryName(name):
    if name == 'WY':
        return "Canada"
    elif name == 'AL':
        return "United States"
    elif name == 'MX':
        return "Maxico"


@login_required(login_url='/login')
def DetailRecord(request, id):
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]
    application = ABCCorporation.objects.filter(id=id).first()
    npmValues = NpmValues.objects.filter(abc_corporation_id=id)
    npmFinal = ''
    for obj in npmValues:
        npmFinal = npmFinal + obj.npm_value+ " > "+ obj.npm_value_category1+ " > "+ obj.npm_value_category2+ " | "

    pmValues = PmValues.objects.filter(abc_corporation_id=id)
    pmFinal = ''
    for obj in pmValues:
        pmFinal = pmFinal + obj.pm_value+ " > "+ obj.pm_value_category1+ " > "+ obj.pm_value_category2+ " | "


    country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()

    notes = Notes.objects.filter(application_id=id, user_id=request.user.id)
    
    notes_dic = {}
    
    for note in notes:
        notes_dic[note.id] = note.feedback
    
    
    dummyNotes = {
        1: "dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1 dummy note 1",
        2: "dummy note 2 dummy note 2 dummy note 2 dummy note 2 dummy note 2 dummy note 2",
        3: "dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3 dummy note 3",
    }
    context = {
        'application': application,
        'country': mapCountryName(country.country_name),
        'npmValues': npmFinal,
        'pmValues': pmFinal,
        'Notes_dic': notes_dic
    }
    return render(request, 'detailRecord.html', context)


@login_required(login_url='/login')
def BulkUpload(request):
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]
    return render(request, 'bulk.html')


@login_required(login_url='/login')
def DownloadSampleExcelFile(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    # decide file name
    response['Content-Disposition'] = 'attachment; filename="bulk_upload_template.xls"'

    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    # adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    # column header names, you can use your own headers here
    columns = ['Company Name', 'Website URL', "Company detail's Video link", 'Country', 'Address 1',
               'Address 2', 'Neighborhood', 'City', 'State', 'Postal Code',
               'Sales First Name', 'Sales Last Name', 'Sales Email Address',
               'Sales Job Title', 'Sales Office Phone', 'Sales Mobile Phone',
               'General First Name', 'General Last Name', 'General Email Address',
               'General Job Title', 'General Office Phone', 'General Mobile Phone',
               'Is your company certified by the National Minority Supplier Development Council (NMSDC) or one of its affiliates?',
               'MOB council', 'Ethnicity', 'MOB Certification Description', 'MOB Expiration Date',
               'MOB Certification Upload',
               'Is your company certified by the Women Business Enterprise National Council Development Council (WBENC) or one of it affiliates? *',
               'WOB council', 'WOB Certification Description', 'WOB Expiration Date', 'WOB Certification Upload',
               'Is your company a veteran-owned business', 'VOB council', 'VOB Certification Description',
               'VOB Expiration Date',
               'VOB Certification Upload', 'Is your company certified by another organization?', 'OC council',
               'OC Certification Description',
               'OC Expiration Date', 'OC Certification Upload', 'Presentation Upload', 'Description',
               'Number of Employees',
               'Tax ID/ VAT Number', 'Total Annual Sales', 'DUNS Number', 'quality certifications',
               'Please describe the "other" quality certification',
               'If certification in process, list date expected to finalize', 'Operations outside USA',
               "Do you currently supply to any OEM's?", 'OEMs',
               'Are you a current supplier to ABC Corporation or have you supplied to ABC Corporation in the past?',
               'Vendor Number',
               'Do you supply to any other Tier 1 automotive companies?', 'Do you offer Just In Time (JIT) delivery?',
               'Do you offer Consignment or Vendor Managed Inventory (VMI) ?',
               'What is the % of sales that are automotive?',
               'List any significant awards/ recognition your company has received', 'Customer Name 1', '% of Sales 1',
               'Automotive - Yes or No 1',
               'Customer Name 2', '% of Sales 2', 'Automotive - Yes or No 2', 'Customer Name 3', '% of Sales 3',
               'Automotive - Yes or No 3',
               'Please select all ABC Corporation NA locations you can effectively service *',
               'For suppliers providing production parts, please list ALL manufacturing locations',
               'What event did you meet ABC Corporation?',
               'Non Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)',
               'Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)',
               'Additional Products and Services: List any additional products and services that you can provide but could not find listed above, Separate each item with a comma (,)',

               ]

    # write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # get your data, from database or from a text file...
    # data = get_data() #dummy method to fetch data.
    # for my_row in data:
    #     row_num = row_num + 1
    #     ws.write(row_num, 0, my_row.name, font_style)
    #     ws.write(row_num, 1, my_row.start_date_time, font_style)
    #     ws.write(row_num, 2, my_row.end_date_time, font_style)
    #     ws.write(row_num, 3, my_row.notes, font_style)

    wb.save(response)
    return response


def UnmapNpm(id):
    if id == "Auxiliaries and supplies":
        return 1
    elif id == "IT and Telecommunication":
        return 2
    elif id == "IT and Telecommunication(cont.)":
        return 3
    elif id == "Production Equipment and Engineering, Buildings and Vehicles":
        return 4
    elif id == "Production Equipment and Engineering, Buildings and Vehicles (cont.)":
        return 5
    elif id == "Corporate Services and Related Supplies":
        return 6
    elif id == "Logistical Services":
        return 7
    elif id == "Logistical Services (cont.)":
        return 8


def UnmapPm(id):
    if id == "Raw Material":
        return 1
    elif id == "Casting":
        return 2
    elif id == "Non Cast Metal Parts":
        return 3
    elif id == "Miscelleanous":
        return 4
    elif id == "Plastic Parts":
        return 5
    elif id == "Rubber Parts":
        return 6
    elif id == "Electronics":
        return 7
    elif id == "Electronics (cont.)":
        return 8
    elif id == "Electro-mech Parts":
        return 9


@login_required(login_url='/login')
def UploadExcelFile(request):
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]

    try:
        excel_file = request.FILES.get('excel_file', None)
        print("excel_file", excel_file)
        data = ""
        # except MultiValueDictKeyError:
        # return redirect(<your_upload_file_failed_url>)
        if (str(excel_file).split('.')[-1] == "csv"):
            data = pd.read_csv(excel_file)

        campany_name = data['Company Name']
        website_url = data['Website URL']
        company_video_link = data["Company detail's Video link"]
        address1 = data['Address 1']
        address2 = data['Address 2']
        country = data['Country']
        city = data['City']
        state = data['State']
        zip_code = data['Postal Code']

        sales_contact_job_title = data['Sales Job Title']
        sales_contact_phone = data['Sales Office Phone']
        print("sales_contact_phone", sales_contact_phone)
        sales_contact_mobile = data['Sales Mobile Phone']
        sales_contact_first_name = data['Sales First Name']
        sales_contact_last_name = data['Sales Last Name']
        sales_contact_email = data['Sales Email Address']

        general_contact_first_name = data['General First Name']
        general_contact_last_name = data['General Last Name']
        general_contact_job_title = data['General Job Title']
        general_contact_email = data['General Email Address']
        general_contact_phone = data['General Office Phone']
        general_contact_mobile = data['General Mobile Phone']

        mbe_business = data[
            "Is your company certified by the National Minority Supplier Development Council (NMSDC) or one of it's affiliates?"]
        mbe_council = data['MOB council']
        mbe_ethnicity = data['Ethnicity']
        mbe_certificationDescription = data['MOB Certification Description']
        mbe_expirationDate = data['MOB Expiration Date']

        wbe_business = data[
            "Is your company certified by the Women's Business Enterprise National Council Development Council (WBENC) or one of it's affiliates? *"]
        wbe_council = data['WOB council']
        wbe_certificationDescription = data['WOB Certification Description']
        wbe_expirationDate = data['WOB Expiration Date']

        vb_business = data["Is your company a veteran-owned business"]
        print("vb_business", vb_business[0])
        vb_council = data['VOB council']
        vb_certificationDescription = data['VOB Certification Description']
        vb_expirationDate = data['VOB Expiration Date']

        other_certification_business = data["Is your company certified by another organization?"]
        other_certification_council = data['OC council']
        other_certification_certificationDescription = data['OC Certification Description']
        other_certification_expirationDate = data['OC Expiration Date']

        presentationDescription = data['Description']
        numberOfEmployees = data['Number of Employees']
        taxIdVatNumber = data['Tax ID/ VAT Number']
        totalAnnaulSales = data['Total Annual Sales']
        DunsNumber = data['DUNS Number']
        qualityCertification = data['quality certifications']
        certificationExpectedDate = data['If certification in process, list date expected to finalize']
        operationOutsideUsa = data['Operations outside USA']

        isOem = data["Do you currently supply to any OEM's?"]
        oEMS = data['OEMs']
        AbcSupplier = data[
            'Are you a current supplier to ABC Corporation or have you supplied to ABC Corporation in the past?']
        vendorNumber = data['Vendor Number']
        anyOtherTier1AutomotiveCompany = data['Do you supply to any other Tier 1 automotive companies?']
        VMI = data['Do you offer Consignment or Vendor Managed Inventory (VMI) ?']
        JIT = data['Do you offer Just In Time (JIT) delivery?']
        percentageSale = data['What is the % of sales that are automotive?']
        significantAwards = data['List any significant awards/ recognition your company has received']
        customerName1 = data['Customer Name 1']
        sales1 = data['% of Sales 1']
        automotive1 = data['Automotive - Yes or No 1']
        customerName2 = data['Customer Name 2']
        sales2 = data['% of Sales 2']
        automotive2 = data['Automotive - Yes or No 2']
        customerName3 = data['Customer Name 3']
        sales3 = data['% of Sales 3']
        automotive3 = data['Automotive - Yes or No 3']
        naLocation = data['Please select all ABC Corporation NA locations you can effectively service *']
        manufacturingLocations = data[
            'For suppliers providing production parts, please list ALL manufacturing locations']
        event = data['What event did you meet ABC Corporation?']

        npmValue = data[
            'Non Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)']

        pmValue = data[
            'Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)']

        additoinalProductAndServices = data[
            'Additional Products and Services: List any additional products and services that you can provide but could not find listed above, Separate each item with a comma (,)']

        for index in range(0, len(campany_name)):
            salesContact = SalesContact()
            if sales_contact_first_name[index]:
                salesContact.first_name = sales_contact_first_name[index]
            if sales_contact_last_name[index]:
                salesContact.last_name = sales_contact_last_name[index]
            if sales_contact_email[index]:
                salesContact.email = sales_contact_email[index]
            if sales_contact_job_title[index]:
                salesContact.job_title = sales_contact_job_title[index]
            print("sales_contact_phone[index]", sales_contact_phone[index])
            if sales_contact_phone[index]:
                salesContact.phone_number = sales_contact_phone[index].astype('int64')
            print("sales_contact_mobile[index]", sales_contact_mobile[index])
            if sales_contact_mobile[index]:
                salesContact.mobile_number = sales_contact_mobile[index].astype('int64')
            salesContact.save()

            generalContact = GeneralContact()
            if general_contact_first_name[index]:
                generalContact.first_name = general_contact_first_name[index]
            if general_contact_last_name[index]:
                generalContact.last_name = general_contact_last_name[index]
            if general_contact_email[index]:
                generalContact.email = general_contact_email[index]
            if general_contact_job_title[index]:
                generalContact.job_title = general_contact_job_title[index]
            if general_contact_phone[index]:
                generalContact.phone_number = general_contact_phone[index].astype('int64')
            if general_contact_mobile[index]:
                generalContact.mobile_number = general_contact_mobile[index].astype('int64')
            generalContact.save()
            generalContact = GeneralContact.objects.filter(email=general_contact_email[index]).first()

            tempCountry = Country.objects.filter(country_name=country[index]).first()

            generalContactInfo = GeneralContactInfo()
            generalContactInfo.company_name = campany_name[index]
            generalContactInfo.website_url = website_url[index]
            generalContactInfo.video_url = company_video_link[index]
            generalContactInfo.address1 = address1[index]
            generalContactInfo.address2 = address2[index]
            generalContactInfo.country = tempCountry
            generalContactInfo.city = city[index]
            generalContactInfo.state = state[index]
            generalContactInfo.zip_code = zip_code[index]
            generalContactInfo.sales_contact = salesContact
            generalContactInfo.general_contact = generalContact
            generalContactInfo.save()

            businessAndCertification = BusinessAndCertification()
            businessAndCertification.business = mbe_business[index]
            businessAndCertification.council = mbe_council[index]
            businessAndCertification.ethnicity = mbe_ethnicity[index]
            businessAndCertification.certification_description = mbe_certificationDescription[index]
            if mbe_expirationDate[index]:
                temp_date = str(mbe_expirationDate[index]).split('/')
                mbe_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
                businessAndCertification.expiration_date = mbe_expirationDate[index]
                print("mbe_expirationDate[index]", mbe_expirationDate[index])
            businessAndCertification.save()

            womenOwnedBusiness = WomenOwnedBusiness()
            womenOwnedBusiness.business = wbe_business[index]
            womenOwnedBusiness.council = wbe_council[index]
            # womenOwnedBusiness.ethnicity = wbe_ethnicity
            womenOwnedBusiness.certification_file = ''
            womenOwnedBusiness.certification_description = wbe_certificationDescription[index]
            if wbe_expirationDate[index]:
                temp_date = str(wbe_expirationDate[index]).split('/')
                wbe_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
                womenOwnedBusiness.expiration_date = wbe_expirationDate[index]
            womenOwnedBusiness.save()

            veteranOwnedBusiness = VeteranOwnedBusiness()
            print("vb_business[index]", vb_business[index])
            veteranOwnedBusiness.business = vb_business[index]
            veteranOwnedBusiness.council = vb_council[index]
            # veteranOwnedBusiness.ethnicity = vb_ethnicity
            veteranOwnedBusiness.certification_file = ''
            veteranOwnedBusiness.certification_description = vb_certificationDescription[index]
            if vb_expirationDate[index]:
                temp_date = str(vb_expirationDate[index]).split('/')
                vb_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
                veteranOwnedBusiness.expiration_date = vb_expirationDate[index]
            veteranOwnedBusiness.save()

            otherCertification = OtherCertification()
            otherCertification.business = other_certification_business[index]
            otherCertification.council = other_certification_council[index]
            # otherCertification.ethnicity = other_certification_ethnicity
            otherCertification.certification_file = ''
            otherCertification.certification_description = other_certification_certificationDescription[index]
            if other_certification_expirationDate[index]:
                temp_date = str(other_certification_expirationDate[index]).split('/')
                other_certification_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]),
                                                                          int(temp_date[0]))
                otherCertification.expiration_date = other_certification_expirationDate[index]
            otherCertification.save()

            diverseCertification = DiverseCertification()
            diverseCertification.minority_owned_business = businessAndCertification
            diverseCertification.women_owned_business = womenOwnedBusiness
            diverseCertification.other_certification = otherCertification
            diverseCertification.veteran_owned_business = veteranOwnedBusiness
            diverseCertification.save()

            companyDetails = CompanyDetails()
            companyDetails.presentation_file = ''
            companyDetails.presentation_description = presentationDescription[index]
            companyDetails.number_of_employees = numberOfEmployees[index]
            companyDetails.tax_id_vat_number = taxIdVatNumber[index]
            companyDetails.total_annaul_sales = totalAnnaulSales[index]
            companyDetails.duns_number = DunsNumber[index]
            companyDetails.quality_certification = qualityCertification[index]
            if certificationExpectedDate[index]:
                temp_date = str(certificationExpectedDate[index]).split('/')
                certificationExpectedDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]),
                                                                 int(temp_date[0]))
                companyDetails.certification_expected_date = certificationExpectedDate[index]
            companyDetails.operation_outside_usa = operationOutsideUsa[index]
            companyDetails.save()

            tempNaLocation = NaLocation.objects.filter(name=naLocation[index]).first()

            productionCapabilities = ProductionCapabilities()
            if isOem[index] == 'yes' or isOem[index] == 'Yes':
                isOem[index] = True
            else:
                isOem[index] = False
            if AbcSupplier[index] == 'yes' or AbcSupplier[index] == 'Yes':
                AbcSupplier[index] = True
            else:
                isOem[index] = False
            if VMI[index] == 'yes' or VMI[index] == 'Yes':
                VMI[index] = True
            else:
                VMI[index] = False
            if JIT[index] == 'yes' or JIT[index] == 'Yes':
                JIT[index] = True
            else:
                JIT[index] = False
            if automotive1[index] == 'yes' or automotive1[index] == 'Yes':
                automotive1[index] = True
            else:
                automotive1[index] = False
            if automotive2[index] == 'yes' or automotive2[index] == 'Yes':
                automotive2[index] = True
            else:
                automotive2[index] = False
            if automotive3[index] == 'yes' or automotive3[index] == 'Yes':
                automotive3[index] = True
            else:
                automotive3[index] = False
            if anyOtherTier1AutomotiveCompany[index] == 'yes' or anyOtherTier1AutomotiveCompany[index] == 'Yes':
                anyOtherTier1AutomotiveCompany[index] = True
            else:
                anyOtherTier1AutomotiveCompany[index] = False
            # print(isOem, AbcSupplier, VMI, JIT, automotive1, automotive2, automotive3)
            productionCapabilities.isOem = isOem[index]
            tempOEMS = OEMS.objects.filter(name=oEMS[index]).first()
            productionCapabilities.oems = tempOEMS
            productionCapabilities.abc_supplier = AbcSupplier[index]
            if vendorNumber[index]:
                productionCapabilities.vendor_number = vendorNumber[index]
            productionCapabilities.any_other_tier1_automotive_company = anyOtherTier1AutomotiveCompany[index]
            productionCapabilities.nmi = VMI[index]
            productionCapabilities.jit = JIT[index]
            if percentageSale[index]:
                productionCapabilities.percentage_sale = percentageSale[index]
            productionCapabilities.significant_awards = significantAwards[index]
            productionCapabilities.customer_name1 = customerName1[index]
            productionCapabilities.sales1 = sales1[index]
            productionCapabilities.automotive1 = automotive1[index]
            productionCapabilities.customer_name2 = customerName2[index]
            productionCapabilities.sales2 = sales2[index]
            productionCapabilities.automotive2 = automotive2[index]
            productionCapabilities.customer_name3 = customerName3[index]
            productionCapabilities.sales3 = sales3[index]
            productionCapabilities.automotive3 = automotive3[index]
            productionCapabilities.record_per_naLocation = tempNaLocation
            productionCapabilities.manufacturing_locations = manufacturingLocations[index]
            productionCapabilities.event = event[index]
            productionCapabilities.save()

            aBCCorporation = ABCCorporation()
            aBCCorporation.general_contant_info = generalContactInfo
            aBCCorporation.diverse_certification = diverseCertification
            aBCCorporation.company_details = companyDetails
            aBCCorporation.production_capabilities = productionCapabilities

            aBCCorporation.save()

            if npmValue[index]:
                npmSelectedValueFinal = npmValue[index].split(',')
                for obj in npmSelectedValueFinal:
                    temp = str(obj).split('>')
                    tempNpmValue = temp[0]
                    npmValueCategory1 = temp[1]
                    if temp[2]:
                        npmValueCategory2 = temp[2]
                    else:
                        npmValueCategory2 = ''
                    npmValues = NpmValues(abc_corporation_id=aBCCorporation.id, npm_value=tempNpmValue,
                                          npm_value_category1=npmValueCategory1, npm_value_category2=npmValueCategory2)
                    npmValues.save()

            if pmValue[index]:
                pmSelectedValueFinal = pmValue[index].split(',')
                for obj in pmSelectedValueFinal:
                    temp = str(obj).split('>')
                    tempPmValue = temp[0]
                    if temp[1]:
                        pmValueCategory1 = temp[1]
                    else:
                        pmValueCategory1 = ''
                    pmValues = PmValues(abc_corporation_id=aBCCorporation.id, pm_value=tempPmValue,
                                        pm_value_category1=pmValueCategory1)
                    pmValues.save()

            messages.success(request, 'Data successfully uploaded')
    except:
        messages.error(request, 'Error while uploading data')
        print("No")

    return render(request, 'bulk.html')


def send_mail_to_client(email, review, customDescription):
    subject = 'New Application at ABC Supplier'

    if customDescription:
        message = customDescription
    else:
        message = f'Your application is {review}'

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)


@login_required(login_url='/login')
def SendResponseToSubmitter(request):
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]
    ApplicationId = request.POST.get('ApplicationId', None)
    try:

        application = ABCCorporation.objects.filter(id=ApplicationId).first()

        general_contact_email = application.general_contant_info.general_contact.email

        review = request.POST.get('review', None)

        customDescription = request.POST.get('customDescription', None)

        send_mail_to_client(general_contact_email, review, customDescription)

        country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
        context = {
            'application': application,
            'country': mapCountryName(country.country_name)
        }
        application.response = 1
        application.save()
        messages.success(request, 'The Response Has Been Sent Successfully To: ' + general_contact_email)
        return render(request, 'detailRecord.html', context)
    except:
        application = ABCCorporation.objects.filter(id=ApplicationId).first()
        country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
        general_contact_email = application.general_contant_info.general_contact.email
        context = {
            'application': application,
            'country': mapCountryName(country.country_name)
        }
        messages.error(request, 'Error While Sending Reponse To: ' + general_contact_email)
        return render(request, 'detailRecord.html', context)


@login_required(login_url='/login')
def SendResponseToSomeone(request, id):
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]
    email_address = request.POST.get('email', None)
    if request.method == 'POST':
        try:

            application_id = id

            messageType = request.POST.get('messageType', None)

            if messageType == 'Default Message':
                content = "A Harold Construction Inc company has registered on the ABC supplier diversity portal. You are receiving this note because this supplier may be of interest to you. Please review the supplier information by clicking on the following link. Afterwards please let us know if you plan any further actions by submitting your feedback below the application."
            else:
                customDescription = request.POST.get('customDescription', None)
                content = customDescription

            report_link = settings.APPLICATION_BASE_URL + "report/" + str(application_id) + "/" + email_address
            html_content = render_to_string("report_email_template.html",
                                            {'content': content, 'report_link': report_link})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "New Application at ABC Supplier",
                text_content,
                settings.EMAIL_HOST_USER,
                [email_address]
            )

            email.attach_alternative(html_content, "text/html")
            email.send()

            application = ABCCorporation.objects.filter(id=id).first()

            country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
            context = {
                'application': application,
                'country': mapCountryName(country.country_name)
            }
            application.emailed = application.emailed + 1
            application.save()
            messages.success(request, 'The Report Has Been Sent Successfully To: ' + email_address)
            return render(request, 'detailRecord.html', context)

        except:

            messages.error(request, 'Error while sending report to: ' + email_address)
            application = ABCCorporation.objects.filter(id=id).first()

            country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
            context = {
                'application': application,
                'country': mapCountryName(country.country_name)
            }
            return render(request, 'detailRecord.html', context)
    else:
        application = ABCCorporation.objects.filter(id=id).first()

        country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
        context = {
            'application': application,
            'country': mapCountryName(country.country_name)
        }
        return render(request, 'detailRecord.html', context)


def GetEmailResponse(request):
    try:

        import email
        import imaplib

        EMAIL = 'faizanaslam455@gmail.com'
        PASSWORD = 'enooetksxehjrjts'

        imap_host = 'imap.gmail.com'

        # init imap connection
        mail = imaplib.IMAP4_SSL(imap_host, 993)
        rc, resp = mail.login(EMAIL, PASSWORD)

        # select only unread messages from inbox
        mail.select('Inbox')
        status, data = mail.search(None, '(FROM "mf591108@gmail.com" SUBJECT "abc")')

        # for each e-mail messages, print text content
        for num in data[0].split():
            # get a single message and parse it by policy.SMTP (RFC compliant)
            status, data = mail.fetch(num, '(RFC822)')
            email_msg = data[0][1]
            email_msg = email.message_from_bytes(email_msg, policy=policy.SMTP)

            print("\n----- MESSAGE START -----\n")

            print("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n" % ( \
                str(email_msg['From']), \
                str(email_msg['To']), \
                str(email_msg['Date']), \
                str(email_msg['Subject'])))

            # print only message parts that contain text data
            for part in email_msg.walk():
                if part.get_content_type() == "text/plain":
                    for line in part.get_content().splitlines():
                        print(line)

            print("\n----- MESSAGE END -----\n")
        return JsonResponse({'data': "Response successfully sent.", 'status': 200})
    except:
        return JsonResponse({'data': "Error while sending response.", 'status': 400})


def Report(request, id, email_address):
    application = ABCCorporation.objects.filter(id=id).first()

    country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
    context = {
        'application': application,
        'country': mapCountryName(country.country_name),
        'email_address': email_address
    }
    return render(request, 'report.html', context)


def SendFeedback(request):
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]
    email_address = request.POST['email_address']

    feedbackDescription = request.POST.get('feedbackDescription', None)

    ApplicationIdFeedback = request.POST.get('ApplicationIdFeedback', None)

    if request.method == 'POST':

        try:

            application = ABCCorporation.objects.filter(id=ApplicationIdFeedback).first()

            country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
            context = {
                'application': application,
                'country': mapCountryName(country.country_name),
                'email_address': email_address
            }

            feedback = Feedback(email=email_address, feedback=feedbackDescription, application_id=ApplicationIdFeedback)
            feedback.save()

            messages.success(request,
                             'The Feedback Has Been Sumitted Successfully. Thank You For Providing Your Feedback.')
            return render(request, 'Report.html', context)
        except:
            application = ABCCorporation.objects.filter(id=ApplicationIdFeedback).first()

            country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
            context = {
                'application': application,
                'country': mapCountryName(country.country_name),
                'email_address': email_address
            }
            messages.error(request, 'Error while sending the feedback.')
            return render(request, 'report.html', context)
    else:
        application = ABCCorporation.objects.filter(id=ApplicationIdFeedback).first()

        country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
        context = {
            'application': application,
            'country': mapCountryName(country.country_name),
            'email_address': email_address
        }
        return render(request, 'report.html', context)


def GetFeedbacks(request):
    application_id = request.POST['ApplicationIdForGetFeedbacks']

    try:

        result = []
        status = 400

        print("application_id", application_id)

        all_feedbacks = Feedback.objects.filter(application_id=application_id)
        if all_feedbacks:
            for obj in all_feedbacks:
                temp = []
                temp.append(obj.email)
                temp.append(obj.feedback)
                temp.append(obj.feedback_date)
                temp.append(obj.update_date)
                result.append(temp)
            status = 200

        print("temp", result)
        return JsonResponse({'data': "Perfect", 'status': status, "result": result})
    except:

        print("application_id", application_id)
        return JsonResponse({'data': "Error", 'status': 400})


def favouriteRecode(request):
    # upload()
    return render(request, 'favourite-list.html')

def removeNote(request, id):

    Notes.objects.filter(id=id).delete()
    resp = {
        'id': id,
        'status': 200

    }
    return JsonResponse(resp)

def addNote(request):
    noteText = request.POST.get('noteText', None)
    ApplicationId = request.POST.get('ApplicationId', None)

    note = Notes(application_id=ApplicationId,feedback=noteText, user_id=request.user.id)
    note.save()
    print("noteText", noteText)
    resp = {
        'id': 21,
        'note': noteText,
        'status': 200

    }
    return JsonResponse(resp)
