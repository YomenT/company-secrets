import json
from django.db import models
from .models import Patient

class PatientUtil:
    def __init__(self, request):
        self.__request = request
        body = request.body.decode('utf-8')
        body = json.loads(body)
        self.__body = body

    @property
    def name(self):
        return self.__body['name']

    @property
    def weight(self):
        return self.__body['weight']

    def get_patient(self):
        return Patient.objects.get(name=self.name)
        
    def check_exists(self):
        return Patient.objects.filter(name=self.name).exists()