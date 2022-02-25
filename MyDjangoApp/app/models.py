from django.db import models


class Landlord(models.Model):
    """ Model Landlord specifying all attributes related to Landlord """
    surname = models.CharField(max_length=30, blank=False)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    nationalid = models.BigIntegerField()
    birthday = models.DateField()
    email = models.EmailField(max_length=30, blank=True, default='-', null=True)
    primarycontact = models.BigIntegerField(blank=True, default='-', null=True)
    othercontact = models.BigIntegerField(blank=True, default='-', null=True)
    gender = models.CharField(max_length=7)


class WaterMeter(models.Model):
    meternumber = models.CharField(max_length=50,)
    previousreading = models.CharField(max_length=50,)
    currentreading = models.CharField(max_length=50,)


class ElectricityMeter(models.Model):
    electricitymeternumber = models.CharField(max_length=50)
    previousreading = models.CharField(max_length=50)
    currentreading = models.CharField(max_length=50)


class Building(models.Model):
    landlordid = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    watermeternumber = models.OneToOneRel(WaterMeter, on_delete=models.CASCADE, field_name='watermeternumber', to='')
    electricitymeternumber = models.OneToOneRel(ElectricityMeter, on_delete=models.CASCADE, field_name='electricitymeternumber', to='')
    commissionrate = models.FloatField(max_length=4)
    interestrate = models.FloatField(max_length=4)
    waterrate = models.FloatField()
    electricityrate = models.FloatField()


class House(models.Model):
    STATUS = [
        ('VACCANT', 'Vaccant'),
        ('RENTED', 'Rented')
    ]
    buildingid = models.ForeignKey(Building, on_delete=models.CASCADE,)
    description = models.TextField(max_length=50)
    rent = models.IntegerField()
    deposit = models.IntegerField()
    garbagefee = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=7)
    rentduedate = models.DateField()


class Tenant(models.Model):
    surname = models.CharField(max_length=30, blank=False)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    nationalid = models.BigIntegerField()
    birthday = models.DateField()
    email = models.EmailField(max_length=30, blank=True, default='-', null=True)
    primarycontact = models.IntegerField(blank=True, default='-', null=True)
    othercontact = models.IntegerField(blank=True, default='-', null=True)
    gender = models.CharField(max_length=7)
    housenumber = models.ForeignKey(House, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=30, blank=True, default='-', null=True)


class Group(models.Model):
    groupname = models.CharField(max_length=20)
    housesassigned = models.ForeignKey(House, on_delete=models.CASCADE)


class GroupMember(models.Model):
    groupid = models.ForeignKey(Group, on_delete=models.CASCADE)
    surname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('CASH', 'Cash'),
        ('MPESA', 'Mpesa'),
        ('COOP-BANK', 'Cooperative Bank'),
        ('EQUITY-BANK', 'Equity Bank'),
    ]
    transationtype = models.CharField(choices=TRANSACTION_TYPE, max_length=15)
    datepaid = models.DateField()
    amountpaid = models.IntegerField()
    description = models.TextField(max_length=20)
    tenantid = models.ForeignKey(Tenant, on_delete=models.CASCADE)
