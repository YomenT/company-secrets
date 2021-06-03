from django.urls import path
from . import views as ui

app_name = "ui"
urlpatterns = [
    path('', ui.index, name="index")
]