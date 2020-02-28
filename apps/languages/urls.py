from django.urls import path
from . import views


app_name = 'languages'

urlpatterns = [
    path('', views.index, name='index'),
]
