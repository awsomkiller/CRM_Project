from django.db import models
from accounts.models import userEmployee,userCustomer

# Create your models here.
class serviceType(models.Model):
    id = models.CharField(max_length=7, primary_key=True)                 #service Id
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(userEmployee,on_delete='PROTECT')
    isActive = models.BooleanField(default='true')

class servicePlans (models.Model) :
    id = models.CharField(max_length=7, primary_key=True)                  #plan Id
    serviceId = models.ForeignKey(serviceType,on_delete='PROTECT')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.IntegerField()
    creator = models.ForeignKey(userEmployee,on_delete='PROTECT')
    isActive = models.BooleanField(default='true')

class userServicePlan (models.Model):
    
    id = models.CharField(max_length=7, primary_key=True)                  #connection Id
    userId = models.ForeignKey(userCustomer,on_delete='PROTECT')
    planId = models.ForeignKey(servicePlans,on_delete='PROTECT')
    dateOfBooking = models.DateField()
    dateOfBill = models.DateField()
    dueDate = models.DateField()