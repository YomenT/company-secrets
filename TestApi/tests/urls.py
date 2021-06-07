from django.urls import path
from . import views as testsapiviews

app_name = "tests"
urlpatterns = [
   path('', testsapiviews.index, name="index"),
   path('/<str:patient>/', testsapiviews.index),

]