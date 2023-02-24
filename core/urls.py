from django.urls import path
from .views import test_logging

urlpatterns = [
    path('test-log/', test_logging, name='test-log')
]