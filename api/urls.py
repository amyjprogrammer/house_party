from django.urls import path

from .views import main

app_name = 'music'

urlpatterns = [
    path('', main),
]