from django.urls import path
from . import views


app_name = 'languages'

urlpatterns = [
    path('', views.index, name='index'),
    path('language/<int:language_id>/', views.language_detail, name='language-detail'),
    path('state/<int:state_id>/', views.state_detail, name='state-detail'),
]
