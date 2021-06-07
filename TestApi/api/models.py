from django.db import models

# Create your models here.
class Patient(models.Model):
    """
    Model to mock patient data
    """ 
    name = models.CharField(max_length=255)
    weight = models.IntegerField()    