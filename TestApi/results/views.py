from api.models import Patient
from tests.models import Test
from .models import Result
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers

def index(request, patient=None, test=None):
    """
    View to return results
    ---------------------------------
    Can retrieve all, by patient, or by patient and test
    """
    if request.method == "GET":
        if patient is None:
            results = Result.objects.all()
        else:
            tests = list(Test.objects.all())
            patient = Patient.objects.get(name=patient)
            if test is not None:
                print("HERE")
                test = Test.objects.get(test_name=test, patient=patient)
                results = Result.objects.filter(patient=patient, test=test)
            else:
                results = Result.objects.filter(patient=patient)
        

        res = serializers.serialize('json', results, use_natural_foreign_keys=True, use_natural_primary_keys=True)
        return JsonResponse(res, safe=False)