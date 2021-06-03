import json
from django.db import models
from .models import Patient

class PatientUtil:
    def __init__(self, request):
        
        self.__request = request
        if not self.check_get():
            body = request.body.decode('utf-8')
            body = json.loads(body)
            self.__body = body

    @property
    def name(self):
        if (self.__request.GET.get('name') is not None):
            return self.__request.GET.get('name')
        return self.__body['name']

    @property
    def weight(self):
        if (self.__request.GET.get('weight') is not None):
            return self.__request.GET.get('weight')
        return self.__body['weight']

    def check_get(self):
        return self.__request.GET.get('name') is not None

    def get_patient(self):
        return Patient.objects.get(name=self.name)
        
    def check_exists(self):
        return Patient.objects.filter(name=self.name).exists()