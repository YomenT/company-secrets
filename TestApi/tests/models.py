from django.db import models
from api.models import Patient
from django.core import serializers

class TestManager(models.Manager):
    def get_by_natural_key(self,test_name):
        return self.get( test_name=test_name)

class Test(models.Model):
    """
    Model to demonstrate applicable test results
    """
    test_name = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['test_name']] 

    objects = TestManager()

    def natural_key(self):
        return (self.test_name)


