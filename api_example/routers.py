from rest_framework import routers
from apps.languages.viewsets import LanguageViewSet, StateViewSet


router = routers.DefaultRouter()

router.register('languages', LanguageViewSet)
router.register('states', StateViewSet)
