from django.urls import path
from . import views as resultsapiviews

app_name = "results"
urlpatterns = [
      path('', resultsapiviews.index, name="index"),
      path('/<str:patient>/', resultsapiviews.index),
      path('/<str:patient>/<str:test>', resultsapiviews.index),
]