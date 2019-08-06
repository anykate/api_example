from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.LanguageView)

urlpatterns = [
    path('languages/', include(router.urls), name='api_language'),
]
