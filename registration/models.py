from django.db import models
from django.utils.timezone import now

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class CompanyDetails(models.Model):
    presentationDescription =models.CharField(max_length=266, default='N', null=False, blank=False)
    numberOfEmployees = models.IntegerField(null=False, blank=False)
    taxIdVatNumber =  models.CharField(max_length=266)
    totalAnnaulSales = models.CharField(max_length=266, null=False, blank=False)
    DunsNumber =  models.CharField(max_length=266)
    qualityCertification = models.CharField(max_length=266, null=False, blank=False)
    # otherQualityCertification = models.CharField(max_length=266)
    certificationExpectedDate = models.DateField()
    operationOutsideUsa = models.CharField(max_length=266, null=False, blank=False)

class GeneralContact(models.Model):
    firstName = models.CharField(max_length=255, null=False, blank=False)
    lastName = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    jobTitle = models.CharField(max_length=255, null=False, blank=False)
    phoneNumber = models.IntegerField(null=False, blank=False)
    MobileNumber = models.IntegerField()

class SalesContact(models.Model):
    firstName = models.CharField(max_length=255, null=False, blank=False)
    lastName = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    jobTitle = models.CharField(max_length=255, null=False, blank=False)
    phoneNumber = models.IntegerField(null=False, blank=False)
    MobileNumber = models.IntegerField()

class BusinessAndCertification(models.Model):
    Business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    certificationDescription = models.CharField(max_length=255)
    expirationDate = models.DateField()

class WomenOwnedBusiness(models.Model):
    Business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    # ethnicity = models.CharField(max_length=255)
    certificationDescription = models.CharField(max_length=255)
    expirationDate = models.DateField()

class VeteranOwnedBusiness(models.Model):
    Business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    certificationDescription = models.CharField(max_length=255)
    expirationDate = models.DateField()

class OtherCertification(models.Model):
    Business = models.CharField(max_length=255, null=False, blank=False)
    council =  models.CharField(max_length=255)
    # ethnicity = models.CharField(max_length=255)
    certificationDescription = models.CharField(max_length=255)
    expirationDate = models.DateField()

class Country(models.Model):
    countryName = models.CharField(max_length=255, null=False, blank=False)

class GeneralContactInfo(models.Model):
    companyName = models.CharField(max_length=255, null=False, blank=False)
    websiteUrl = models.CharField(max_length=255, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=255, null=False, blank=False)
    address2 = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False)
    zipCode = models.IntegerField(null=False, blank=False)
    SalesContact = models.ForeignKey(SalesContact, on_delete=models.CASCADE)
    GeneralContact = models.ForeignKey(GeneralContact, on_delete=models.CASCADE)

class DiverseCertification(models.Model):
    MinorityOwnedBusiness = models.ForeignKey(BusinessAndCertification, on_delete=models.CASCADE)
    WomenOwnedBusiness = models.ForeignKey(WomenOwnedBusiness, on_delete=models.CASCADE)
    VeteranOwnedBusiness = models.ForeignKey(VeteranOwnedBusiness, on_delete=models.CASCADE)
    OtherCertification = models.ForeignKey(OtherCertification, on_delete=models.CASCADE)

class OEMS(models.Model):
    name = models.CharField(max_length=255)

class NaLocation(models.Model):
    name = models.CharField(max_length=255)

class ProductionCapabilities(models.Model):
    isOem = models.BooleanField(null=False, blank=False)
    OEMS = models.ForeignKey(OEMS, on_delete=models.CASCADE)
    AbcSupplier = models.BooleanField(null=False, blank=False)
    vendorNumber = models.IntegerField()
    anyOtherTier1AutomotiveCompany = models.BooleanField()
    VMI = models.BooleanField()
    JIT = models.BooleanField()
    percentageSale = models.IntegerField()
    significantAwards = models.CharField(max_length=1055, null=False, blank=False)
    customerName1 = models.CharField(max_length=255, null=False, blank=False)
    sales1 = models.IntegerField(null=False, blank=False)
    automotive1 = models.BooleanField(null=False, blank=False)
    customerName2 = models.CharField(max_length=255, null=False, blank=False)
    sales2 = models.IntegerField(null=False, blank=False)
    automotive2 = models.BooleanField(null=False, blank=False)
    customerName3 = models.CharField(max_length=255, null=False, blank=False)
    sales3 = models.IntegerField(null=False, blank=False)
    automotive3 = models.BooleanField(null=False, blank=False)
    recordPerNaLocation = models.ForeignKey(NaLocation, on_delete=models.CASCADE)
    manufacturingLocations = models.CharField(max_length=1055)
    event = models.CharField(max_length=1055)

class NpmCategory(models.Model):
    name = models.CharField(max_length=255)


class NpmSubCategory(models.Model):
    parent_id = models.IntegerField()
    name = models.CharField(max_length=255)

class PmCategory(models.Model):
    name = models.CharField(max_length=255)


class PmSubCategory(models.Model):
    parent_id = models.IntegerField()
    name = models.CharField(max_length=255)

class ProductAndService(models.Model):
    npmValue = models.CharField(max_length=255)
    npmValueCategory1 = models.CharField(max_length=255)
    npmValueCategory2 = models.CharField(max_length=255)

    pmValue = models.CharField(max_length=255)
    pmValueCategory1 = models.CharField(max_length=255)
    pmValueCategory2 = models.CharField(max_length=255)
    additoinalProductAndServices = models.CharField(max_length=1055)

class ABCCorporation(models.Model):
    generalContantInfo = models.ForeignKey(GeneralContactInfo, on_delete=models.CASCADE)
    diverseCertification = models.ForeignKey(DiverseCertification, on_delete=models.CASCADE)
    companyDetails = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    productionCapabilities = models.ForeignKey(ProductionCapabilities, on_delete=models.CASCADE)
    productAndService = models.ForeignKey(ProductAndService, on_delete=models.CASCADE)











