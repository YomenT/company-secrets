from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from api.models import Patient
from tests.models import Test

# Create your models here.
class Result(models.Model):
    """
    Model to demo test result for given patient and test
    """
    result = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=CASCADE)

