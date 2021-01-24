from django.urls import path
from .views import add

app_name = 'team'

urlpatterns = [
    path('add/', add, name='add'),
]