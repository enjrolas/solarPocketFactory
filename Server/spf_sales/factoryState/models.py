from django.db import models
from django.forms import ModelForm

class FactoryState(models.Model):
    #mapping
    _1ma=models.IntegerField()
    _2ma=models.IntegerField()
    _3ma=models.IntegerField()
    _4ma=models.IntegerField()

    #axis settings
    
    #feed rate
    _xfr=models.IntegerField()
    _yfr=models.IntegerField()
    _zfr=models.IntegerField()
    _afr=models.IntegerField()

    #max velocity
    _xvm=models.IntegerField()
    _yvm=models.IntegerField()
    _zvm=models.IntegerField()
    _avm=models.IntegerField()

    #travel
    _xtr=models.FloatField()
    _ytr=models.FloatField()
    _ztr=models.FloatField()
    _atr=models.FloatField()

    #step angle
    _xsa=models.FloatField()
    _ysa=models.FloatField()
    _zsa=models.FloatField()
    _asa=models.FloatField()

    #power mode
    _1pm=models.IntegerField()
    _2pm=models.IntegerField()
    _3pm=models.IntegerField()
    _4pm=models.IntegerField()
    
    #raw materials in stock
    solettesInHopper=models.IntegerField()  #number of solettes
    tabbingOnSpool=models.IntegerField()  #mm of tabbing
    backingsInHopper=models.IntegerField()  #number of backings
    encapsulantInTub=models.IntegerField()  #ccs of encapsulant

    backingWidth=models.FloatField()  #in mm
    backingLength=models.FloatField() #in mm

    soletteWidth=models.FloatField()  #in mm
    soletteLength=models.FloatField()  # in mm
