from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from .templates import api


# Create your views here.
def index(request):
    return render(request, 'index.html')