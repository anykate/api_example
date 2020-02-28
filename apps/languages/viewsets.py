from rest_framework import viewsets
from .models import Language, State
from .serializers import LanguageSerializer, StateSerializer


# Create your views here.
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
