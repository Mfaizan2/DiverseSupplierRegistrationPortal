import datetime

from django.shortcuts import render
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

            if request.FILES['MobCertificationFile']:
                mbe_certification_file = request.FILES['MobCertificationFile']
                fss = FileSystemStorage()
                file = fss.save(mbe_certification_file.name, mbe_certification_file)
                mbe_certification_file = fss.url(file)
                print("mbe_certification_file", mbe_certification_file)
            else:
                mbe_certification_file = ''
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
            if request.FILES['WobCertificationFile']:
                wbe_certification_file = request.FILES['WobCertificationFile']
                fss = FileSystemStorage()
                file = fss.save(wbe_certification_file.name, wbe_certification_file)
                wbe_certification_file = fss.url(file)
                print("wbe_certification_file", wbe_certification_file)
            else:
                wbe_certification_file = ''
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

            if request.FILES['VobCertificationFile']:
                vb_certification_file = request.FILES['VobCertificationFile']
                fss = FileSystemStorage()
                file = fss.save(vb_certification_file.name, vb_certification_file)
                vb_certification_file = fss.url(file)
                print("vb_certification_file", vb_certification_file)
            else:
                vb_certification_file = ''

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

            if request.FILES['CobCertificationFile']:
                other_certification_file = request.FILES['CobCertificationFile']
                fss = FileSystemStorage()
                file = fss.save(other_certification_file.name, other_certification_file)
                other_certification_file = fss.url(file)
                print("other_certification_file", other_certification_file)
            else:
                other_certification_file = ''

            # print(request.POST['other_certification_expirationDate'])
            other_certification_expirationDate = str(request.POST['other_certification_expirationDate']).split('-')
            other_certification_expirationDate = datetime.date(int(other_certification_expirationDate[0]), int(other_certification_expirationDate[1]), int(other_certification_expirationDate[2]))
            #--------------------------------------

            #Company Details

            # print(request.POST['presentationDescription'])
            presentationDescription = request.POST['presentationDescription']

            if request.FILES['presentationFile']:
                presentation_file = request.FILES['presentationFile']
                fss = FileSystemStorage()
                file = fss.save(presentation_file.name, presentation_file)
                presentation_file = fss.url(file)
            else:
                presentation_file = ''

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
            salesContact.first_name = sales_contact_first_name
            salesContact.last_name = sales_contact_last_name
            salesContact.email = sales_contact_email
            salesContact.job_title = sales_contact_job_title
            salesContact.phone_number = sales_contact_phone
            salesContact.mobile_number = sales_contact_mobile
            salesContact.save()

            generalContact = GeneralContact()
            generalContact.first_name = general_contact_first_name
            generalContact.last_name = general_contact_last_name
            generalContact.email = general_contact_email
            generalContact.job_title = general_contact_job_title
            generalContact.phone_number = general_contact_phone
            generalContact.mobile_number = general_contact_mobile
            generalContact.save()
            generalContact = GeneralContact.objects.filter(email=general_contact_email).first()

            print("country b", country)
            country = Country.objects.filter(country_name=country).first()


            generalContactInfo = GeneralContactInfo()
            generalContactInfo.company_name = campany_name
            generalContactInfo.website_url = website_url
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
            businessAndCertification.council =  mbe_council
            businessAndCertification.ethnicity = mbe_ethnicity
            businessAndCertification.certification_description = mbe_certificationDescription
            businessAndCertification.certification_file = mbe_certification_file
            businessAndCertification.expiration_date = mbe_expirationDate
            businessAndCertification.save()

            print("wbe_business", wbe_business)
            womenOwnedBusiness = WomenOwnedBusiness()
            womenOwnedBusiness.business = wbe_business
            womenOwnedBusiness.council =  wbe_council
            # womenOwnedBusiness.ethnicity = wbe_ethnicity
            womenOwnedBusiness.certification_description = wbe_certificationDescription
            womenOwnedBusiness.certification_file = wbe_certification_file
            womenOwnedBusiness.expiration_date = wbe_expirationDate
            womenOwnedBusiness.save()

            print("vb_business", vb_business)
            veteranOwnedBusiness = VeteranOwnedBusiness()
            veteranOwnedBusiness.business = vb_business
            veteranOwnedBusiness.council =  vb_council
            # veteranOwnedBusiness.ethnicity = vb_ethnicity
            veteranOwnedBusiness.certification_description = vb_certificationDescription
            veteranOwnedBusiness.certification_file = vb_certification_file
            veteranOwnedBusiness.expiration_date = vb_expirationDate
            veteranOwnedBusiness.save()

            print("other_certification_business", other_certification_business)
            otherCertification = OtherCertification()
            otherCertification.business = other_certification_business
            otherCertification.council =  other_certification_council
            # otherCertification.ethnicity = other_certification_ethnicity
            otherCertification.certification_description = other_certification_certificationDescription
            otherCertification.certification_file = other_certification_file
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
            companyDetails.tax_id_vat_number =  taxIdVatNumber
            companyDetails.total_annaul_sales = totalAnnaulSales
            companyDetails.duns_number =  DunsNumber
            companyDetails.quality_certification = qualityCertification
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
            productionCapabilities.oems = oEMS
            productionCapabilities.abc_supplier = AbcSupplier
            productionCapabilities.vendor_number = vendorNumber
            productionCapabilities.any_other_tier1_automotive_company = anyOtherTier1AutomotiveCompany
            productionCapabilities.nmi = VMI
            productionCapabilities.jit = JIT
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

            productAndService = ProductAndService()
            productAndService.npm_value = npmValue
            productAndService.npm_value_category1 = npmValueCategory1
            productAndService.npm_value_category2 = npmValueCategory2
            productAndService.save()

            productAndService.pm_value = pmValue
            productAndService.pm_value_category1 = pmValueCategory1
            productAndService.pm_value_category2 = pmValueCategory2
            productAndService.additoinal_product_and_services = additoinalProductAndServices
            productAndService.save()

            aBCCorporation = ABCCorporation()
            aBCCorporation.general_contant_info = generalContactInfo
            aBCCorporation.diverse_certification = diverseCertification
            aBCCorporation.company_details = companyDetails
            aBCCorporation.production_capabilities = productionCapabilities
            aBCCorporation.product_and_service = productAndService
            aBCCorporation.save()
            messages.success(request, 'Application successfully submitted')
            return render(request, 'Registrationform.html')
            # except Exception as e:
            #     messages.error(request, e)
            #     print(e)
    except:
        messages.error(request, 'Error while doing registration')



    return render(request, 'Registrationform.html')


def AllRecords(request):
    all_applications = ABCCorporation.objects.all()
    # paginator = Paginator(all_applications, 10)
    # page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, page_number)
    # print("all_applications", page_obj)

    context = {
        'expenses': all_applications,
        'page_obj': all_applications
    }
    return render(request, 'allRecords.html', context)

def mapCountryName(name):
    if name=='WY':
        return "Canada"
    elif name == 'AL':
        return "United States"
    elif name == 'MX':
        return "Maxico"

def DetailRecord(request, id):
    application = ABCCorporation.objects.filter(id=id).first()

    country = Country.objects.filter(country_name=application.general_contant_info.country.country_name).first()
    context = {
        'application': application,
        'country': mapCountryName(country.country_name)
    }
    return render(request, 'detailRecord.html', context)

def BulkUpload(request):
    return render(request, 'bulk.html')

def DownloadSampleExcelFile(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    #decide file name
    response['Content-Disposition'] = 'attachment; filename="bulk_upload_template.xls"'

    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    #adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    #column header names, you can use your own headers here
    columns = ['Company Name', 'Website URL', 'Country', 'Address 1',
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
               'Is your company a veteran-owned business', 'VOB council', 'VOB Certification Description', 'VOB Expiration Date',
               'VOB Certification Upload', 'Is your company certified by another organization?', 'OC council', 'OC Certification Description',
               'OC Expiration Date', 'OC Certification Upload', 'Presentation Upload', 'Description', 'Number of Employees',
               'Tax ID/ VAT Number', 'Total Annual Sales', 'DUNS Number', 'quality certifications', 'Please describe the "other" quality certification',
               'If certification in process, list date expected to finalize', 'Operations outside USA', "Do you currently supply to any OEM's?", 'OEMs',
               'Are you a current supplier to ABC Corporation or have you supplied to ABC Corporation in the past?', 'Vendor Number',
               'Do you supply to any other Tier 1 automotive companies?', 'Do you offer Just In Time (JIT) delivery?',
               'Do you offer Consignment or Vendor Managed Inventory (VMI) ?', 'What is the % of sales that are automotive?',
               'List any significant awards/ recognition your company has received', 'Customer Name 1', '% of Sales 1', 'Automotive - Yes or No 1',
               'Customer Name 2', '% of Sales 2', 'Automotive - Yes or No 2', 'Customer Name 3', '% of Sales 3', 'Automotive - Yes or No 3',
               'Please select all ABC Corporation NA locations you can effectively service *', 'For suppliers providing production parts, please list ALL manufacturing locations',
               'What event did you meet ABC Corporation?', 'Non Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)',
               'Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)',
               'Additional Products and Services: List any additional products and services that you can provide but could not find listed above, Separate each item with a comma (,)',

               ]


    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    #get your data, from database or from a text file...
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
    if id=="Auxiliaries and supplies":
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
    if id=="Raw Material":
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


def UploadExcelFile(request):
    # excel_file = request.FILES["excel_file"]
    #
    # print("excel_file", excel_file)
    #
    # # you may put validations here to check extension or file size
    #
    # wb = openpyxl.load_workbook(excel_file)
    #
    # # getting a particular sheet by name out of many sheets
    # worksheet = wb["Sheet1"]
    # print(worksheet)
    #
    # excel_data = list()
    # # iterating over the rows and
    # # getting value from each cell in row
    # for row in worksheet.iter_rows():
    #     row_data = list()
    #     for cell in row:
    #         row_data.append(str(cell.value))
    #     excel_data.append(row_data)

    try:
        excel_file = request.FILES['excel_file']
        print("excel_file", excel_file)
        data = ""
        # except MultiValueDictKeyError:
        # return redirect(<your_upload_file_failed_url>)
        if (str(excel_file).split('.')[-1] == "csv"):
            data= pd.read_csv(excel_file)



        campany_name = data['Company Name']
        website_url = data['Website URL']
        address1 = data['Address 1']
        address2 = data['Address 2']
        country = data['Country']
        city = data['City']
        state = data['State']
        zip_code = data['Postal Code']


        sales_contact_job_title = data['Sales Job Title']
        sales_contact_phone = data['Sales Office Phone']
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

        mbe_business = data["Is your company certified by the National Minority Supplier Development Council (NMSDC) or one of it's affiliates?"]
        mbe_council = data['MOB council']
        mbe_ethnicity = data['Ethnicity']
        mbe_certificationDescription = data['MOB Certification Description']
        mbe_expirationDate = data['MOB Expiration Date']

        wbe_business = data["Is your company certified by the Women's Business Enterprise National Council Development Council (WBENC) or one of it's affiliates? *"]
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
        AbcSupplier = data['Are you a current supplier to ABC Corporation or have you supplied to ABC Corporation in the past?']
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
        manufacturingLocations = data['For suppliers providing production parts, please list ALL manufacturing locations']
        event = data['What event did you meet ABC Corporation?']

        npmValue = data['Non Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)']

        pmValue = data['Production Material e.g (category>subcategory1>subcategory2,category>subcategory1>subcategory2)']

        additoinalProductAndServices = data['Additional Products and Services: List any additional products and services that you can provide but could not find listed above, Separate each item with a comma (,)']


        for index in range(0,len(campany_name)):
            salesContact = SalesContact()
            salesContact.first_name = sales_contact_first_name[index]
            salesContact.last_name = sales_contact_last_name[index]
            salesContact.email = sales_contact_email[index]
            salesContact.job_title = sales_contact_job_title[index]
            salesContact.phone_number = sales_contact_phone[index]
            salesContact.mobile_number = sales_contact_mobile[index]
            salesContact.save()

            generalContact = GeneralContact()
            generalContact.first_name = general_contact_first_name[index]
            generalContact.last_name = general_contact_last_name[index]
            generalContact.email = general_contact_email[index]
            generalContact.job_title = general_contact_job_title[index]
            generalContact.phone_number = general_contact_phone[index]
            generalContact.mobile_number = general_contact_mobile[index]
            generalContact.save()
            generalContact = GeneralContact.objects.filter(email=general_contact_email[index]).first()

            tempCountry = Country.objects.filter(country_name=country[index]).first()


            generalContactInfo = GeneralContactInfo()
            generalContactInfo.company_name = campany_name[index]
            generalContactInfo.website_url = website_url[index]
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
            businessAndCertification.council =  mbe_council[index]
            businessAndCertification.ethnicity = mbe_ethnicity[index]
            businessAndCertification.certification_description = mbe_certificationDescription[index]
            temp_date = str(mbe_expirationDate[index]).split('/')
            mbe_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
            businessAndCertification.expiration_date = mbe_expirationDate[index]
            print("mbe_expirationDate[index]", mbe_expirationDate[index])
            businessAndCertification.save()

            womenOwnedBusiness = WomenOwnedBusiness()
            womenOwnedBusiness.business = wbe_business[index]
            womenOwnedBusiness.council =  wbe_council[index]
            # womenOwnedBusiness.ethnicity = wbe_ethnicity
            womenOwnedBusiness.certification_description = wbe_certificationDescription[index]
            temp_date = str(wbe_expirationDate[index]).split('/')
            wbe_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
            womenOwnedBusiness.expiration_date = wbe_expirationDate[index]
            womenOwnedBusiness.save()

            veteranOwnedBusiness = VeteranOwnedBusiness()
            print("vb_business[index]", vb_business[index])
            veteranOwnedBusiness.business = vb_business[index]
            veteranOwnedBusiness.council =  vb_council[index]
            # veteranOwnedBusiness.ethnicity = vb_ethnicity
            veteranOwnedBusiness.certification_description = vb_certificationDescription[index]
            temp_date = str(vb_expirationDate[index]).split('/')
            vb_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
            veteranOwnedBusiness.expiration_date = vb_expirationDate[index]
            veteranOwnedBusiness.save()

            otherCertification = OtherCertification()
            otherCertification.business = other_certification_business[index]
            otherCertification.council =  other_certification_council[index]
            # otherCertification.ethnicity = other_certification_ethnicity
            otherCertification.certification_description = other_certification_certificationDescription[index]
            temp_date = str(other_certification_expirationDate[index]).split('/')
            other_certification_expirationDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
            otherCertification.expiration_date = other_certification_expirationDate[index]
            otherCertification.save()

            diverseCertification = DiverseCertification()
            diverseCertification.minority_owned_business = businessAndCertification
            diverseCertification.women_owned_business = womenOwnedBusiness
            diverseCertification.other_certification = otherCertification
            diverseCertification.veteran_owned_business = veteranOwnedBusiness
            diverseCertification.save()

            companyDetails = CompanyDetails()
            companyDetails.presentation_description = presentationDescription[index]
            companyDetails.number_of_employees = numberOfEmployees[index]
            companyDetails.tax_id_vat_number =  taxIdVatNumber[index]
            companyDetails.total_annaul_sales = totalAnnaulSales[index]
            companyDetails.duns_number =  DunsNumber[index]
            companyDetails.quality_certification = qualityCertification[index]
            temp_date = str(certificationExpectedDate[index]).split('/')
            certificationExpectedDate[index] = datetime.date(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
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
            productionCapabilities.vendor_number = vendorNumber[index]
            productionCapabilities.any_other_tier1_automotive_company = anyOtherTier1AutomotiveCompany[index]
            productionCapabilities.nmi = VMI[index]
            productionCapabilities.jit = JIT[index]
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

            productAndService = ProductAndService()

            temp = str(npmValue[index]).split('>')
            tempNpmValue = temp[0]
            npmValueCategory1 = temp[1]
            npmValueCategory2 = temp[2]

            productAndService.npm_value = UnmapNpm(tempNpmValue)
            productAndService.npm_value_category1 = npmValueCategory1
            productAndService.npm_value_category2 = npmValueCategory2
            productAndService.save()


            temp = str(pmValue[index]).split('>')
            tempPmValue = temp[0]
            pmValueCategory1 = temp[1]
            pmValueCategory2 = temp[2]


            productAndService.pm_value = UnmapPm(tempPmValue)
            productAndService.pm_value_category1 = pmValueCategory1
            productAndService.pm_value_category2 = pmValueCategory2
            productAndService.additoinal_product_and_services = additoinalProductAndServices[index]
            productAndService.save()

            aBCCorporation = ABCCorporation()
            aBCCorporation.general_contant_info = generalContactInfo
            aBCCorporation.diverse_certification = diverseCertification
            aBCCorporation.company_details = companyDetails
            aBCCorporation.production_capabilities = productionCapabilities
            aBCCorporation.product_and_service = productAndService
            aBCCorporation.save()

        messages.success(request, 'Data successfully uploaded')

    except:
        messages.error(request, 'Error while uploading data')
        print ("No")



    return render(request , 'bulk.html')

def send_mail_to_client(email, review, customDescription):
    subject = 'Supplier Diversity Registration Form Response'

    if customDescription:
        message = customDescription
    else:
        message = f'Your application is {review}'

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)

def SendResponseToSubmitter(request):
    try:

        ApplicationId = request.POST['ApplicationId']

        general_contact_email = ABCCorporation.objects.filter(id=ApplicationId).first().general_contant_info.general_contact.email

        review = request.POST.get('review', None)

        customDescription = request.POST.get('customDescription', None)

        send_mail_to_client(general_contact_email, review, customDescription)


        return JsonResponse({'data': "Response successfully sent.",'status':200})
    except:
        return JsonResponse({'data': "Error while sending response.",'status':400})


