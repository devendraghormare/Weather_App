
from weather import views
from django.urls import URLPattern
from django.urls import path

urlpatterns = [
    path('', views.index)
]
