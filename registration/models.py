from django.db import models
from django.utils.timezone import now

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class CompanyDetails(models.Model):
    presentation_description =models.CharField(max_length=266, default='N', null=False, blank=False)
    presentation_file = models.CharField(max_length=255, default='')
    number_of_employees = models.BigIntegerField(null=False, blank=False)
    tax_id_vat_number =  models.CharField(max_length=266)
    total_annaul_sales = models.CharField(max_length=266, null=False, blank=False)
    duns_number =  models.CharField(max_length=266)
    quality_certification = models.CharField(max_length=266, null=False, blank=False)
    # otherQualityCertification = models.CharField(max_length=266)
    certification_expected_date = models.DateField(null=True, blank= True)
    operation_outside_usa = models.CharField(max_length=266, null=False, blank=False)

class GeneralContact(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    job_title = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.BigIntegerField(null=False, blank=False)
    mobile_number = models.BigIntegerField(null=True, blank=True)

class SalesContact(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    job_title = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.BigIntegerField(null=False, blank=False)
    mobile_number = models.BigIntegerField(null=True, blank=True)

class BusinessAndCertification(models.Model):
    business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    certification_description = models.CharField(max_length=255)
    expiration_date = models.DateField(null=True, blank=True)
    certification_file = models.CharField(max_length=255, default='')

class WomenOwnedBusiness(models.Model):
    business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    # ethnicity = models.CharField(max_length=255)
    certification_description = models.CharField(max_length=255)
    expiration_date = models.DateField(null=True, blank=True)
    certification_file = models.CharField(max_length=255, default='')

class VeteranOwnedBusiness(models.Model):
    business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    # ethnicity = models.CharField(max_length=255)
    certification_description = models.CharField(max_length=255)
    expiration_date = models.DateField(null=True, blank=True)
    certification_file = models.CharField(max_length=255, default='')

class OtherCertification(models.Model):
    business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    # ethnicity = models.CharField(max_length=255)
    certification_description = models.CharField(max_length=255)
    expiration_date = models.DateField(null=True, blank=True)
    certification_file = models.CharField(max_length=255, default='')

class Country(models.Model):
    country_name = models.CharField(max_length=255, null=False, blank=False)

class GeneralContactInfo(models.Model):
    company_name = models.CharField(max_length=255, null=False, blank=False)
    website_url = models.CharField(max_length=255, null=False, blank=False)
    video_url = models.CharField(max_length=1255, null=True, blank=True, default='')
    company_video_file = models.CharField(max_length=255, null=True, blank=True, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=255, null=False, blank=False)
    address2 = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False)
    zip_code = models.BigIntegerField(null=False, blank=False)
    sales_contact = models.ForeignKey(SalesContact, on_delete=models.CASCADE)
    general_contact = models.ForeignKey(GeneralContact, on_delete=models.CASCADE)

class DiverseCertification(models.Model):
    minority_owned_business = models.ForeignKey(BusinessAndCertification, on_delete=models.CASCADE)
    women_owned_business = models.ForeignKey(WomenOwnedBusiness, on_delete=models.CASCADE)
    veteran_owned_business = models.ForeignKey(VeteranOwnedBusiness, on_delete=models.CASCADE)
    other_certification = models.ForeignKey(OtherCertification, on_delete=models.CASCADE)

class OEMS(models.Model):
    name = models.CharField(max_length=255)

class NaLocation(models.Model):
    name = models.CharField(max_length=255)

class ProductionCapabilities(models.Model):
    isOem = models.BooleanField(null=False, blank=False)
    oems = models.ForeignKey(OEMS, on_delete=models.CASCADE, null=True, blank=True)
    abc_supplier = models.BooleanField(null=False, blank=False)
    vendor_number = models.IntegerField(null=True, blank=True)
    any_other_tier1_automotive_company = models.BooleanField()
    nmi = models.BooleanField(default=False)
    jit = models.BooleanField(default=False)
    percentage_sale = models.BigIntegerField(null=True, blank=True)
    significant_awards = models.CharField(max_length=1055, null=False, blank=False)
    customer_name1 = models.CharField(max_length=255, null=False, blank=False)
    sales1 = models.BigIntegerField(null=False, blank=False)
    automotive1 = models.BooleanField(null=False, blank=False)
    customer_name2 = models.CharField(max_length=255, null=False, blank=False)
    sales2 = models.BigIntegerField(null=False, blank=False)
    automotive2 = models.BooleanField(null=False, blank=False)
    customer_name3 = models.CharField(max_length=255, null=False, blank=False)
    sales3 = models.BigIntegerField(null=False, blank=False)
    automotive3 = models.BooleanField(null=False, blank=False)
    record_per_naLocation = models.ForeignKey(NaLocation, on_delete=models.CASCADE)
    manufacturing_locations = models.CharField(max_length=1055)
    event = models.CharField(max_length=1055, null=True, blank=True)

class NpmCategory(models.Model):
    name = models.CharField(max_length=255)


class NpmSubCategory(models.Model):
    parent_id = models.BigIntegerField()
    name = models.CharField(max_length=255)

class PmCategory(models.Model):
    name = models.CharField(max_length=255)


class PmSubCategory(models.Model):
    parent_id = models.BigIntegerField()
    name = models.CharField(max_length=255)

class ProductAndService(models.Model):
    npm_value = models.CharField(max_length=255, null=True, blank=True)
    npm_value_category1 = models.CharField(max_length=255, null=True, blank=True)
    npm_value_category2 = models.CharField(max_length=255, null=True, blank=True)

    pm_value = models.CharField(max_length=255, null=True, blank=True)
    pm_value_category1 = models.CharField(max_length=255, null=True, blank=True)
    pm_value_category2 = models.CharField(max_length=255, null=True, blank=True)
    additoinal_product_and_services = models.CharField(max_length=1055, null=True, blank=True)

class ApplicationResponse(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.CharField(max_length=1055)
    to = models.CharField(max_length=1055)

class ApplicationEmailed(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.CharField(max_length=1055)
    to = models.CharField(max_length=1055)

class NpmValues(models.Model):
    abc_corporation_id = models.IntegerField()
    npm_value = models.CharField(max_length=255)
    npm_value_category1 = models.CharField(max_length=255)
    npm_value_category2 = models.CharField(max_length=255)

class PmValues(models.Model):
    abc_corporation_id = models.IntegerField()
    pm_value = models.CharField(max_length=255)
    pm_value_category1 = models.CharField(max_length=255)
    pm_value_category2 = models.CharField(max_length=255)

class ABCCorporation(models.Model):
    general_contant_info = models.ForeignKey(GeneralContactInfo, on_delete=models.CASCADE)
    diverse_certification = models.ForeignKey(DiverseCertification, on_delete=models.CASCADE)
    company_details = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    production_capabilities = models.ForeignKey(ProductionCapabilities, on_delete=models.CASCADE)
    # product_and_service = models.ForeignKey(ProductAndService, on_delete=models.CASCADE)
    response = models.BigIntegerField(default=0)
    emailed = models.BigIntegerField(default=0)

class Feedback(models.Model):
    application_id = models.BigIntegerField(null=False, default=0)
    email = models.EmailField(_('email address'), null=False, blank=False)
    feedback = models.CharField(max_length=1055, null=True, blank=True)
    feedback_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(null=True)

class Notes(models.Model):
    application_id = models.BigIntegerField(null=False, default=0)
    feedback = models.CharField(max_length=1055, null=True, blank=True)
    user_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)













