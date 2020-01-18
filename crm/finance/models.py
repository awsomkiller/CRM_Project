from django.db import models
from branches.models import userServicePlan
from accounts.models import userEmployee

# Create your models here.
class userCustomerBill (models.Model):

    id = models.CharField(max_length=7, primary_key=True)  
    amount = models.IntegerField()
    receipt = models.ForeignKey(userCustomerReceipt,on_delete='PROTECT')
    connectionId = models.ForeignKey(userServicePlan,on_delete='PROTECT')

class userCustomerReceipt(models.Model):

    id = models.CharField(max_length=7, primary_key=True)  
    transactionId = models.ForeignKey(userCustomerTransaction, on_delete='PROTECT')
    connectionId = models.ForeignKey(userServicePlan,on_delete='PROTECT')
    billId = models.ForeignKey(userCustomerBill,on_delete='PROTECT')

class userCustomerTransaction(models.Model):

    id = models.CharField(max_length=7, primary_key=True)  
    billId = models.ForeignKey(userCustomerBill,on_delete='PROTECT')
    modeOfTransaction = models.CharField()

class userEmployeePackage(model.Model):
    id = models.CharField(max_length=7, primary_key=True)  
    userId = models.ForeignKey(userEmployee,on_delete='CASCADE')
    amount = models.IntegerField()
    description = models.CharField(max_length=250)
    isActive = models.BooleanField(default='true')

class userEmployeePaymentBill(model.Model):
    id = models.CharField(max_length=7, primary_key=True)  
    packageId = models.ForeignKey(userEmployeePackage, on_delete='PROTECT')
    totalAttendance = models.IntegerField()
    totalDays = models.DateField()
    paymentReceipt = models.ForeignKey(userPaymentReceipt, on_delete='PROTECT')
    amount = models.IntegerField()
    

class userPaymentReceipt(model.Model):
    id = models.CharField(max_length=7, primary_key=True)  
    amount = models.IntegerField()
    salaryMonth = models.CharField(max_length=10)
    dateOfPayment = models.DateField()
    modeOfPayment = models.CharField(max_length=10)
    comments = models.CharField(max_length=100)