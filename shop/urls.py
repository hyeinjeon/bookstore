from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', show_list, name="list"),
    path('<int:id>/<product_slug>/', product_detail, name="product_detail"),
]