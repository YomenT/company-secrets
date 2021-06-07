from api.models import Patient
from .models import Test
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers

def index(request, patient=None):
    if request.method == "GET":
        if patient is None:
            tests = list(Test.objects.all())
        else: 
            patient = Patient.objects.get(name=patient)
            tests = Test.objects.filter(patient=patient)
        res = serializers.serialize('json', tests, use_natural_foreign_keys=True, use_natural_primary_keys=True)
        return JsonResponse(res, safe=False)

