import datetime

from django.shortcuts import render
from registration.models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def Registration(request):
    if request.method == 'POST':

        # try:
        # General Contact Info
        # print(request.POST['campany_name'])
        campany_name = request.POST['campany_name']
        # print(request.POST['website_url'])
        website_url = request.POST['website_url']
        # print(request.POST['address1'])
        address1 = request.POST['address1']
        # print(request.POST['address2'])
        address2 = request.POST['address2']
        # print(request.POST['country'])
        country = request.POST['country']
        # print(request.POST['city'])
        city = request.POST['city']
        # print(request.POST['state'])
        state = request.POST['state']
        # print(request.POST['zip_code'])
        zip_code = request.POST['zip_code']

        # print(request.POST['sales_contact_first_name'])
        sales_contact_first_name = request.POST['sales_contact_first_name']
        # print(request.POST['sales_contact_last_name'])
        sales_contact_last_name = request.POST['sales_contact_last_name']
        # print(request.POST['sales_contact_email'])
        sales_contact_email = request.POST['sales_contact_email']
        # print(request.POST['sales_contact_job_title'])
        sales_contact_job_title = request.POST['sales_contact_job_title']
        # print(request.POST['sales_contact_phone'])
        sales_contact_phone = request.POST['sales_contact_phone']
        # print(request.POST['sales_contact_mobile'])
        sales_contact_mobile = request.POST['sales_contact_mobile']

        # print(request.POST['general_contact_first_name'])
        general_contact_first_name = request.POST['general_contact_first_name']
        # print(request.POST['general_contact_last_name'])
        general_contact_last_name = request.POST['general_contact_last_name']
        # print(request.POST['general_contact_email'])
        general_contact_email = request.POST['general_contact_email']
        # print(request.POST['general_contact_job_title'])
        general_contact_job_title = request.POST['general_contact_job_title']
        # print(request.POST['general_contact_phone'])
        general_contact_phone = request.POST['general_contact_phone']
        # print(request.POST['general_contact_mobile'])
        general_contact_mobile = request.POST['general_contact_mobile']
        #----------------------------------

        #Diverse Certification

        # print(request.POST['mbe_business'])
        mbe_business = request.POST['mbe_business']
        # print(request.POST['mbe_council'])
        mbe_council =  request.POST['mbe_council']
        # print(request.POST['mbe_ethnicity'])
        mbe_ethnicity = request.POST['mbe_ethnicity']
        # print(request.POST['mbe_certificationDescription'])
        mbe_certificationDescription = request.POST['mbe_certificationDescription']
        # print(request.POST['mbe_expirationDate'])
        mbe_expirationDate = str(request.POST['mbe_expirationDate']).split('-')
        mbe_expirationDate = datetime.date(int(mbe_expirationDate[0]), int(mbe_expirationDate[1]), int(mbe_expirationDate[2]))

        # print(request.POST['wbe_business'])
        wbe_business = request.POST['wbe_business']
        # print(request.POST['wbe_council'])
        wbe_council =  request.POST['wbe_council']
        # print(request.POST['wbe_ethnicity'])
        # wbe_ethnicity = "xyz"
        # print(request.POST['wbe_certificationDescription'])
        wbe_certificationDescription = request.POST['wbe_certificationDescription']
        # print(request.POST['wbe_expirationDate'])
        wbe_expirationDate = str((request.POST['wbe_expirationDate'])).split('-')
        wbe_expirationDate = datetime.date(int(wbe_expirationDate[0]), int(wbe_expirationDate[1]), int(wbe_expirationDate[2]))

        # print(request.POST['vb_business'])
        vb_business = request.POST['vb_business']
        # print(request.POST['vb_council'])
        vb_council = request.POST['vb_council']
        # print(request.POST['vb_ethnicity'])
        # vb_ethnicity = "xyz"
        # print(request.POST['vb_certificationDescription'])
        vb_certificationDescription = request.POST['vb_certificationDescription']

        vb_expirationDate = str(request.POST['vb_expirationDate']).split('-')
        print(int(vb_expirationDate[0]),int(vb_expirationDate[1]),int(vb_expirationDate[2]), "faizan")
        vb_expirationDate = datetime.date(int(vb_expirationDate[0]), int(vb_expirationDate[1]), int(vb_expirationDate[2]))

        # print(request.POST['other_certification_business'])
        other_certification_business = request.POST['other_certification_business']
        # print(request.POST['other_certification_council'])
        other_certification_council =  request.POST['other_certification_council']
        # print(request.POST['other_certification_ethnicity'])
        # other_certification_ethnicity = "xyz"
        # print(request.POST['other_certification_certificationDescription'])
        other_certification_certificationDescription = request.POST['other_certification_certificationDescription']
        # print(request.POST['other_certification_expirationDate'])
        other_certification_expirationDate = str(request.POST['other_certification_expirationDate']).split('-')
        other_certification_expirationDate = datetime.date(int(other_certification_expirationDate[0]), int(other_certification_expirationDate[1]), int(other_certification_expirationDate[2]))
        #--------------------------------------

        #Company Details

        # print(request.POST['presentationDescription'])
        presentationDescription = request.POST['presentationDescription']
        # print(request.POST['numberOfEmployees'])
        numberOfEmployees = request.POST['numberOfEmployees']
        # print(request.POST['taxIdVatNumber'])
        taxIdVatNumber =  request.POST['taxIdVatNumber']
        # print(request.POST['totalAnnaulSales'])
        totalAnnaulSales = request.POST['totalAnnaulSales']
        # print(request.POST['DunsNumber'])
        DunsNumber =  request.POST['DunsNumber']
        # print(request.POST['qualityCertification'])
        qualityCertification = request.POST['qualityCertification']
        # print(request.POST['certificationExpectedDate'])
        certificationExpectedDate = str(request.POST['certificationExpectedDate']).split('-')
        certificationExpectedDate = datetime.date(int(certificationExpectedDate[0]), int(certificationExpectedDate[1]), int(certificationExpectedDate[2]))
        # print(request.POST['operationOutsideUsa'])
        operationOutsideUsa = request.POST['operationOutsideUsa']

        #--------------------------------------

        #Production Capability
        # print(request.POST['isOem'])
        isOem = request.POST.get('isOem', False)
        # print(request.POST['oEMS'])
        oEMS = request.POST['oEMS']
        oEMS = OEMS.objects.filter(name=oEMS).first()
        # print(request.POST['JIT'])
        JIT = request.POST.get('JIT', False)
        # print(request.POST['AbcSupplier'])
        AbcSupplier = request.POST.get('AbcSupplier', False)
        # print(request.POST['vendorNumber'])
        vendorNumber = int(request.POST['vendorNumber'])
        # print(request.POST['anyOtherTier1AutomotiveCompany'])
        anyOtherTier1AutomotiveCompany = request.POST.get('anyOtherTier1AutomotiveCompany', False)
        # print(request.POST['vmi'])
        VMI = request.POST.get('vmi', False)
        # print(request.POST['percentageSale'])
        percentageSale = int(request.POST['percentageSale'])
        print(request.POST['significantAwards'])
        significantAwards = request.POST['significantAwards']
        # print(request.POST['customerName1'])
        customerName1 = request.POST['customerName1']
        # print(request.POST['sales1'])
        sales1 = int(request.POST['sales1'])
        # print(request.POST['automotive1'])
        automotive1 = request.POST.get('automotive1', False)
        # print(request.POST['customerName2'])
        customerName2 = request.POST['customerName2']
        # print(request.POST['sales2'])
        sales2 = int(request.POST['sales2'])
        # print(request.POST['automotive2'])
        automotive2 = request.POST.get('automotive2', False)
        # print(request.POST['customerName3'])
        customerName3 = request.POST['customerName3']
        # print(request.POST['sales3'])
        sales3 = int(request.POST['sales3'])
        # print(request.POST['automotive3'])
        automotive3 = request.POST.get('automotive3', False)
        # print(request.POST['recordPerNaLocation'])
        recordPerNaLocation = request.POST['recordPerNaLocation']
        # print(request.POST['manufacturingLocations'])
        manufacturingLocations = request.POST['manufacturingLocations']
        # print(request.POST['event'])
        event = request.POST['event']

        #-----------------------------------------------

        # Production and services
        # print(request.POST['npmValue'])
        npmValue = request.POST['npmValue']
        # print(request.POST['npmValueCategory1'])
        npmValueCategory1 = request.POST['npmValueCategory1']
        # print(request.POST['npmValueCategory2'])
        npmValueCategory2 = request.POST['npmValueCategory2']

        # print(request.POST['pmValue'])
        pmValue = request.POST['pmValue']
        # print(request.POST['pmValueCategory1'])
        pmValueCategory1 = request.POST['pmValueCategory1']
        # print(request.POST['pmValueCategory2'])
        pmValueCategory2 = request.POST['pmValueCategory2']
        # print(request.POST['additoinalProductAndServices'])
        additoinalProductAndServices = request.POST['additoinalProductAndServices']

        #------------------------------------------------


        salesContact = SalesContact()
        salesContact.firstName = sales_contact_first_name
        salesContact.lastName = sales_contact_last_name
        salesContact.email = sales_contact_email
        salesContact.jobTitle = sales_contact_job_title
        salesContact.phoneNumber = sales_contact_phone
        salesContact.MobileNumber = sales_contact_mobile
        salesContact.save()

        generalContact = GeneralContact()
        generalContact.firstName = general_contact_first_name
        generalContact.lastName = general_contact_last_name
        generalContact.email = general_contact_email
        generalContact.jobTitle = general_contact_job_title
        generalContact.phoneNumber = general_contact_phone
        generalContact.MobileNumber = general_contact_mobile
        generalContact.save()
        generalContact = GeneralContact.objects.filter(email=general_contact_email).first()

        print("country b", country)
        country = Country.objects.filter(countryName=country).first()
        print("country", country)
        print("generalContact", generalContact)

        generalContactInfo = GeneralContactInfo()
        generalContactInfo.companyName = campany_name
        generalContactInfo.websiteUrl = website_url
        generalContactInfo.address1 = address1
        generalContactInfo.address2 = address2
        generalContactInfo.country = country
        generalContactInfo.city = city
        generalContactInfo.state = state
        generalContactInfo.zipCode = zip_code
        generalContactInfo.SalesContact = salesContact
        generalContactInfo.GeneralContact = generalContact
        generalContactInfo.save()


        businessAndCertification = BusinessAndCertification()
        businessAndCertification.Business = mbe_business
        businessAndCertification.council =  mbe_council
        businessAndCertification.ethnicity = mbe_ethnicity
        businessAndCertification.certificationDescription = mbe_certificationDescription
        businessAndCertification.expirationDate = mbe_expirationDate
        businessAndCertification.save()

        womenOwnedBusiness = WomenOwnedBusiness()
        womenOwnedBusiness.Business = wbe_business
        womenOwnedBusiness.council =  wbe_council
        # womenOwnedBusiness.ethnicity = wbe_ethnicity
        womenOwnedBusiness.certificationDescription = wbe_certificationDescription
        womenOwnedBusiness.expirationDate = wbe_expirationDate
        womenOwnedBusiness.save()

        veteranOwnedBusiness = VeteranOwnedBusiness()
        veteranOwnedBusiness.Business = vb_business
        veteranOwnedBusiness.council =  vb_council
        # veteranOwnedBusiness.ethnicity = vb_ethnicity
        veteranOwnedBusiness.certificationDescription = vb_certificationDescription
        veteranOwnedBusiness.expirationDate = vb_expirationDate
        veteranOwnedBusiness.save()

        otherCertification = OtherCertification()
        otherCertification.Business = other_certification_business
        otherCertification.council =  other_certification_council
        # otherCertification.ethnicity = other_certification_ethnicity
        otherCertification.certificationDescription = other_certification_certificationDescription
        otherCertification.expirationDate = other_certification_expirationDate
        otherCertification.save()

        diverseCertification = DiverseCertification()
        diverseCertification.MinorityOwnedBusiness = businessAndCertification
        diverseCertification.WomenOwnedBusiness = womenOwnedBusiness
        diverseCertification.OtherCertification = otherCertification
        diverseCertification.VeteranOwnedBusiness = veteranOwnedBusiness
        diverseCertification.save()

        companyDetails = CompanyDetails()
        companyDetails.presentationDescription = presentationDescription
        companyDetails.numberOfEmployees = numberOfEmployees
        companyDetails.taxIdVatNumber =  taxIdVatNumber
        companyDetails.totalAnnaulSales = totalAnnaulSales
        companyDetails.DunsNumber =  DunsNumber
        companyDetails.qualityCertification = qualityCertification
        companyDetails.certificationExpectedDate = certificationExpectedDate
        companyDetails.operationOutsideUsa = operationOutsideUsa
        companyDetails.save()

        naLocation = NaLocation.objects.filter(name=recordPerNaLocation).first()

        productionCapabilities = ProductionCapabilities()
        if isOem == 'yes':
            isOem = True
        else:
            isOem = False
        if AbcSupplier == 'yes':
            AbcSupplier = True
        else:
            isOem = False
        if VMI == 'yes':
            VMI = True
        else:
            VMI = False
        if JIT == 'yes':
            JIT = True
        else:
            JIT = False
        if automotive1 == 'yes':
            automotive1 = True
        else:
            automotive1 = False
        if automotive2 == 'yes':
            automotive2 = True
        else:
            automotive2 = False
        if automotive3 == 'yes':
            automotive3 = True
        else:
            automotive3 = False
        if anyOtherTier1AutomotiveCompany == 'yes':
            anyOtherTier1AutomotiveCompany = True
        else:
            anyOtherTier1AutomotiveCompany = False
        # print(isOem, AbcSupplier, VMI, JIT, automotive1, automotive2, automotive3)
        productionCapabilities.isOem = isOem
        productionCapabilities.OEMS = oEMS
        productionCapabilities.AbcSupplier = AbcSupplier
        productionCapabilities.vendorNumber = vendorNumber
        productionCapabilities.anyOtherTier1AutomotiveCompany = anyOtherTier1AutomotiveCompany
        productionCapabilities.VMI = VMI
        productionCapabilities.JIT = JIT
        productionCapabilities.percentageSale = percentageSale
        productionCapabilities.significantAwards = significantAwards
        productionCapabilities.customerName1 = customerName1
        productionCapabilities.sales1 = sales1
        productionCapabilities.automotive1 = automotive1
        productionCapabilities.customerName2 = customerName2
        productionCapabilities.sales2 = sales2
        productionCapabilities.automotive2 = automotive2
        productionCapabilities.customerName3 = customerName3
        productionCapabilities.sales3 = sales3
        productionCapabilities.automotive3 = automotive3
        productionCapabilities.recordPerNaLocation = naLocation
        productionCapabilities.manufacturingLocations = manufacturingLocations
        productionCapabilities.event = event
        productionCapabilities.save()

        productAndService = ProductAndService()
        productAndService.npmValue = npmValue
        productAndService.npmValueCategory1 = npmValueCategory1
        productAndService.npmValueCategory2 = npmValueCategory2
        productAndService.save()

        productAndService.pmValue = pmValue
        productAndService.pmValueCategory1 = pmValueCategory1
        productAndService.pmValueCategory2 = pmValueCategory2
        productAndService.additoinalProductAndServices = additoinalProductAndServices
        productAndService.save()

        aBCCorporation = ABCCorporation()
        aBCCorporation.generalContantInfo = generalContactInfo
        aBCCorporation.diverseCertification = diverseCertification
        aBCCorporation.companyDetails = companyDetails
        aBCCorporation.productionCapabilities = productionCapabilities
        aBCCorporation.productAndService = productAndService
        aBCCorporation.save()
        messages.success(request, 'Application successfully submitted')
        return render(request, 'Registrationform.html')
        # except Exception as e:
        #     messages.error(request, e)
        #     print(e)



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
