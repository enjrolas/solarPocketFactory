from django.db import models
from django.forms import ModelForm

class FactoryState(models.Model):
    #mapping
    _1ma
    _2ma
    _3ma
    command  =   models.CharField(max_length=20)
    commandTimeStamp    =   models.DateTimeField(auto_now=True)
    parameter=models.FloatField()
    status      =   models.CharField(max_length=20)
    statusTimeStamp   =   models.DateTimeField(auto_now=True)
    description = models.TextField()
    json = models.TextField()

