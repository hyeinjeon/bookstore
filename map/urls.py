from django.urls import path
from .views import *

app_name = 'map'

urlpatterns = [
    path('search/', search, name="api_search"),
]