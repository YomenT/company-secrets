from django.db import models
from django.core import serializers

class PatientManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

# Create your models here.
class Patient(models.Model):
    """
    Model to mock patient data
    """ 
    name = models.CharField(max_length=255)
    weight = models.IntegerField()    

    objects = PatientManager()

    def natural_key(self):
        return (self.name)

