from django.db import models
from django.forms import ModelForm

class Command(models.Model):
    command  =   models.CharField(max_length=20)
    commandTimeStamp    =   models.DateTimeField(auto_now=True)
    parameter=models.FloatField()
    status      =   models.CharField(max_length=20)
    statusTimeStamp   =   models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
