from django.urls import path
from . import views as apiviews

app_name = "api"
urlpatterns = [
    path('', apiviews.controller, name="controller")
]