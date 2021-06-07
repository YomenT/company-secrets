from django.db import models
from api.models import Patient

class Test(models.Model):
    """
    Model to demonstrate applicable test results
    """
    test_name = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
