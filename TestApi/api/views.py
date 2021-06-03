from api.models import Patient
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .patientutil import PatientUtil
from django.core import serializers

@csrf_exempt
def controller(request):
    """
    Controller for our test patient API endpoint
    """
    util = PatientUtil(request)

    if request.method == "GET":
        return get_patient(request, util)

    if request.method == "POST":
        return create_patient(request, util)
    
    if request.method == "PATCH":
        return update_patient(request, util)
    
    if request.method == "DELETE":
        return delete_patient(request, util)
    
    
@csrf_exempt
def get_patient(request, util):
    """
    Get a patient with a given name
    """
    try:
        patient = serializers.serialize('json', [util.get_patient()], fields=('name','size'))
    except:
        return HttpResponse(status=404)
    
    return JsonResponse(patient, safe=False)

@csrf_exempt
def create_patient(request, util):
    """
    Create a new patient
    """

    #if patient exists, do not create new record (name must be unique)
    if (util.check_exists()):
        return HttpResponse(status=409)
    
    new_patient = Patient()
    new_patient.name = util.name
    new_patient.weight = util.weight
    new_patient.save()
    return HttpResponse(status=204)

@csrf_exempt
def update_patient(request, util):
    """
    Update weight of a patient
    """
    if (not util.check_exists()):
        return HttpResponse(status=404)

    patient_to_update = util.get_patient()
    patient_to_update.weight = util.weight

    return HttpResponse(status=204)

@csrf_exempt
def delete_patient(self, util):
    """
    Delete a patient based on name
    """
    if (not util.check_exists()):
        return HttpResponse(status=404)
    
    patient_to_delete = util.get_patient()
    patient_to_delete.delete()

    return HttpResponse(status=204)