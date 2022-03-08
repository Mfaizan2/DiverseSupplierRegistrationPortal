import datetime

from django.shortcuts import render
from registration.models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def Registration(request):
    if request.method == 'POST':

        try:
            # General Contact Info
            print(request.POST['campany_name'])
            campany_name = "ABCTech"
            print(request.POST['website_url'])
            website_url = "abc@gmail.com"
            print(request.POST['address1'])
            address1 = "abc house 3"
            print(request.POST['address2'])
            address2 = "abc house 3"
            print(request.POST['country'])
            country = "Pakistan"
            print(request.POST['city'])
            city = "Lahore"
            print(request.POST['state'])
            state = "Punjab"
            print(request.POST['zip_code'])
            zip_code = 54000

            print(request.POST['sales_contact_first_name'])
            sales_contact_first_name = "Zeeshan"
            print(request.POST['sales_contact_last_name'])
            sales_contact_last_name = "Aslam"
            print(request.POST['sales_contact_email'])
            sales_contact_email = "Zeeshan@gmail.com"
            print(request.POST['sales_contact_job_title'])
            sales_contact_job_title = "Dev"
            print(request.POST['sales_contact_phone'])
            sales_contact_phone = "12345"
            print(request.POST['sales_contact_mobile'])
            sales_contact_mobile = "67890"

            print(request.POST['general_contact_first_name'])
            general_contact_first_name = "Zeeshan"
            print(request.POST['general_contact_last_name'])
            general_contact_last_name = "Aslam"
            print(request.POST['general_contact_email'])
            general_contact_email = "Zeeshan@gmail.com"
            print(request.POST['general_contact_job_title'])
            general_contact_job_title = "Dev"
            print(request.POST['general_contact_phone'])
            general_contact_phone = "12345"
            print(request.POST['general_contact_mobile'])
            general_contact_mobile = "67890"
            #----------------------------------

            #Diverse Certification

            print(request.POST['mbe_business'])
            mbe_business = "yes"
            print(request.POST['mbe_council'])
            mbe_council =  "abc"
            print(request.POST['mbe_ethnicity'])
            mbe_ethnicity = "xyz"
            print(request.POST['mbe_certificationDescription'])
            mbe_certificationDescription = "this is temp"
            print(request.POST['mbe_expirationDate'])
            mbe_expirationDate = datetime.date(1997, 10, 19)

            print(request.POST['wbe_business'])
            wbe_business = "yes"
            print(request.POST['wbe_council'])
            wbe_council =  "abc"
            # print(request.POST['wbe_ethnicity'])
            # wbe_ethnicity = "xyz"
            print(request.POST['wbe_certificationDescription'])
            wbe_certificationDescription = "this is temp"
            print(request.POST['wbe_expirationDate'])
            wbe_expirationDate = datetime.date(1997, 10, 19)

            print(request.POST['vb_business'])
            vb_business = "yes"
            print(request.POST['vb_council'])
            vb_council =  "abc"
            # print(request.POST['vb_ethnicity'])
            # vb_ethnicity = "xyz"
            print(request.POST['vb_certificationDescription'])
            vb_certificationDescription = "this is temp"
            print(request.POST['vb_expirationDate'])
            vb_expirationDate = datetime.date(1997, 10, 19)

            print(request.POST['other_certification_business'])
            other_certification_business = "yes"
            print(request.POST['other_certification_council'])
            other_certification_council =  "abc"
            # print(request.POST['other_certification_ethnicity'])
            # other_certification_ethnicity = "xyz"
            print(request.POST['other_certification_certificationDescription'])
            other_certification_certificationDescription = "this is temp"
            print(request.POST['other_certification_expirationDate'])
            other_certification_expirationDate = datetime.date(1997, 10, 19)
            #--------------------------------------

            #Company Details

            print(request.POST['presentationDescription'])
            presentationDescription = "the temp"
            print(request.POST['numberOfEmployees'])
            numberOfEmployees = 12
            print(request.POST['taxIdVatNumber'])
            taxIdVatNumber =  "343B"
            print(request.POST['totalAnnaulSales'])
            totalAnnaulSales = "less than $1M"
            print(request.POST['DunsNumber'])
            DunsNumber =  "123KM"
            print(request.POST['qualityCertification'])
            qualityCertification = "Many"
            print(request.POST['certificationExpectedDate'])
            certificationExpectedDate = datetime.date(1997, 10, 19)
            print(request.POST['operationOutsideUsa'])
            operationOutsideUsa = "Maxcio"

            #--------------------------------------

            #Production Capability
            print(request.POST['isOem'])
            isOem = True
            print(request.POST['oEMS'])
            oEMS = OEMS.objects.filter(name="BMW").first()
            print(request.POST['JIT'])
            JIT = True
            print(request.POST['AbcSupplier'])
            AbcSupplier = True
            print(request.POST['vendorNumber'])
            vendorNumber = 123312
            print(request.POST['anyOtherTier1AutomotiveCompany'])
            anyOtherTier1AutomotiveCompany = True
            print(request.POST['VMI'])
            VMI = True
            print(request.POST['percentageSale'])
            percentageSale = 20
            print(request.POST['significantAwards'])
            significantAwards = "Many more to come"
            print(request.POST['customerName1'])
            customerName1 = "Qasim"
            print(request.POST['sales1'])
            sales1 = 233
            print(request.POST['automotive1'])
            automotive1 = True
            print(request.POST['customerName2'])
            customerName2 = "Ahmed"
            print(request.POST['sales2'])
            sales2 = 3333
            print(request.POST['automotive2'])
            automotive2 = True
            print(request.POST['customerName3'])
            customerName3 = "hassan"
            print(request.POST['sales3'])
            sales3 = 2222
            print(request.POST['automotive3'])
            automotive3 = False
            print(request.POST['recordPerNaLocation'])
            recordPerNaLocation = "MX"
            print(request.POST['manufacturingLocations'])
            manufacturingLocations = "FSD"
            print(request.POST['event'])
            event = "FCA"

            #-----------------------------------------------

            # Production and services
            print(request.POST['npmValue'])
            npmValue = "AUXILIARIES"
            print(request.POST['npmValueCategory1'])
            npmValueCategory1 = "MRO"
            print(request.POST['npmValueCategory2'])
            npmValueCategory2 = "HYDROLIC"

            print(request.POST['pmValue'])
            pmValue = "RAW MATERIAL"
            print(request.POST['pmValueCategory1'])
            pmValueCategory1 = "BAE METAL"
            print(request.POST['pmValueCategory2'])
            pmValueCategory2 = "bnnnn"
            print(request.POST['additoinalProductAndServices'])
            additoinalProductAndServices = "ABC, CDB, NMN"

            #------------------------------------------------


            # salesContact = SalesContact()
            # salesContact.firstName = sales_contact_first_name
            # salesContact.lastName = sales_contact_last_name
            # salesContact.email = sales_contact_email
            # salesContact.jobTitle = sales_contact_job_title
            # salesContact.phoneNumber = sales_contact_phone
            # salesContact.MobileNumber = sales_contact_mobile
            # salesContact.save()
            #
            # generalContact = GeneralContact()
            # generalContact.firstName = general_contact_first_name
            # generalContact.lastName = general_contact_last_name
            # generalContact.email = general_contact_email
            # generalContact.jobTitle = general_contact_job_title
            # generalContact.phoneNumber = general_contact_phone
            # generalContact.MobileNumber = general_contact_mobile
            # generalContact.save()
            # generalContact = GeneralContact.objects.filter(email=general_contact_email).first()
            #
            # country = Country.objects.filter(countryName=country).first()
            # print("country", country)
            # print("generalContact", generalContact)
            #
            # generalContactInfo = GeneralContactInfo()
            # generalContactInfo.companyName = campany_name
            # generalContactInfo.websiteUrl = website_url
            # generalContactInfo.address1 = address1
            # generalContactInfo.address2 = address2
            # generalContactInfo.country = country
            # generalContactInfo.city = city
            # generalContactInfo.state = state
            # generalContactInfo.zipCode = zip_code
            # generalContactInfo.SalesContact = salesContact
            # generalContactInfo.GeneralContact = generalContact
            # generalContactInfo.save()
            #
            #
            # businessAndCertification = BusinessAndCertification()
            # businessAndCertification.Business = mbe_business
            # businessAndCertification.council =  mbe_council
            # businessAndCertification.ethnicity = mbe_ethnicity
            # businessAndCertification.certificationDescription = mbe_certificationDescription
            # businessAndCertification.expirationDate = mbe_expirationDate
            # businessAndCertification.save()
            #
            # womenOwnedBusiness = WomenOwnedBusiness()
            # womenOwnedBusiness.Business = wbe_business
            # womenOwnedBusiness.council =  wbe_council
            # womenOwnedBusiness.ethnicity = wbe_ethnicity
            # womenOwnedBusiness.certificationDescription = wbe_certificationDescription
            # womenOwnedBusiness.expirationDate = wbe_expirationDate
            # womenOwnedBusiness.save()
            #
            # veteranOwnedBusiness = VeteranOwnedBusiness()
            # veteranOwnedBusiness.Business = vb_business
            # veteranOwnedBusiness.council =  vb_council
            # veteranOwnedBusiness.ethnicity = vb_ethnicity
            # veteranOwnedBusiness.certificationDescription = vb_certificationDescription
            # veteranOwnedBusiness.expirationDate = vb_expirationDate
            # veteranOwnedBusiness.save()
            #
            # otherCertification = OtherCertification()
            # otherCertification.Business = other_certification_business
            # otherCertification.council =  other_certification_council
            # otherCertification.ethnicity = other_certification_ethnicity
            # otherCertification.certificationDescription = other_certification_certificationDescription
            # otherCertification.expirationDate = other_certification_expirationDate
            # otherCertification.save()
            #
            # diverseCertification = DiverseCertification()
            # diverseCertification.MinorityOwnedBusiness = businessAndCertification
            # diverseCertification.WomenOwnedBusiness = womenOwnedBusiness
            # diverseCertification.OtherCertification = otherCertification
            # diverseCertification.VeteranOwnedBusiness = veteranOwnedBusiness
            # diverseCertification.save()
            #
            # companyDetails = CompanyDetails()
            # companyDetails.presentationDescription = presentationDescription
            # companyDetails.numberOfEmployees = numberOfEmployees
            # companyDetails.taxIdVatNumber =  taxIdVatNumber
            # companyDetails.totalAnnaulSales = totalAnnaulSales
            # companyDetails.DunsNumber =  DunsNumber
            # companyDetails.qualityCertification = qualityCertification
            # companyDetails.certificationExpectedDate = certificationExpectedDate
            # companyDetails.operationOutsideUsa = operationOutsideUsa
            # companyDetails.save()
            #
            # naLocation = NaLocation.objects.filter(name=recordPerNaLocation).first()
            #
            # productionCapabilities = ProductionCapabilities()
            # productionCapabilities.isOem = isOem
            # productionCapabilities.OEMS = oEMS
            # productionCapabilities.AbcSupplier = AbcSupplier
            # productionCapabilities.vendorNumber = vendorNumber
            # productionCapabilities.anyOtherTier1AutomotiveCompany = anyOtherTier1AutomotiveCompany
            # productionCapabilities.VMI = VMI
            # productionCapabilities.percentageSale = percentageSale
            # productionCapabilities.significantAwards = significantAwards
            # productionCapabilities.customerName1 = customerName1
            # productionCapabilities.sales1 = sales1
            # productionCapabilities.automotive1 = automotive1
            # productionCapabilities.customerName2 = customerName2
            # productionCapabilities.sales2 = sales2
            # productionCapabilities.automotive2 = automotive2
            # productionCapabilities.customerName3 = customerName3
            # productionCapabilities.sales3 = sales3
            # productionCapabilities.automotive3 = automotive3
            # productionCapabilities.recordPerNaLocation = naLocation
            # productionCapabilities.manufacturingLocations = manufacturingLocations
            # productionCapabilities.event = event
            # productionCapabilities.save()
            #
            # productAndService = ProductAndService()
            # productAndService.npmValue = npmValue
            # productAndService.npmValueCategory1 = npmValueCategory1
            # productAndService.npmValueCategory2 = npmValueCategory2
            # productAndService.save()
            #
            # productAndService.pmValue = pmValue
            # productAndService.pmValueCategory1 = pmValueCategory1
            # productAndService.pmValueCategory2 = pmValueCategory2
            # productAndService.additoinalProductAndServices = additoinalProductAndServices
            # productAndService.save()
            #
            # aBCCorporation = ABCCorporation()
            # aBCCorporation.generalContantInfo = generalContactInfo
            # aBCCorporation.diverseCertification = diverseCertification
            # aBCCorporation.companyDetails = companyDetails
            # aBCCorporation.productionCapabilities = productionCapabilities
            # aBCCorporation.productAndService = productAndService
            # aBCCorporation.save()
            messages.success(request, 'Application successfully submitted')
            return render(request, 'Registrationform.html')
        except Exception as e:
            messages.error(request, e)
            print(e)



    return render(request, 'Registrationform.html')


def AllRecords(request):
    all_applications = ABCCorporation.objects.all()
    paginator = Paginator(all_applications, 10)
    page_number = 1 #request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    print("all_applications", page_obj)
    for rec in page_obj:
        print(rec.productAndService.npmValue)
    context = {
        'expenses': all_applications,
        'page_obj': page_obj
    }
    return render(request, 'allRecords.html', context)
