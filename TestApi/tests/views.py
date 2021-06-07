from api.models import Patient
from .models import Test
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers

def index(request):
    if request.method == "GET":
        tests = list(Test.objects.all())
        res = serializers.serialize('json', tests)
        return JsonResponse(res, safe=False)