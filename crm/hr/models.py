from django.db import models
from accounts.models import userEmployee
# Create your models here.

class userEmployeeAttendance(models.Model) :

    empId = models.ForeignKey(userEmployee,on_delete='CASCADE')
    date = models.DateField()
    data = models.CharField()                                   #To Be Fixxed
    comment = models.CharField(max_length=100)
    billed = models.BooleanField(default='false')