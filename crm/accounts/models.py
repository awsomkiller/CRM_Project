from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
    )



#Type of Gov Id
govId_choices =(
    ('aadhar card','AADHAR CARD'),
    ('driving license', 'DRIVING LICENSE'),
    ('passport','PASSPORT'),
    ('other','OTHER'),
)

# Create your models here.
class userEmployee(AbstractBaseUser):
    userName = models.CharField(max_length=7, primary_key=True)
    emailId  = models.EmailField(max_length=50,unique=True)
    fullName = models.CharField(max_length=100)
    dob = models.DateField()
    contactNo = models.IntegerField() 
    panNo = models.CharField(max_length=10) 
    govIdType = models.CharField(max_length=20, choices=govId_choices,default='aadhar card')
    govId = models.IntegerField() 
    seniorId = models.CharField(max_length=7)
    password = models.CharField(max_length=100)
    superUser = models.BooleanField(default=False) 
    manager = models.BooleanField(default=False) 
    Hr = models.BooleanField(default=False) 
    active = models.BooleanField(default=False) 

    USERNAME_FIELD = 'userName'

    REQUIRED_FIELD = []

    def __str__(self):
        return self.userName
    
    def get_full_name(self):
        return self.fullName

    @property
    def is_superUser(self):
        return self.superUser
    
    @property
    def is_hr(self):
        return self.Hr

    @property
    def is_active(self):
        return self.active

    @property
    def is_manager(self):
        return self.manager


class userCustomer(models.Model) :

    fullName= models.CharField(max_length=100)
    emailId = models.EmailField(max_length=50,unique=True)
    contactNo = models.IntegerField()
    address = models.CharField(max_length=250)
    govIdType = models.CharField(max_length=20, choices=govId_choices,default='aadhar card')
    govId = models.IntegerField()
    isActive = models.BooleanField(default=False)
    creationDate = models.DateField()
    creator = models.ForeignKey(userEmployee,on_delete='PROTECT')